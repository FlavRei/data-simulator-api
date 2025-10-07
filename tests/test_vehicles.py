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

def test_list_vehicles():
    r = client.get("/vehicles")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    # les véhicules peuvent être vides si DB n'a pas encore de seed
