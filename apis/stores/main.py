from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from core.rate_limit import rate_limit_middleware
from starlette.middleware.base import BaseHTTPMiddleware
from core.auth_middleware import AuthMiddleware
from core.db import execute_query
from schemas.api_models import StoreCreate, StoreUpdate, StoreRead
import uuid
from datetime import datetime
import json
import unicodedata
from fastapi import Query

"""
Microservicio de Gestión de Tiendas (Stores API) para Que Vino!.
Este servicio centraliza la administración de marcas, catálogos y entidades legales
de la red de tiendas de vino, integrándose directamente con Google BigQuery.
"""

app = FastAPI(title="Que Vino Stores API")

# Configuración de CORS para permitir la integración con frontends administrativos y públicos
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
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middlewares de seguridad: Limitación de tasa y Autenticación Firebase/Google
app.add_middleware(BaseHTTPMiddleware, dispatch=rate_limit_middleware)
app.add_middleware(AuthMiddleware)

def log_transaction_sync(request: Request, db_type: str, parameters: dict, payload_before: dict = None, payload_after: dict = None):
    """
    Registra de forma síncrona cada operación de base de datos en la tabla de auditoría stores_log.
    
    Args:
        request (Request): Objeto de petición FastAPI para extraer contexto de usuario.
        db_type (str): Tipo de operación (INSERT, UPDATE, DELETE).
        parameters (dict): Parámetros de la consulta realizada.
        payload_before (dict, optional): Estado del registro antes de la operación.
        payload_after (dict, optional): Estado del registro después de la operación.
    """
    user = getattr(request.state, "user", {})
    email = user.get("email")
    uid = user.get("uid")

    query = """
    INSERT INTO `src_api_transactions.stores_log`
    (transaction_id, performed_by_user_id, performed_by_email, transaction_api_type, 
     transaction_api_path, transaction_db_type, transaction_parameters, 
     payload_before, payload_after, event_timestamp, ingestion_timestamp)
    VALUES (@tid, @uid, @email, @api_type, @api_path, @db_type, @params, @before, @after, @ts, CURRENT_TIMESTAMP())
    """
    
    # Serialización a JSON string para compatibilidad con parámetros de BigQuery
    params = [
        {"name": "tid", "type": "STRING", "value": str(uuid.uuid4())},
        {"name": "uid", "type": "STRING", "value": uid},
        {"name": "email", "type": "STRING", "value": email},
        {"name": "api_type", "type": "STRING", "value": request.method},
        {"name": "api_path", "type": "STRING", "value": request.url.path},
        {"name": "db_type", "type": "STRING", "value": db_type},
        {"name": "params", "type": "JSON", "value": json.dumps(parameters, default=str)},
        {"name": "before", "type": "JSON", "value": json.dumps(payload_before, default=str) if payload_before else None},
        {"name": "after", "type": "JSON", "value": json.dumps(payload_after, default=str) if payload_after else None},
        {"name": "ts", "type": "TIMESTAMP", "value": datetime.utcnow().isoformat() + "Z"}
    ]
    execute_query(query, params)

@app.get("/protected")
def protected_route():
    """Ruta de prueba para verificar la correcta validación del middleware de autenticación."""
    return {"message": "Success"}

def normalize_string(input_str: str) -> str:
    """
    Normaliza una cadena de texto eliminando acentos y convirtiéndola a minúsculas
    para facilitar búsquedas de texto precisas en BigQuery.
    """
    if not input_str:
        return ""
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)]).lower()

@app.get("/stores", response_model=dict)
def list_stores(limit: int = Query(50, le=100), offset: int = Query(0, ge=0)):
    """
    Obtiene un listado paginado de todas las tiendas registradas.
    
    Args:
        limit (int): Cantidad máxima de registros a retornar (máx 100).
        offset (int): Cantidad de registros a omitir para la paginación.
    """
    query = "SELECT * FROM `src_database.stores` ORDER BY created_at DESC LIMIT @limit OFFSET @offset"
    params = [
        {"name": "limit", "type": "INT64", "value": limit},
        {"name": "offset", "type": "INT64", "value": offset}
    ]
    res = list(execute_query(query, params))
    return {"items": [dict(r) for r in res], "limit": limit, "offset": offset}

@app.get("/stores/search", response_model=dict)
def search_stores(name: str = Query(..., min_length=2), limit: int = Query(50, le=100), offset: int = Query(0, ge=0)):
    """
    Busca tiendas por nombre utilizando coincidencia parcial y normalización de texto.
    
    Args:
        name (str): Término de búsqueda (mínimo 2 caracteres).
    """
    norm_name = normalize_string(name)
    query = "SELECT * FROM `src_database.stores` WHERE LOWER(name) LIKE @name OR LOWER(name) LIKE @norm_name ORDER BY created_at DESC LIMIT @limit OFFSET @offset"
    params = [
        {"name": "name", "type": "STRING", "value": f"%{name.lower()}%"},
        {"name": "norm_name", "type": "STRING", "value": f"%{norm_name}%"},
        {"name": "limit", "type": "INT64", "value": limit},
        {"name": "offset", "type": "INT64", "value": offset}
    ]
    res = list(execute_query(query, params))
    return {"items": [dict(r) for r in res], "limit": limit, "offset": offset}

@app.post("/stores", status_code=201)
def create_store(store: StoreCreate, request: Request):
    """
    Crea una nueva tienda en el ecosistema.
    Si no se proporciona un ID, se genera un UUID-v4 de forma automática.
    """
    store_id = store.id if store.id else str(uuid.uuid4())
    store_dict = store.model_dump()
    store_dict["id"] = store_id
    
    query = """
    INSERT INTO `src_database.stores`
    (id, name, type, digital_platform, is_producer, has_wine_club, representative_name, country_code, country_name, city_code, city_name, address, created_at, updated_at)
    VALUES (@id, @name, @type, @digital_platform, @is_producer, @has_wine_club, @representative_name, @country_code, @country_name, @city_code, @city_name, @address, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP())
    """
    params = [
        {"name": "id", "type": "STRING", "value": store_id},
        {"name": "name", "type": "STRING", "value": store.name},
        {"name": "type", "type": "STRING", "value": store.type},
        {"name": "digital_platform", "type": "STRING", "value": store.digital_platform},
        {"name": "is_producer", "type": "BOOLEAN", "value": store.is_producer},
        {"name": "has_wine_club", "type": "BOOLEAN", "value": store.has_wine_club},
        {"name": "representative_name", "type": "STRING", "value": store.representative_name},
        {"name": "country_code", "type": "STRING", "value": store.country_code},
        {"name": "country_name", "type": "STRING", "value": store.country_name},
        {"name": "city_code", "type": "STRING", "value": store.city_code},
        {"name": "city_name", "type": "STRING", "value": store.city_name},
        {"name": "address", "type": "STRING", "value": store.address}
    ]
    
    execute_query(query, params)
    # Auditoría síncrona obligatoria según constitución
    log_transaction_sync(request, "INSERT", {"action": "create"}, payload_after=store_dict)
    
    return {"id": store_id, "name": store.name}


@app.put("/stores/{store_id}")
def update_store(store_id: str, store_update: StoreUpdate, request: Request):
    """
    Actualiza los datos de una tienda existente identificada por su ID.
    Realiza una búsqueda previa para garantizar la integridad y obtener el estado 'before' para auditoría.
    """
    query_select = "SELECT * FROM `src_database.stores` WHERE id = @id LIMIT 1"
    res = list(execute_query(query_select, [{"name": "id", "type": "STRING", "value": store_id}]))
    
    if not res:
        raise HTTPException(status_code=404, detail="Tienda no encontrada")
        
    old_store = dict(res[0])
    
    # Lógica de actualización dinámica (actualmente simplificada al campo name)
    query_update = "UPDATE `src_database.stores` SET name = @name, updated_at = CURRENT_TIMESTAMP() WHERE id = @id"
    params = [
        {"name": "id", "type": "STRING", "value": store_id},
        {"name": "name", "type": "STRING", "value": store_update.name if store_update.name else old_store["name"]}
    ]
    
    execute_query(query_update, params)
    
    new_store = {**old_store, "name": store_update.name} 
    
    log_transaction_sync(request, "UPDATE", {"id": store_id}, payload_before=old_store, payload_after=new_store)
    
    return {"message": "Tienda actualizada exitosamente"}

@app.delete("/stores/{store_id}")
def delete_store(store_id: str, request: Request):
    """
    Elimina permanentemente una tienda del catálogo.
    """
    query_select = "SELECT * FROM `src_database.stores` WHERE id = @id LIMIT 1"
    res = list(execute_query(query_select, [{"name": "id", "type": "STRING", "value": store_id}]))
    
    if not res:
        raise HTTPException(status_code=404, detail="Tienda no encontrada")
        
    old_store = dict(res[0])
    
    query_delete = "DELETE FROM `src_database.stores` WHERE id = @id"
    execute_query(query_delete, [{"name": "id", "type": "STRING", "value": store_id}])
    
    log_transaction_sync(request, "DELETE", {"id": store_id}, payload_before=old_store)
    
    return {"message": "Tienda eliminada exitosamente"}
