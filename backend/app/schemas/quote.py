from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class QuoteBase(BaseModel):
    moving_request_id: int
    price: float = Field(..., gt=0)
    estimated_duration: Optional[int] = None
    description: Optional[str] = None
    includes_packing: bool = False
    includes_unpacking: bool = False
    includes_insurance: bool = False

class QuoteCreate(QuoteBase):
    pass

class QuoteUpdate(BaseModel):
    price: Optional[float] = Field(None, gt=0)
    estimated_duration: Optional[int] = None
    description: Optional[str] = None
    includes_packing: Optional[bool] = None
    includes_unpacking: Optional[bool] = None
    includes_insurance: Optional[bool] = None

class QuoteResponse(QuoteBase):
    id: int
    mover_id: int
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
