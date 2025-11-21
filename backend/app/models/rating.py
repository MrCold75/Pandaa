from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    moving_request_id = Column(Integer, ForeignKey("moving_requests.id"), nullable=False)
    mover_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    client_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Notation
    rating = Column(Integer, nullable=False)  # 1-5
    comment = Column(Text)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relations
    mover = relationship("User", back_populates="ratings_received", foreign_keys=[mover_id])
    client = relationship("User", back_populates="ratings_given", foreign_keys=[client_id])
