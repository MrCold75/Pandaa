from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    phone = Column(String)
    is_mover = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Profil déménageur
    company_name = Column(String)
    description = Column(String)
    service_area = Column(String)
    average_rating = Column(Float, default=0.0)
    total_ratings = Column(Integer, default=0)
    
    # Relations
    moving_requests = relationship("MovingRequest", back_populates="client", foreign_keys="MovingRequest.client_id")
    quotes = relationship("Quote", back_populates="mover", foreign_keys="Quote.mover_id")
    ratings_received = relationship("Rating", back_populates="mover", foreign_keys="Rating.mover_id")
    ratings_given = relationship("Rating", back_populates="client", foreign_keys="Rating.client_id")
