import pytest
import unicodedata
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from main import app

client = TestClient(app)

def normalize_string(input_str: str) -> str:
    """Remueve acentos y convierte a minusculas."""
    if not input_str:
        return ""
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)]).lower()

def test_normalize_string():
    assert normalize_string("viñedo") == "vinedo"
    assert normalize_string("Río Negro") == "rio negro"
    assert normalize_string("Mendoza") == "mendoza"

@patch("main.execute_query")
@patch("core.auth_middleware.verify_firebase_token")
def test_search_pagination_limit(mock_verify, mock_execute):
    mock_verify.return_value = {"email": "test@test.com", "uid": "123"}
    
    # Pruebas con limite > 100 deben fallar
    response = client.get("/stores/search?name=vinedo&limit=101", headers={"Authorization": "Bearer fake_token"})
    assert response.status_code == 422
    
@patch("main.execute_query")
@patch("core.auth_middleware.verify_firebase_token")
def test_search_success(mock_verify, mock_execute):
    mock_verify.return_value = {"email": "test@test.com", "uid": "123"}
    
    mock_row = {"id": "1", "name": "Viñedo del Mar"}
    mock_execute.return_value = [mock_row]
    response = client.get("/stores/search?name=viñedo&limit=50", headers={"Authorization": "Bearer fake_token"})
    assert response.status_code == 200
    assert response.json()["items"][0]["name"] == "Viñedo del Mar"

@patch("main.execute_query")
@patch("core.auth_middleware.verify_firebase_token")
def test_list_stores_success(mock_verify, mock_execute):
    mock_verify.return_value = {"email": "test@test.com", "uid": "123"}
    
    mock_row = {"id": "1", "name": "Test Store"}
    mock_execute.return_value = [mock_row]
    response = client.get("/stores?limit=50", headers={"Authorization": "Bearer fake_token"})
    assert response.status_code == 200
    assert response.json()["items"][0]["name"] == "Test Store"
