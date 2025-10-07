import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.core.config import settings

client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def set_api_key_env():
    # ensure API key check is satisfied
    settings.REQUIRE_API_KEY = False
    yield
    settings.REQUIRE_API_KEY = True

def test_simulate_and_list():
    # simulate 5 deliveries
    r = client.post("/deliveries/simulate?count=5")
    assert r.status_code == 200
    data = r.json()
    assert data["inserted"] == 5

    # list deliveries
    r = client.get("/deliveries")
    assert r.status_code == 200
    arr = r.json()
    assert isinstance(arr, list)
    assert len(arr) >= 5
