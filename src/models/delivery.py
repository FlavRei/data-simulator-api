from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.core.database import Base

class Delivery(Base):
    __tablename__ = "deliveries"

    id = Column(String, primary_key=True, index=True)
    departure_time = Column(String, nullable=True)
    arrival_time = Column(String, nullable=True)
    quantity_tons = Column(String, nullable=True)
    distance_km = Column(String, nullable=True)
    delay_days = Column(String, nullable=True)
    status = Column(String, nullable=True)

    carrier_id = Column(String, ForeignKey("carriers.id"))
    vehicle_id = Column(String, ForeignKey("vehicles.id"))
    origin_id = Column(String, ForeignKey("warehouses.id"))
    destination_id = Column(String, ForeignKey("warehouses.id"))

    carrier = relationship("Carrier", back_populates="deliveries")
    vehicle = relationship("Vehicle", back_populates="deliveries")
    origin_warehouse = relationship("Warehouse", foreign_keys=[origin_id], back_populates="origin_deliveries")
    destination_warehouse = relationship("Warehouse", foreign_keys=[destination_id], back_populates="destination_deliveries")
