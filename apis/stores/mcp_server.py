from mcp.server.fastmcp import FastMCP
from pydantic import ValidationError
from schemas.api_models import StoreCreate, StoreUpdate
from main import create_store, update_store, delete_store
from fastapi import Request
import re

"""
Servidor MCP para la Gestión de Tiendas (Que Vino Stores MCP).
Expone las capacidades de la Stores API como herramientas (Tools) 
para que sean consumidas por agentes inteligentes de forma segura y estructurada.
"""

mcp = FastMCP("QueVinoStores")

# Simulación de objeto Request para invocar la lógica de negocio de FastAPI desde MCP
# Permite compartir la lógica de validación y logs sin duplicar código.
class MockRequest:
    def __init__(self, action: str, path: str):
        self.method = action
        self.url = type('URL', (), {'path': path})()
        # Identidad del agente para trazabilidad en logs
        self.state = type('State', (), {'user': {'email': 'agent@mcp', 'uid': 'mcp-agent-001'}})()

def sanitize_input(value: str) -> str:
    """
    Protección básica contra inyección de SQL para entradas de texto provenientes de MCP.
    Cumple con el mandato de seguridad de la constitución del proyecto.
    """
    if value:
        # Bloqueo de palabras clave de SQL y comentarios
        if re.search(r"(;|--|\bDROP\b|\bSELECT\b|\bINSERT\b|\bUPDATE\b)", value, re.IGNORECASE):
            raise ValueError("Caracteres inválidos detectados. Palabras clave de SQL están bloqueadas.")
    return value

@mcp.tool()
def create_store_tool(name: str, is_producer: bool, has_wine_club: bool, country_code: str, country_name: str, city_code: str, city_name: str) -> str:
    """
    Crea una nueva tienda en el índice de Que Vino.
    
    Args:
        name (str): Nombre de la tienda.
        is_producer (bool): Si la tienda es productora de vino.
        has_wine_club (bool): Si cuenta con club de vinos.
    """
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
        return f"Éxito: {res}"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def update_store_tool(store_id: str, name: str) -> str:
    """
    Actualiza el nombre de una tienda existente.
    
    Args:
        store_id (str): ID único de la tienda.
        name (str): Nuevo nombre de la tienda.
    """
    try:
        store_update = StoreUpdate(name=sanitize_input(name))
        req = MockRequest("PUT", f"/stores/{store_id}")
        res = update_store(sanitize_input(store_id), store_update, req)
        return f"Éxito: {res}"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def delete_store_tool(store_id: str) -> str:
    """
    Elimina una tienda existente del índice de Que Vino.
    
    Args:
        store_id (str): ID de recurso de la tienda a eliminar.
    """
    try:
        req = MockRequest("DELETE", f"/stores/{store_id}")
        res = delete_store(sanitize_input(store_id), req)
        return f"Éxito: {res}"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def list_stores_tool(limit: int = 50, offset: int = 0) -> str:
    """
    Lista las tiendas de forma paginada para exploración de agentes.
    """
    from main import list_stores
    try:
        max_limit = min(limit, 100) # Prevención de OOM
        res = list_stores(limit=max_limit, offset=offset)
        return f"Resultados: {res}"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def search_stores_tool(name: str, limit: int = 50, offset: int = 0) -> str:
    """
    Busca tiendas utilizando el nombre normalizado. Útil para agentes que 
    reciben peticiones de búsqueda de usuarios.
    """
    from main import search_stores
    try:
        max_limit = min(limit, 100)
        safe_name = sanitize_input(name)
        res = search_stores(name=safe_name, limit=max_limit, offset=offset)
        return f"Resultados: {res}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()
