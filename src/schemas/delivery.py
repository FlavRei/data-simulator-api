from pydantic import BaseModel, ConfigDict

class DeliveryOut(BaseModel):
    delivery_id: str
    departure_time: str
    distance_km: str
    delay_min: str
    status: str
    carrier_id: int
    vehicle_id: int
    origin_id: int
    destination_id: int

    model_config = ConfigDict(from_attributes=True)
