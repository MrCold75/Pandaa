from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True, index=True)
    moving_request_id = Column(Integer, ForeignKey("moving_requests.id"), nullable=False)
    mover_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Détails du devis
    price = Column(Float, nullable=False)
    estimated_duration = Column(Integer)  # en heures
    description = Column(Text)
    
    # Détails supplémentaires
    includes_packing = Column(Integer, default=0)  # Boolean
    includes_unpacking = Column(Integer, default=0)  # Boolean
    includes_insurance = Column(Integer, default=0)  # Boolean
    
    # Statut
    status = Column(String, default="pending")  # pending, accepted, rejected
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relations
    moving_request = relationship("MovingRequest", back_populates="quotes", foreign_keys=[moving_request_id])
    mover = relationship("User", back_populates="quotes", foreign_keys=[mover_id])
