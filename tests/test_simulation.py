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

def test_simulation():
    r = client.post("/simulate")
    assert r.status_code == 200
    data = r.json()
    assert data["carriers"] == 5
    assert data["vehicles"] == 15
    assert data["warehouses"] == 10
    assert data["deliveries"] == 50
