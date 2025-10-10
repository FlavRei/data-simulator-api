from pydantic import BaseModel, ConfigDict

class WarehouseOut(BaseModel):
    name: str
    city: str
    country: str
    capacity: str

    model_config = ConfigDict(from_attributes=True)
