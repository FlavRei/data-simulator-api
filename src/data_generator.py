from faker import Faker
import random

fake = Faker()

def generate_deliveries(n: int = 10):
    deliveries = []
    for _ in range(n):
        delivery = {
            "delivery_id": fake.uuid4(),
            "origin": fake.city(),
            "destination": fake.city(),
            "departure_time": fake.date_time_between(start_date="-7d", end_date="now").isoformat(),
            "distance_km": round(random.uniform(10, 1500), 2),
            "delay_min": random.choice([0, 0, 0, 15, 30, 60, 120]),
            "status": random.choice(["on_time", "delayed", "cancelled"]),
            "carrier": random.choice(["DHL", "FedEx", "UPS", "Chronopost", "Mondial Relay"]),
        }
        deliveries.append(delivery)
    return deliveries
