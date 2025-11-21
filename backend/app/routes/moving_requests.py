from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models.user import User
from ..models.moving_request import MovingRequest
from ..schemas.moving_request import MovingRequestCreate, MovingRequestUpdate, MovingRequestResponse
from ..utils.dependencies import get_current_user

router = APIRouter(prefix="/api/moving-requests", tags=["Moving Requests"])

@router.post("", response_model=MovingRequestResponse, status_code=status.HTTP_201_CREATED)
def create_moving_request(
    request_data: MovingRequestCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Créer une nouvelle demande de déménagement"""
    photos_str = ",".join(request_data.photos) if request_data.photos else ""
    
    new_request = MovingRequest(
        client_id=current_user.id,
        pickup_address=request_data.pickup_address,
        pickup_city=request_data.pickup_city,
        pickup_postal_code=request_data.pickup_postal_code,
        delivery_address=request_data.delivery_address,
        delivery_city=request_data.delivery_city,
        delivery_postal_code=request_data.delivery_postal_code,
        moving_date=request_data.moving_date,
        description=request_data.description,
        estimated_volume=request_data.estimated_volume,
        has_heavy_items=1 if request_data.has_heavy_items else 0,
        has_fragile_items=1 if request_data.has_fragile_items else 0,
        floor_pickup=request_data.floor_pickup,
        floor_delivery=request_data.floor_delivery,
        has_elevator_pickup=1 if request_data.has_elevator_pickup else 0,
        has_elevator_delivery=1 if request_data.has_elevator_delivery else 0,
        photos=photos_str
    )
    
    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    
    response = MovingRequestResponse.model_validate(new_request)
    response.photos = new_request.photos.split(",") if new_request.photos else []
    return response

@router.get("", response_model=List[MovingRequestResponse])
def list_moving_requests(
    status: str = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Lister les demandes de déménagement"""
    query = db.query(MovingRequest)
    
    if not current_user.is_mover:
        # Les clients voient seulement leurs propres demandes
        query = query.filter(MovingRequest.client_id == current_user.id)
    
    if status:
        query = query.filter(MovingRequest.status == status)
    
    requests = query.order_by(MovingRequest.created_at.desc()).all()
    
    results = []
    for req in requests:
        response = MovingRequestResponse.model_validate(req)
        response.photos = req.photos.split(",") if req.photos else []
        results.append(response)
    
    return results

@router.get("/{request_id}", response_model=MovingRequestResponse)
def get_moving_request(
    request_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Obtenir les détails d'une demande de déménagement"""
    moving_request = db.query(MovingRequest).filter(MovingRequest.id == request_id).first()
    
    if not moving_request:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Moving request not found"
        )
    
    # Vérifier les permissions
    if not current_user.is_mover and moving_request.client_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to view this request"
        )
    
    response = MovingRequestResponse.model_validate(moving_request)
    response.photos = moving_request.photos.split(",") if moving_request.photos else []
    return response

@router.put("/{request_id}", response_model=MovingRequestResponse)
def update_moving_request(
    request_id: int,
    request_data: MovingRequestUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Mettre à jour une demande de déménagement"""
    moving_request = db.query(MovingRequest).filter(MovingRequest.id == request_id).first()
    
    if not moving_request:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Moving request not found"
        )
    
    # Vérifier que c'est le client qui possède la demande
    if moving_request.client_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this request"
        )
    
    update_data = request_data.model_dump(exclude_unset=True)
    
    # Gérer les photos
    if "photos" in update_data:
        update_data["photos"] = ",".join(update_data["photos"]) if update_data["photos"] else ""
    
    # Gérer les booléens
    for field in ["has_heavy_items", "has_fragile_items", "has_elevator_pickup", "has_elevator_delivery"]:
        if field in update_data:
            update_data[field] = 1 if update_data[field] else 0
    
    for field, value in update_data.items():
        setattr(moving_request, field, value)
    
    db.commit()
    db.refresh(moving_request)
    
    response = MovingRequestResponse.model_validate(moving_request)
    response.photos = moving_request.photos.split(",") if moving_request.photos else []
    return response

@router.delete("/{request_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_moving_request(
    request_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Supprimer une demande de déménagement"""
    moving_request = db.query(MovingRequest).filter(MovingRequest.id == request_id).first()
    
    if not moving_request:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Moving request not found"
        )
    
    # Vérifier que c'est le client qui possède la demande
    if moving_request.client_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this request"
        )
    
    db.delete(moving_request)
    db.commit()
    
    return None
