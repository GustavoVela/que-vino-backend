import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)

valid_loc_payload = {
    "country_code": "FR",
    "country_name": "France",
    "city_code": "BXD",
    "city_name": "Bordeaux"
}

@patch("main.execute_query")
@patch("core.auth_middleware.verify_firebase_token")
def test_create_location(mock_verify, mock_execute):
    mock_verify.return_value = {"email": "test@test.com", "uid": "123"}
    mock_execute.return_value = []
    
    response = client.post("/locations", json=valid_loc_payload, headers={"Authorization": "Bearer fake"})
    assert response.status_code == 201
    assert response.json()["city_name"] == "Bordeaux"

@patch("main.execute_query")
@patch("core.auth_middleware.verify_firebase_token")
def test_update_location(mock_verify, mock_execute):
    mock_verify.return_value = {"email": "test@test.com", "uid": "123"}
    fake_row = {"city_name": "Old"}
    mock_execute.side_effect = [[fake_row], [], []]
    
    response = client.put("/locations/123", json={"city_name": "New"}, headers={"Authorization": "Bearer fake"})
    assert response.status_code == 200

@patch("main.execute_query")
@patch("core.auth_middleware.verify_firebase_token")
def test_search_location(mock_verify, mock_execute):
    mock_verify.return_value = {"email": "test@test.com", "uid": "123"}
    mock_execute.return_value = [{"id": "1", "city_name": "Bordeaux"}]
    
    response = client.get("/locations/search?term=Bordeaux&limit=101", headers={"Authorization": "Bearer fake"})
    assert response.status_code == 422 # Limit enforcement

    response = client.get("/locations/search?term=Bordeaux&limit=50", headers={"Authorization": "Bearer fake"})
    assert response.status_code == 200
    assert len(response.json()["items"]) == 1
