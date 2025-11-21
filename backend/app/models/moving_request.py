from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class MovingRequest(Base):
    __tablename__ = "moving_requests"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Détails du déménagement
    pickup_address = Column(String, nullable=False)
    pickup_city = Column(String, nullable=False)
    pickup_postal_code = Column(String, nullable=False)
    
    delivery_address = Column(String, nullable=False)
    delivery_city = Column(String, nullable=False)
    delivery_postal_code = Column(String, nullable=False)
    
    moving_date = Column(DateTime, nullable=False)
    description = Column(Text)
    
    # Détails des objets
    estimated_volume = Column(Float)  # en m³
    has_heavy_items = Column(Integer, default=0)  # Boolean
    has_fragile_items = Column(Integer, default=0)  # Boolean
    floor_pickup = Column(Integer, default=0)
    floor_delivery = Column(Integer, default=0)
    has_elevator_pickup = Column(Integer, default=0)  # Boolean
    has_elevator_delivery = Column(Integer, default=0)  # Boolean
    
    # Photos (URLs séparées par des virgules)
    photos = Column(Text)
    
    # Statut
    status = Column(String, default="open")  # open, quoted, accepted, completed, cancelled
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relations
    client = relationship("User", back_populates="moving_requests", foreign_keys=[client_id])
    quotes = relationship("Quote", back_populates="moving_request", cascade="all, delete-orphan")
