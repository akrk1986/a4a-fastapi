"""Testing code for A4A REST API calls"""
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_get_all():
    response = client.get("/api/players")
    assert response.status_code == 200


def test_get_nonexistent_item():
    response = client.get("/api/players/fubar")
    assert response.status_code == 404
    assert response.json() == {"detail": "Error: Player ID 'fubar' does not exist in the players database"}


def test_nonexistent_path():
    response = client.get("/api/fubar")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
