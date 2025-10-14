from faker import Faker
import random
from src.models.carrier import Carrier
from src.models.delivery import Delivery
from src.models.vehicle import Vehicle
from src.models.warehouse import Warehouse
from src.services.corruption import corrupt_value

fake = Faker()

def generate_carriers(n=5):
    carriers = []
    for _ in range(n):
        c = Carrier(
            id=fake.uuid4(),
            name=corrupt_value(random.choice(["DHL", "FedEx", "UPS", "Chronopost", "Mondial Relay"])),
            country=corrupt_value(fake.country()),
            rating=corrupt_value(round(random.uniform(1, 5), 0))
        )
        carriers.append(c)
    return carriers

def generate_vehicles(carriers, n=15):
    vehicles = []
    for _ in range(n):
        carrier = random.choice(carriers) if carriers else None
        v = Vehicle(
            id=fake.uuid4(),
            registration_number=corrupt_value(fake.license_plate()),
            type=corrupt_value(random.choice(["truck", "van", "trailer", None, ""])),
            capacity_tons=corrupt_value(random.randint(2, 40)),
            carrier=carrier
        )
        vehicles.append(v)
    return vehicles

def generate_warehouses(n=10):
    warehouses = []
    for _ in range(n):
        w = Warehouse(
            id=fake.uuid4(),
            city=corrupt_value(fake.city()),
            country=corrupt_value(fake.country()),
            capacity=corrupt_value(random.randint(100, 1000))
        )
        warehouses.append(w)
    return warehouses

def generate_deliveries(vehicles, warehouses, n=50):
    deliveries = []
    for _ in range(n):
        vehicle = random.choice(vehicles) if vehicles else None
        carrier = vehicle.carrier if vehicle else None
        origin, destination = random.sample(warehouses, 2) if len(warehouses) >= 2 else (None, None)

        d = Delivery(
            id=fake.uuid4(),
            departure_time=corrupt_value(fake.date_time_between(start_date='-30d', end_date='now').isoformat()),
            quantity_tons=corrupt_value(random.randint(1, 40)),
            distance_km=corrupt_value(round(random.uniform(5, 20000), 2)),
            delay_min=corrupt_value(random.choice([None, 0, 15, 30, 45, 60, 90, 120, "unknown"])),
            status=corrupt_value(random.choice(["on_time", "delayed", "cancelled", "", None, 404])),
            carrier=carrier,
            vehicle=vehicle,
            origin_warehouse=origin,
            destination_warehouse=destination
        )
        deliveries.append(d)
    return deliveries
