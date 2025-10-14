from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.core.database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(String, primary_key=True, index=True)
    registration_number = Column(String, nullable=True)
    type = Column(String, nullable=True)
    capacity_tons = Column(String, nullable=True)
    carrier_id = Column(String, ForeignKey("carriers.id"), nullable=False)

    carrier = relationship("Carrier", back_populates="vehicles")
    deliveries = relationship("Delivery", back_populates="vehicle")
