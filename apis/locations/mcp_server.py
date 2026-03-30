from mcp.server.fastmcp import FastMCP
from pydantic import ValidationError
from schemas.api_models import LocationCreate, LocationUpdate
from main import create_location, update_location, delete_location, list_locations, search_locations
import re

mcp = FastMCP("QueVinoLocations")

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
def create_location_tool(country_code: str, country_name: str, city_code: str, city_name: str) -> str:
    """Creates a new location in Que Vino index."""
    try:
        loc = LocationCreate(
            country_code=sanitize_input(country_code),
            country_name=sanitize_input(country_name),
            city_code=sanitize_input(city_code),
            city_name=sanitize_input(city_name)
        )
        req = MockRequest("POST", "/locations")
        res = create_location(loc, req)
        return f"Success: {res}"
    except Exception as e:
        return f"Failed: {str(e)}"

@mcp.tool()
def update_location_tool(loc_id: str, city_name: str) -> str:
    """Updates an existing location."""
    try:
        loc_update = LocationUpdate(city_name=sanitize_input(city_name))
        req = MockRequest("PUT", f"/locations/{loc_id}")
        res = update_location(sanitize_input(loc_id), loc_update, req)
        return f"Success: {res}"
    except Exception as e:
        return f"Failed: {str(e)}"

@mcp.tool()
def delete_location_tool(loc_id: str) -> str:
    """Deletes an existing location from Que Vino index."""
    try:
        req = MockRequest("DELETE", f"/locations/{loc_id}")
        res = delete_location(sanitize_input(loc_id), req)
        return f"Success: {res}"
    except Exception as e:
        return f"Failed: {str(e)}"

@mcp.tool()
def list_locations_tool(limit: int = 50, offset: int = 0) -> str:
    """List locations pagination."""
    try:
        max_limit = min(limit, 100)
        res = list_locations(limit=max_limit, offset=offset)
        return f"Results: {res}"
    except Exception as e:
        return f"Failed: {str(e)}"

@mcp.tool()
def search_locations_tool(term: str, limit: int = 50, offset: int = 0) -> str:
    """Search locations by normalized name, city or country."""
    try:
        max_limit = min(limit, 100)
        safe_term = sanitize_input(term)
        res = search_locations(term=safe_term, limit=max_limit, offset=offset)
        return f"Results: {res}"
    except Exception as e:
        return f"Failed: {str(e)}"

if __name__ == "__main__":
    mcp.run()
