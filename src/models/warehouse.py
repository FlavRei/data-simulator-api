from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.core.database import Base

class Warehouse(Base):
    __tablename__ = "warehouses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    city = Column(String, nullable=True)
    country = Column(String, nullable=True)
    capacity = Column(String, nullable=True)

    origin_deliveries = relationship("Delivery", back_populates="origin_warehouse", foreign_keys="Delivery.origin_id")
    destination_deliveries = relationship("Delivery", back_populates="destination_warehouse", foreign_keys="Delivery.destination_id")
