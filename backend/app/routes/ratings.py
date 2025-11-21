from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models.user import User
from ..models.rating import Rating
from ..models.moving_request import MovingRequest
from ..models.quote import Quote
from ..schemas.rating import RatingCreate, RatingResponse
from ..utils.dependencies import get_current_user

router = APIRouter(prefix="/api/ratings", tags=["Ratings"])

@router.post("", response_model=RatingResponse, status_code=status.HTTP_201_CREATED)
def create_rating(
    rating_data: RatingCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Créer une nouvelle notation"""
    # Vérifier que la demande existe
    moving_request = db.query(MovingRequest).filter(
        MovingRequest.id == rating_data.moving_request_id
    ).first()
    
    if not moving_request:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Moving request not found"
        )
    
    # Vérifier que c'est le client qui possède la demande
    if moving_request.client_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to rate this mover"
        )
    
    # Vérifier que le déménagement est terminé
    if moving_request.status != "completed":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot rate before the move is completed"
        )
    
    # Vérifier qu'un devis accepté existe pour ce déménageur
    accepted_quote = db.query(Quote).filter(
        Quote.moving_request_id == rating_data.moving_request_id,
        Quote.mover_id == rating_data.mover_id,
        Quote.status == "accepted"
    ).first()
    
    if not accepted_quote:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No accepted quote found for this mover"
        )
    
    # Vérifier qu'une notation n'existe pas déjà
    existing_rating = db.query(Rating).filter(
        Rating.moving_request_id == rating_data.moving_request_id,
        Rating.mover_id == rating_data.mover_id
    ).first()
    
    if existing_rating:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You have already rated this mover for this move"
        )
    
    new_rating = Rating(
        moving_request_id=rating_data.moving_request_id,
        mover_id=rating_data.mover_id,
        client_id=current_user.id,
        rating=rating_data.rating,
        comment=rating_data.comment
    )
    
    db.add(new_rating)
    
    # Mettre à jour la moyenne du déménageur
    mover = db.query(User).filter(User.id == rating_data.mover_id).first()
    if mover:
        all_ratings = db.query(Rating).filter(Rating.mover_id == rating_data.mover_id).all()
        total_rating = sum(r.rating for r in all_ratings) + rating_data.rating
        count = len(all_ratings) + 1
        mover.average_rating = total_rating / count
        mover.total_ratings = count
    
    db.commit()
    db.refresh(new_rating)
    
    return RatingResponse.model_validate(new_rating)

@router.get("/user/{user_id}", response_model=List[RatingResponse])
def get_user_ratings(
    user_id: int,
    db: Session = Depends(get_db)
):
    """Obtenir les notations d'un utilisateur (déménageur)"""
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    if not user.is_mover:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User is not a mover"
        )
    
    ratings = db.query(Rating).filter(Rating.mover_id == user_id).order_by(Rating.created_at.desc()).all()
    return [RatingResponse.model_validate(rating) for rating in ratings]
