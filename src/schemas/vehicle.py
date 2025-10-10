from pydantic import BaseModel, ConfigDict
from typing import Optional

class VehicleOut(BaseModel):
    registration_number: str
    type: str
    capacity_tons: int
    carrier_id: Optional[int]

    model_config = ConfigDict(from_attributes=True)
