from fastapi import FastAPI, Request, HTTPException, BackgroundTasks, Query
from fastapi.middleware.cors import CORSMiddleware
from core.auth_middleware import AuthMiddleware
from config import settings
from schemas.api_models import SyncRequest
from services.sync_service import sync_bucket_to_gemini
from core.gemini_client import list_stores, list_documents, delete_store, delete_document
from core.db import log_api_transaction_async
import logging
import uuid

app = FastAPI(
    title="Que Vino Knowledge Stores API",
    description="API para la gestión de repositorios de conocimiento RAG (Gemini + GCS)",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:3000",
        "http://localhost:5173",
        "https://quevino.mx",
        "https://www.quevino.mx",
        "https://que-vino-admin.lovable.app",
        "https://9ebf32fb-b85f-43d4-b440-af3007c90f34.lovableproject.com",
        "https://id-preview--9ebf32fb-b85f-43d4-b440-af3007c90f34.lovable.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error_code": "INTERNAL_SERVER_ERROR",
            "message": "An unexpected error occurred",
            "detail": str(exc)
        }
    )

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error_code": "HTTP_ERROR",
            "message": exc.detail if isinstance(exc.detail, str) else exc.detail.get("message", "Request failed"),
            "detail": exc.detail if not isinstance(exc.detail, str) else None
        }
    )

app.add_middleware(AuthMiddleware)

@app.get("/health")
async def health_check():
    """Endpoint de salud para Cloud Run."""
    return {"status": "ok", "environment": settings.environment}

@app.get("/knowledge-stores")
async def get_stores(request: Request, background_tasks: BackgroundTasks):
    """Lista todos los stores de Gemini."""
    user_id = getattr(request.state, "user", {}).get("uid", "SYSTEM")
    try:
        stores = list_stores()
        background_tasks.add_task(log_api_transaction_async, "ALL", "ALL", user_id, "LIST_STORES")
        return stores
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/knowledge-stores/{store_id}/files")
async def get_store_files(request: Request, store_id: str, background_tasks: BackgroundTasks):
    """Lista todos los archivos de un store específico."""
    user_id = getattr(request.state, "user", {}).get("uid", "SYSTEM")
    try:
        # El store_id de la URL es el ID corto. Gemini requiere el nombre completo.
        full_store_name = store_id if store_id.startswith("fileSearchStores/") else f"fileSearchStores/{store_id}"
        files = list_documents(full_store_name)
        background_tasks.add_task(log_api_transaction_async, "UNKNOWN", store_id, user_id, "LIST_FILES")
        return files
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/knowledge-stores/sync")
async def sync_store(request: Request, body: SyncRequest):
    """
    Sincroniza un bucket de GCS con Gemini.
    """
    user_id = getattr(request.state, "user", {}).get("uid", "SYSTEM")
    transaction_id = str(uuid.uuid4())
    
    try:
        summary = await sync_bucket_to_gemini(
            body.bucket_name, 
            user_id, 
            transaction_id, 
            prefix=body.prefix, 
            store_name=body.store_name
        )
        return {
            "status": "completed",
            "transaction_id": transaction_id,
            "summary": summary
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"error_code": "SYNC_FAILED", "message": str(e)}
        )

@app.delete("/knowledge-stores/{store_id}", status_code=204)
async def remove_store(
    request: Request,
    store_id: str,
    background_tasks: BackgroundTasks,
    force: bool = Query(default=False, description="Si es true, elimina todos los documentos del store antes de borrarlo (cascade delete).")
):
    """
    Elimina un store de Gemini.

    Si el store contiene documentos, Gemini rechaza la operación con FAILED_PRECONDITION.
    Usa ?force=true para eliminar en cascada todos los documentos primero y luego el store.

    HTTP 409 Conflict: El store no está vacío. Usa ?force=true o elimina los archivos primero.
    HTTP 404 Not Found: El store no existe.
    HTTP 204 No Content: Eliminado exitosamente.
    """
    user_id = getattr(request.state, "user", {}).get("uid", "SYSTEM")
    full_store_name = store_id if store_id.startswith("fileSearchStores/") else f"fileSearchStores/{store_id}"

    try:
        # Gemini soporta force=True de forma nativa en DeleteFileSearchStoreConfig.
        # Esto elimina documentos y chunks en cascada sin necesidad de un loop manual.
        logging.info(f"[remove_store] Eliminando store {full_store_name} (force={force})")
        delete_store(full_store_name, force=force)
        background_tasks.add_task(log_api_transaction_async, "UNKNOWN", store_id, user_id, "DELETE_STORE", "DELETE")

    except HTTPException:
        raise
    except Exception as e:
        err_str = str(e)
        # Gemini retorna FAILED_PRECONDITION cuando el store no está vacío
        if "FAILED_PRECONDITION" in err_str or "Cannot delete non-empty" in err_str:
            raise HTTPException(
                status_code=409,
                detail={
                    "error_code": "STORE_NOT_EMPTY",
                    "message": "El store no se puede eliminar porque contiene documentos indexados.",
                    "detail": "Usa ?force=true para eliminar en cascada todos los documentos primero, o elimínalos individualmente con DELETE /knowledge-stores/{store_id}/files/{file_id}."
                }
            )
        # Gemini retorna NOT_FOUND cuando el store no existe
        if "NOT_FOUND" in err_str or "404" in err_str:
            raise HTTPException(
                status_code=404,
                detail={"error_code": "STORE_NOT_FOUND", "message": f"El store '{store_id}' no existe.", "detail": None}
            )
        logging.error(f"[remove_store] Error inesperado al eliminar store {store_id}: {err_str}")
        raise HTTPException(
            status_code=500,
            detail={"error_code": "DELETE_STORE_FAILED", "message": err_str, "detail": None}
        )

@app.delete("/knowledge-stores/{store_id}/files/{file_id}", status_code=204)
async def remove_file(request: Request, store_id: str, file_id: str, background_tasks: BackgroundTasks):
    """
    Elimina un archivo específico de un store.

    El file_id debe ser el ID corto del documento (sin el prefijo del store).
    Se recomienda obtenerlo del campo 'id' de GET /knowledge-stores/{store_id}/files
    y pasar únicamente la última parte del resource name.
    """
    user_id = getattr(request.state, "user", {}).get("uid", "SYSTEM")
    try:
        # El resource name completo del documento es el campo 'id' retornado por list_documents.
        # Si el caller pasa el ID corto, reconstruimos el nombre completo.
        if file_id.startswith("fileSearchStores/"):
            doc_name = file_id
        else:
            doc_name = f"fileSearchStores/{store_id}/documents/{file_id}"
        delete_document(doc_name)
        background_tasks.add_task(log_api_transaction_async, "UNKNOWN", store_id, user_id, "DELETE_FILE", "DELETE")
    except Exception as e:
        err_str = str(e)
        if "NOT_FOUND" in err_str or "404" in err_str:
            raise HTTPException(
                status_code=404,
                detail={"error_code": "FILE_NOT_FOUND", "message": f"El archivo '{file_id}' no existe en el store '{store_id}'.", "detail": None}
            )
        logging.error(f"[remove_file] Error inesperado al eliminar archivo {file_id}: {err_str}")
        raise HTTPException(
            status_code=500,
            detail={"error_code": "DELETE_FILE_FAILED", "message": err_str, "detail": None}
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
