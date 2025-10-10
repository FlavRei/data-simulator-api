from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.core.database import Base

class Carrier(Base):
    __tablename__ = "carriers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    country = Column(String, nullable=True)
    rating = Column(String, nullable=True)

    vehicles = relationship("Vehicle", back_populates="carrier")
