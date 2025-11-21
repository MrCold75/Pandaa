from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    phone: Optional[str] = None
    is_mover: bool = False

class UserCreate(UserBase):
    password: str = Field(..., min_length=6)
    company_name: Optional[str] = None
    description: Optional[str] = None
    service_area: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    phone: Optional[str] = None
    company_name: Optional[str] = None
    description: Optional[str] = None
    service_area: Optional[str] = None

class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    company_name: Optional[str] = None
    description: Optional[str] = None
    service_area: Optional[str] = None
    average_rating: float
    total_ratings: int

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse
