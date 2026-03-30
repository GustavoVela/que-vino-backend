import pytest
from mcp_server import sanitize_input

def test_sanitize_input_valid():
    assert sanitize_input("Bordeaux") == "Bordeaux"

def test_sanitize_input_sql_injection_semicolon():
    with pytest.raises(ValueError, match="Invalid characters in string"):
        sanitize_input("London; DROP TABLE locations;")
