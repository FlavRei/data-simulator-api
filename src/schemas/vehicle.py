from pydantic import BaseModel, ConfigDict

class VehicleOut(BaseModel):
    registration_number: str
    type: str
    capacity_tons: str
    carrier_id: int

    model_config = ConfigDict(from_attributes=True)
