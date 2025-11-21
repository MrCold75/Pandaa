from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List

class MovingRequestBase(BaseModel):
    pickup_address: str
    pickup_city: str
    pickup_postal_code: str
    delivery_address: str
    delivery_city: str
    delivery_postal_code: str
    moving_date: datetime
    description: Optional[str] = None
    estimated_volume: Optional[float] = None
    has_heavy_items: bool = False
    has_fragile_items: bool = False
    floor_pickup: int = 0
    floor_delivery: int = 0
    has_elevator_pickup: bool = False
    has_elevator_delivery: bool = False

class MovingRequestCreate(MovingRequestBase):
    photos: Optional[List[str]] = []

class MovingRequestUpdate(BaseModel):
    pickup_address: Optional[str] = None
    pickup_city: Optional[str] = None
    pickup_postal_code: Optional[str] = None
    delivery_address: Optional[str] = None
    delivery_city: Optional[str] = None
    delivery_postal_code: Optional[str] = None
    moving_date: Optional[datetime] = None
    description: Optional[str] = None
    estimated_volume: Optional[float] = None
    has_heavy_items: Optional[bool] = None
    has_fragile_items: Optional[bool] = None
    floor_pickup: Optional[int] = None
    floor_delivery: Optional[int] = None
    has_elevator_pickup: Optional[bool] = None
    has_elevator_delivery: Optional[bool] = None
    photos: Optional[List[str]] = None
    status: Optional[str] = None

class MovingRequestResponse(MovingRequestBase):
    id: int
    client_id: int
    status: str
    created_at: datetime
    updated_at: datetime
    photos: Optional[List[str]] = []

    class Config:
        from_attributes = True
