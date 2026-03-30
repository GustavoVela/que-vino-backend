import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from main import app

client = TestClient(app)

valid_store_payload = {
    "name": "Test Wine Store",
    "type": "Fisica",
    "is_producer": False,
    "has_wine_club": True,
    "country_code": "MX",
    "country_name": "Mexico",
    "city_code": "CDMX",
    "city_name": "Ciudad de Mexico"
}

@patch("main.execute_query")
@patch("core.auth_middleware.verify_firebase_token")
def test_create_store(mock_verify, mock_execute):
    mock_verify.return_value = {"email": "test@test.com", "uid": "123"}
    # Mocking successful execution
    mock_execute.return_value = []
    
    response = client.post("/stores", json=valid_store_payload, headers={"Authorization": "Bearer fake_token"})
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == "Test Wine Store"

@patch("main.execute_query")
@patch("core.auth_middleware.verify_firebase_token")
def test_create_store_validation_error(mock_verify, mock_execute):
    mock_verify.return_value = {"email": "test@test.com", "uid": "123"}
    # Missing required 'name' and 'country_code'
    invalid_payload = {
        "is_producer": False,
        "has_wine_club": True
    }
    response = client.post("/stores", json=invalid_payload, headers={"Authorization": "Bearer fake_token"})
    assert response.status_code == 422

@patch("main.execute_query")
@patch("core.auth_middleware.verify_firebase_token")
def test_update_store(mock_verify, mock_execute):
    mock_verify.return_value = {"email": "test@test.com", "uid": "123"}
    
    # Mock execution returning a fake existing store row for the SELECT before UPDATE
    fake_row = {"name": "Test Store Old"}
    
    mock_execute.side_effect = [[fake_row], [], []]  # First call returns row, second executes update, third logs
    
    response = client.put("/stores/123e4567-e89b-12d3-a456-426614174000", json={"name": "New Name"}, headers={"Authorization": "Bearer fake_token"})
    assert response.status_code == 200
    assert response.json()["message"] == "Store updated successfully"

@patch("main.execute_query")
@patch("core.auth_middleware.verify_firebase_token")
def test_update_store_not_found(mock_verify, mock_execute):
    mock_verify.return_value = {"email": "test@test.com", "uid": "123"}
    # Return empty list to simulate store not found
    mock_execute.return_value = []
    
    response = client.put("/stores/invalid-id-1234", json={"name": "New Name"}, headers={"Authorization": "Bearer fake_token"})
    assert response.status_code == 404
