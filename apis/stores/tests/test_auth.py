import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)

def test_missing_auth_header():
    response = client.get("/protected")
    assert response.status_code == 401
    assert "Authorization header missing" in response.text

@patch("core.auth_middleware.verify_firebase_token")
def test_invalid_auth_token(mock_verify):
    mock_verify.side_effect = Exception("Invalid token")
    response = client.get("/protected", headers={"Authorization": "Bearer invalid_token"})
    assert response.status_code == 401
    assert "Token expired or invalid" in response.text
