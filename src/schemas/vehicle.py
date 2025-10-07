from pydantic import BaseModel, ConfigDict
from typing import Optional

class VehicleOut(BaseModel):
    vehicle_id: str
    plate: Optional[str]
    model: Optional[str]
    capacity_t: Optional[float]

    model_config = ConfigDict(from_attributes=True)
