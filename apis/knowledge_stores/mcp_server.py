from mcp.server.fastmcp import FastMCP
from main import app
from schemas.api_models import SyncRequest
from services.sync_service import sync_bucket_to_gemini
from core.gemini_client import list_stores, list_documents
import uuid

# Initialize FastMCP
mcp = FastMCP("Knowledge Stores MCP")

@mcp.tool()
async def list_knowledge_stores() -> list:
    """Lista todos los repositorios de conocimiento disponibles en Gemini."""
    return list_stores()

@mcp.tool()
async def list_knowledge_documents(store_id: str) -> list:
    """Lista los documentos dentro de un repositorio de conocimiento."""
    return list_documents(store_id)

@mcp.tool()
async def sync_knowledge_bucket(bucket_name: str) -> dict:
    """
    Sincroniza un bucket de GCS con un repositorio de Gemini.
    Este proceso es incremental (mirroring).
    """
    # Note: In MCP context, we might not have a real user_id from JWT
    # We use a system indicator
    transaction_id = str(uuid.uuid4())
    return await sync_bucket_to_gemini(bucket_name, "MCP_AGENT", transaction_id)

if __name__ == "__main__":
    mcp.run()
