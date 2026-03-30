from mcp.server.fastmcp import FastMCP
from pydantic import ValidationError
from schemas.api_models import StoreCreate, StoreUpdate
from main import create_store, update_store, delete_store
from fastapi import Request
import re

mcp = FastMCP("QueVinoStores")

# Mock request for helper invocation mapping to REST logic 
# In a real scenario, business logic should be abstracted from view, but to share logic here:
class MockRequest:
    def __init__(self, action: str, path: str):
        self.method = action
        self.url = type('URL', (), {'path': path})()
        self.state = type('State', (), {'user': {'email': 'agent@mcp', 'uid': 'mcp-agent-001'}})()

def sanitize_input(value: str) -> str:
    """Basic SQL injection protection for MCP input strings per constitution."""
    if value:
        # Avoid semicolons, drop, select, insert, quotes
        if re.search(r"(;|--|\bDROP\b|\bSELECT\b|\bINSERT\b|\bUPDATE\b)", value, re.IGNORECASE):
            raise ValueError("Invalid characters in string. SQL keywords are blocked.")
    return value

@mcp.tool()
def create_store_tool(name: str, is_producer: bool, has_wine_club: bool, country_code: str, country_name: str, city_code: str, city_name: str) -> str:
    """Creates a new store in Que Vino index."""
    try:
        store = StoreCreate(
            name=sanitize_input(name),
            is_producer=is_producer,
            has_wine_club=has_wine_club,
            country_code=sanitize_input(country_code),
            country_name=sanitize_input(country_name),
            city_code=sanitize_input(city_code),
            city_name=sanitize_input(city_name)
        )
        req = MockRequest("POST", "/stores")
        res = create_store(store, req)
        return f"Success: {res}"
    except Exception as e:
        return f"Failed: {str(e)}"

@mcp.tool()
def update_store_tool(store_id: str, name: str) -> str:
    """Updates an existing store name."""
    try:
        store_update = StoreUpdate(name=sanitize_input(name))
        req = MockRequest("PUT", f"/stores/{store_id}")
        res = update_store(sanitize_input(store_id), store_update, req)
        return f"Success: {res}"
    except Exception as e:
        return f"Failed: {str(e)}"

@mcp.tool()
def delete_store_tool(store_id: str) -> str:
    """Deletes an existing store from Que Vino index."""
    try:
        req = MockRequest("DELETE", f"/stores/{store_id}")
        res = delete_store(sanitize_input(store_id), req)
        return f"Success: {res}"
    except Exception as e:
        return f"Failed: {str(e)}"

@mcp.tool()
def list_stores_tool(limit: int = 50, offset: int = 0) -> str:
    """List stores pagination."""
    from main import list_stores
    try:
        max_limit = min(limit, 100) # Enforce limit OOM
        res = list_stores(limit=max_limit, offset=offset)
        return f"Results: {res}"
    except Exception as e:
        return f"Failed: {str(e)}"

@mcp.tool()
def search_stores_tool(name: str, limit: int = 50, offset: int = 0) -> str:
    """Search stores by normalized name."""
    from main import search_stores
    try:
        max_limit = min(limit, 100)
        safe_name = sanitize_input(name)
        res = search_stores(name=safe_name, limit=max_limit, offset=offset)
        return f"Results: {res}"
    except Exception as e:
        return f"Failed: {str(e)}"

if __name__ == "__main__":
    mcp.run()
