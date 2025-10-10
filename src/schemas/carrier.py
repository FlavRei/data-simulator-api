from pydantic import BaseModel, ConfigDict

class CarrierOut(BaseModel):
    name: str
    country: str
    rating: int

    model_config = ConfigDict(from_attributes=True)
