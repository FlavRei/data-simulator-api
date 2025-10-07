from pydantic import BaseModel, ConfigDict
from typing import Optional

class WarehouseOut(BaseModel):
    name: str
    city: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]

    model_config = ConfigDict(from_attributes=True)
