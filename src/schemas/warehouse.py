from pydantic import BaseModel, ConfigDict
from typing import Optional

class WarehouseOut(BaseModel):
    name: str
    city: Optional[str]
    country: Optional[str]
    capacity: Optional[int]

    model_config = ConfigDict(from_attributes=True)
