from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class DeliveryOut(BaseModel):
    delivery_id: str
    origin: Optional[str]
    destination: Optional[str]
    departure_time: Optional[datetime]
    distance_km: Optional[float]
    delay_min: Optional[int]
    status: Optional[str]
    carrier: Optional[str]

    model_config = ConfigDict(from_attributes=True)
