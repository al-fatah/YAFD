import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"YAFD" in response.data

def test_place_order(client):
    response = client.post("/order", data={"item": "Burger", "consumer": "Alice"})
    assert response.status_code == 200
    assert b"Burger" in response.data

def test_get_orders(client):
    response = client.get("/orders")
    assert response.status_code == 200
    assert isinstance(response.json, list)
