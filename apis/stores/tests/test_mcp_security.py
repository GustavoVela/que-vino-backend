import pytest
from mcp_server import sanitize_input

def test_sanitize_input_valid():
    assert sanitize_input("Mi Tiendita") == "Mi Tiendita"
    assert sanitize_input("Vinedo Valle Sagrado") == "Vinedo Valle Sagrado"
    assert sanitize_input("") == ""

def test_sanitize_input_sql_injection_semicolon():
    with pytest.raises(ValueError, match="Invalid characters in string"):
        sanitize_input("Tienda; DROP TABLE stores;")

def test_sanitize_input_sql_injection_comment():
    with pytest.raises(ValueError, match="Invalid characters in string"):
        sanitize_input("Tienda -- admin")

def test_sanitize_input_sql_injection_keywords():
    with pytest.raises(ValueError, match="Invalid characters in string"):
        sanitize_input("Tienda select * from users")
        
    with pytest.raises(ValueError, match="Invalid characters in string"):
        sanitize_input("UPDATE stores SET name='hack'")

def test_sanitize_input_case_insensitivity():
    with pytest.raises(ValueError, match="Invalid characters in string"):
        sanitize_input("DrOp TABLE stores")
