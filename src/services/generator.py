from faker import Faker
import random
from datetime import datetime, timedelta
from src.services.corruption import corrupt_value

fake = Faker()
FREQ_CARRIERS = ["DHL", "FedEx", "UPS", "Chronopost", "Mondial Relay"]

def _random_departure():
    # random datetime in last 14 days or next 2 days
    start = datetime.now() - timedelta(days=14)
    end = datetime.now() + timedelta(days=2)
    return fake.date_time_between(start_date=start, end_date=end)

def generate_delivery():
    """Génère une livraison, en retournant un dict prêt pour l'ORM."""
    # simulated realistic distance and occasional missing/invalid
    distance = round(random.uniform(5, 1500), 2)
    # generate delay with heavier probability for on_time
    status = random.choices(["on_time", "delayed", "cancelled", ""], weights=[0.7, 0.22, 0.05, 0.03])[0]
    delay = None
    if status == "delayed":
        delay = random.choice([5, 10, 15, 30, 60, 120, 240])
    elif status == "on_time":
        delay = 0 if random.random() > 0.95 else None

    carrier = random.choice(FREQ_CARRIERS)
    origin = fake.city()
    destination = fake.city()

    delivery = {
        "delivery_id": fake.uuid4(),
        "origin": corrupt_value(origin),
        "destination": corrupt_value(destination),
        "departure_time": _random_departure(),
        "distance_km": distance if random.random() > 0.02 else None,  # 2% missing
        "delay_min": delay,
        "status": corrupt_value(status),
        "carrier": corrupt_value(carrier),
    }
    return delivery

def generate_deliveries_batch(n: int = 10):
    return [generate_delivery() for _ in range(n)]
