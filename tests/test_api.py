from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_get_deliveries():
    response = client.get("/deliveries?count=5")
    assert response.status_code == 200
    data = response.json()
    assert "deliveries" in data
    assert len(data["deliveries"]) == 5
