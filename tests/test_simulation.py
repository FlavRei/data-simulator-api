import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.core.config import settings

client = TestClient(app)

@pytest.fixture(autouse=True)
def disable_api_key():
    settings.REQUIRE_API_KEY = False
    yield
    settings.REQUIRE_API_KEY = True

def test_simulation_without_db():
    """Test la simulation complète uniquement à travers l'API."""
    r = client.post("/simulate")
    assert r.status_code == 200
    data = r.json()
    assert data["carriers"] == 5
    assert data["vehicles"] == 15
    assert data["warehouses"] == 10
    assert data["deliveries"] == 50

    carriers = data.get("carrier_data", [])
    vehicles = data.get("vehicle_data", [])
    deliveries = data.get("delivery_data", [])
    warehouses = data.get("warehouse_data", [])

    # Vérifie que les relations sont cohérentes dans le JSON
    carrier_ids = {c["id"] for c in carriers}
    vehicle_ids = {v["id"] for v in vehicles}
    warehouse_ids = {w["id"] for w in warehouses}

    # Chaque véhicule doit référencer un carrier existant
    for v in vehicles:
        assert v["carrier_id"] in carrier_ids

    # Chaque livraison doit référencer un véhicule, un carrier et deux entrepôts distincts
    for d in deliveries:
        assert d["vehicle_id"] in vehicle_ids
        assert d["carrier_id"] in carrier_ids
        assert d["origin_id"] in warehouse_ids
        assert d["destination_id"] in warehouse_ids
        assert d["origin_id"] != d["destination_id"]
