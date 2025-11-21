from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class RatingBase(BaseModel):
    moving_request_id: int
    mover_id: int
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = None

class RatingCreate(RatingBase):
    pass

class RatingResponse(RatingBase):
    id: int
    client_id: int
    created_at: datetime

    class Config:
        from_attributes = True
