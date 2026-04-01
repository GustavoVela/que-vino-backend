import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check_public():
    """Verifica que el endpoint de salud sea público."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_auth_middleware_blocking():
    """Verifica que el middleware bloquee peticiones sin token."""
    response = client.get("/knowledge-stores")
    assert response.status_code == 401
    # Note: JSON response contains error_code according to our implementation
    assert response.json()["error_code"] == "UNAUTHORIZED"
