from mcp.server.fastmcp import FastMCP
from pydantic import ValidationError
from schemas.api_models import LocationCreate, LocationUpdate
from main import create_location, update_location, delete_location, list_locations, search_locations
import re

"""
Servidor MCP para la Gestión de Sucursales (Que Vino Locations MCP).
Expone las capacidades de la Locations API como herramientas (Tools) 
para agentes de IA, permitiendo la administración geográfica de la red.
"""

mcp = FastMCP("QueVinoLocations")

# Clase auxiliar para simular peticiones HTTP desde el contexto de MCP
class MockRequest:
    def __init__(self, action: str, path: str):
        self.method = action
        self.url = type('URL', (), {'path': path})()
        # Identidad del agente para auditoría en el middleware de logs
        self.state = type('State', (), {'user': {'email': 'agent@mcp', 'uid': 'mcp-agent-001'}})()

def sanitize_input(value: str) -> str:
    """
    Sanitización de entradas para prevenir ataques de inyección SQL 
    en las herramientas consumidas por agentes de IA.
    """
    if value:
        # Validación de patrones prohibidos según constitución
        if re.search(r"(;|--|\bDROP\b|\bSELECT\b|\bINSERT\b|\bUPDATE\b)", value, re.IGNORECASE):
            raise ValueError("Entrada inválida. Se detectaron palabras clave de SQL bloqueadas.")
    return value

@mcp.tool()
def create_location_tool(country_code: str, country_name: str, city_code: str, city_name: str) -> str:
    """
    Crea una nueva ubicación física en el índice de Que Vino.
    
    Args:
        country_code (str): Código ISO del país.
        country_name (str): Nombre del país.
    """
    try:
        loc = LocationCreate(
            country_code=sanitize_input(country_code),
            country_name=sanitize_input(country_name),
            city_code=sanitize_input(city_code),
            city_name=sanitize_input(city_name)
        )
        req = MockRequest("POST", "/locations")
        res = create_location(loc, req)
        return f"Éxito: {res}"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def update_location_tool(loc_id: str, city_name: str) -> str:
    """
    Actualiza el nombre de la ciudad de una sucursal existente.
    
    Args:
        loc_id (str): ID de la sucursal.
        city_name (str): Nuevo nombre de la ciudad.
    """
    try:
        loc_update = LocationUpdate(city_name=sanitize_input(city_name))
        req = MockRequest("PUT", f"/locations/{loc_id}")
        res = update_location(sanitize_input(loc_id), loc_update, req)
        return f"Éxito: {res}"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def delete_location_tool(loc_id: str) -> str:
    """
    Elimina una sucursal del índice de Que Vino.
    
    Args:
        loc_id (str): ID de recurso de la sucursal.
    """
    try:
        req = MockRequest("DELETE", f"/locations/{loc_id}")
        res = delete_location(sanitize_input(loc_id), req)
        return f"Éxito: {res}"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def list_locations_tool(limit: int = 50, offset: int = 0) -> str:
    """
    Lista las sucursales de forma paginada para facilitar la navegación del agente.
    """
    try:
        max_limit = min(limit, 100)
        res = list_locations(limit=max_limit, offset=offset)
        return f"Resultados: {res}"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def search_locations_tool(term: str, limit: int = 50, offset: int = 0) -> str:
    """
    Busca sucursales por término (ciudad o país) utilizando normalización.
    """
    try:
        max_limit = min(limit, 100)
        safe_term = sanitize_input(term)
        res = search_locations(term=safe_term, limit=max_limit, offset=offset)
        return f"Resultados: {res}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()
