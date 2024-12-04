from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_temperature():
    response = client.get("/temperature/next-10-days")
    assert response.status_code == 200
    data = response.json()
    assert "location" in data
    assert "predictions" in data
    assert len(data["predictions"]) > 0
