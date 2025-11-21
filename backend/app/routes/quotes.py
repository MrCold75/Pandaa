from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models.user import User
from ..models.quote import Quote
from ..models.moving_request import MovingRequest
from ..schemas.quote import QuoteCreate, QuoteUpdate, QuoteResponse
from ..utils.dependencies import get_current_user, get_current_mover

router = APIRouter(prefix="/api/quotes", tags=["Quotes"])

@router.post("", response_model=QuoteResponse, status_code=status.HTTP_201_CREATED)
def create_quote(
    quote_data: QuoteCreate,
    current_user: User = Depends(get_current_mover),
    db: Session = Depends(get_db)
):
    """Créer un nouveau devis (réservé aux déménageurs)"""
    # Vérifier que la demande existe
    moving_request = db.query(MovingRequest).filter(
        MovingRequest.id == quote_data.moving_request_id
    ).first()
    
    if not moving_request:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Moving request not found"
        )
    
    # Vérifier qu'un devis n'existe pas déjà pour ce déménageur
    existing_quote = db.query(Quote).filter(
        Quote.moving_request_id == quote_data.moving_request_id,
        Quote.mover_id == current_user.id
    ).first()
    
    if existing_quote:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You have already submitted a quote for this request"
        )
    
    new_quote = Quote(
        moving_request_id=quote_data.moving_request_id,
        mover_id=current_user.id,
        price=quote_data.price,
        estimated_duration=quote_data.estimated_duration,
        description=quote_data.description,
        includes_packing=1 if quote_data.includes_packing else 0,
        includes_unpacking=1 if quote_data.includes_unpacking else 0,
        includes_insurance=1 if quote_data.includes_insurance else 0
    )
    
    db.add(new_quote)
    db.commit()
    db.refresh(new_quote)
    
    return QuoteResponse.model_validate(new_quote)

@router.get("", response_model=List[QuoteResponse])
def list_quotes(
    moving_request_id: int = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Lister les devis"""
    query = db.query(Quote)
    
    if moving_request_id:
        # Vérifier les permissions
        moving_request = db.query(MovingRequest).filter(
            MovingRequest.id == moving_request_id
        ).first()
        
        if not moving_request:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Moving request not found"
            )
        
        if not current_user.is_mover and moving_request.client_id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized to view these quotes"
            )
        
        query = query.filter(Quote.moving_request_id == moving_request_id)
    elif current_user.is_mover:
        # Les déménageurs voient leurs propres devis
        query = query.filter(Quote.mover_id == current_user.id)
    else:
        # Les clients voient les devis de leurs demandes
        query = query.join(MovingRequest).filter(MovingRequest.client_id == current_user.id)
    
    quotes = query.order_by(Quote.created_at.desc()).all()
    return [QuoteResponse.model_validate(quote) for quote in quotes]

@router.get("/{quote_id}", response_model=QuoteResponse)
def get_quote(
    quote_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Obtenir les détails d'un devis"""
    quote = db.query(Quote).filter(Quote.id == quote_id).first()
    
    if not quote:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Quote not found"
        )
    
    # Vérifier les permissions
    moving_request = db.query(MovingRequest).filter(
        MovingRequest.id == quote.moving_request_id
    ).first()
    
    if not current_user.is_mover or quote.mover_id == current_user.id:
        pass  # Le déménageur peut voir son propre devis
    elif moving_request.client_id == current_user.id:
        pass  # Le client peut voir les devis de sa demande
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to view this quote"
        )
    
    return QuoteResponse.model_validate(quote)

@router.put("/{quote_id}/accept", response_model=QuoteResponse)
def accept_quote(
    quote_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Accepter un devis (réservé aux clients)"""
    quote = db.query(Quote).filter(Quote.id == quote_id).first()
    
    if not quote:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Quote not found"
        )
    
    # Vérifier que c'est le client qui possède la demande
    moving_request = db.query(MovingRequest).filter(
        MovingRequest.id == quote.moving_request_id
    ).first()
    
    if moving_request.client_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to accept this quote"
        )
    
    quote.status = "accepted"
    moving_request.status = "accepted"
    
    # Rejeter les autres devis
    other_quotes = db.query(Quote).filter(
        Quote.moving_request_id == quote.moving_request_id,
        Quote.id != quote_id
    ).all()
    
    for other_quote in other_quotes:
        other_quote.status = "rejected"
    
    db.commit()
    db.refresh(quote)
    
    return QuoteResponse.model_validate(quote)

@router.put("/{quote_id}/reject", response_model=QuoteResponse)
def reject_quote(
    quote_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Refuser un devis (réservé aux clients)"""
    quote = db.query(Quote).filter(Quote.id == quote_id).first()
    
    if not quote:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Quote not found"
        )
    
    # Vérifier que c'est le client qui possède la demande
    moving_request = db.query(MovingRequest).filter(
        MovingRequest.id == quote.moving_request_id
    ).first()
    
    if moving_request.client_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to reject this quote"
        )
    
    quote.status = "rejected"
    db.commit()
    db.refresh(quote)
    
    return QuoteResponse.model_validate(quote)
