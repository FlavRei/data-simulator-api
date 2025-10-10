from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class DeliveryOut(BaseModel):
    delivery_id: str
    departure_time: datetime
    distance_km: float
    delay_min: Optional[int] = None
    status: str
    carrier_id: int
    vehicle_id: int
    origin_id: int
    destination_id: int

    model_config = ConfigDict(from_attributes=True)
