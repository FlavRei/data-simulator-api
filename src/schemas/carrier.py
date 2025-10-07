from pydantic import BaseModel, ConfigDict

class CarrierOut(BaseModel):
    name: str
    code: str

    model_config = ConfigDict(from_attributes=True)
