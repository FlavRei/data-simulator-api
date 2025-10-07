from sqlalchemy import Column, Integer, String, Float, DateTime
from src.core.database import Base
import datetime

class Delivery(Base):
    __tablename__ = "deliveries"

    id = Column(Integer, primary_key=True, index=True)
    delivery_id = Column(String, unique=True, index=True)
    origin = Column(String)
    destination = Column(String)
    departure_time = Column(DateTime, default=datetime.datetime.now)
    distance_km = Column(Float)
    delay_min = Column(Integer, nullable=True)
    status = Column(String)
    carrier = Column(String)
