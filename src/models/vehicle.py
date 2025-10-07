from sqlalchemy import Column, Integer, String, Float
from src.core.database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(String, unique=True, index=True, nullable=False)
    plate = Column(String, nullable=True)
    model = Column(String, nullable=True)
    capacity_t = Column(Float, nullable=True)
