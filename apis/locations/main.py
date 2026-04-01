from fastapi import FastAPI, Depends, Request, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from core.rate_limit import rate_limit_middleware
from starlette.middleware.base import BaseHTTPMiddleware
from core.auth_middleware import AuthMiddleware
from core.db import execute_query
from schemas.api_models import LocationCreate, LocationUpdate, LocationRead
import uuid
from datetime import datetime
import json
import unicodedata

"""
Microservicio de Gestión de Sucursales (Locations API) para Que Vino!.
Este servicio administra las ubicaciones físicas de la red de tiendas, 
permitiendo búsquedas geo-referenciadas y gestión de sucursales independientes.
"""

app = FastAPI(title="Que Vino Locations API")

# Configuración de CORS con exclusión manual de credenciales debido al uso de Bearer tokens
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:3000",
        "http://localhost:5173", # Vite default
        "https://quevino.mx",
        "https://www.quevino.mx",
        "https://id-preview--9ebf32fb-b85f-43d4-b440-af3007c90f34.lovable.app",
        "https://que-vino-admin.lovable.app",
        "https://9ebf32fb-b85f-43d4-b440-af3007c90f34.lovableproject.com"
    ],
    allow_credentials=False, 
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middlewares de control de acceso: Rate Limiting y Auth Middleware
app.add_middleware(BaseHTTPMiddleware, dispatch=rate_limit_middleware)
app.add_middleware(AuthMiddleware)

def log_transaction_sync(request: Request, db_type: str, parameters: dict, payload_before: dict = None, payload_after: dict = None):
    """
    Registra de forma síncrona cada evento de base de datos en locations_log.
    Constituye el rastro de auditoría mandatorio para operaciones administrativas.
    """
    user = getattr(request.state, "user", {})
    email = user.get("email")
    uid = user.get("uid")

    query = """
    INSERT INTO `src_api_transactions.locations_log`
    (transaction_id, performed_by_user_id, performed_by_email, transaction_api_type, 
     transaction_api_path, transaction_db_type, transaction_parameters, 
     payload_before, payload_after, event_timestamp, ingestion_timestamp)
    VALUES (@tid, @uid, @email, @api_type, @api_path, @db_type, @params, @before, @after, @ts, CURRENT_TIMESTAMP())
    """
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

def normalize_string(input_str: str) -> str:
    """
    Remueve diacríticos y normaliza el texto para búsquedas robustas.
    """
    if not input_str:
        return ""
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)]).lower()

@app.get("/locations", response_model=dict)
def list_locations(limit: int = Query(50, le=100), offset: int = Query(0, ge=0)):
    """
    Lista las sucursales del sistema de forma paginada.
    """
    query = "SELECT * FROM `src_database.locations` ORDER BY created_at DESC LIMIT @limit OFFSET @offset"
    params = [{"name": "limit", "type": "INT64", "value": limit}, {"name": "offset", "type": "INT64", "value": offset}]
    res = list(execute_query(query, params))
    return {"items": [dict(r) for r in res], "limit": limit, "offset": offset}

@app.get("/locations/search", response_model=dict)
def search_locations(term: str = Query(..., min_length=2), limit: int = Query(50, le=100), offset: int = Query(0, ge=0)):
    """
    Realiza una búsqueda de sucursales por ciudad o país.
    """
    norm_term = normalize_string(term)
    query = "SELECT * FROM `src_database.locations` WHERE LOWER(city_name) LIKE @term OR LOWER(country_name) LIKE @norm_term ORDER BY created_at DESC LIMIT @limit OFFSET @offset"
    params = [
        {"name": "term", "type": "STRING", "value": f"%{term.lower()}%"},
        {"name": "norm_term", "type": "STRING", "value": f"%{norm_term}%"},
        {"name": "limit", "type": "INT64", "value": limit},
        {"name": "offset", "type": "INT64", "value": offset}
    ]
    res = list(execute_query(query, params))
    return {"items": [dict(r) for r in res], "limit": limit, "offset": offset}

@app.post("/locations", status_code=201)
def create_location(location: LocationCreate, request: Request):
    """
    Crea un nuevo registro de ubicación física (sucursal).
    Asocia coordenadas geográficas y metadatos de ubicación.
    """
    loc_id = location.id if location.id else str(uuid.uuid4())
    loc_dict = location.model_dump()
    loc_dict["id"] = loc_id
    
    query = """
    INSERT INTO `src_database.locations`
    (id, country_code, country_name, state_code, state_name, city_code, city_name, latitude, longitude, created_at, updated_at)
    VALUES (@id, @country_code, @country_name, @state_code, @state_name, @city_code, @city_name, @latitude, @longitude, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP())
    """
    params = [
        {"name": "id", "type": "STRING", "value": loc_id},
        {"name": "country_code", "type": "STRING", "value": location.country_code},
        {"name": "country_name", "type": "STRING", "value": location.country_name},
        {"name": "state_code", "type": "STRING", "value": location.state_code},
        {"name": "state_name", "type": "STRING", "value": location.state_name},
        {"name": "city_code", "type": "STRING", "value": location.city_code},
        {"name": "city_name", "type": "STRING", "value": location.city_name},
        {"name": "latitude", "type": "FLOAT", "value": location.latitude},
        {"name": "longitude", "type": "FLOAT", "value": location.longitude}
    ]
    execute_query(query, params)
    log_transaction_sync(request, "INSERT", {"action": "create"}, payload_after=loc_dict)
    
    return {"id": loc_id, "city_name": location.city_name}

@app.put("/locations/{loc_id}")
def update_location(loc_id: str, location_update: LocationUpdate, request: Request):
    """
    Actualiza la información de una sucursal existente.
    """
    query_select = "SELECT * FROM `src_database.locations` WHERE id = @id LIMIT 1"
    res = list(execute_query(query_select, [{"name": "id", "type": "STRING", "value": loc_id}]))
    if not res:
        raise HTTPException(status_code=404, detail="Ubicación no encontrada")
        
    old_loc = dict(res[0])
    
    # Actualización simplificada a nivel de modelo demonstrativo
    query_update = "UPDATE `src_database.locations` SET city_name = @city_name, updated_at = CURRENT_TIMESTAMP() WHERE id = @id"
    params = [
        {"name": "id", "type": "STRING", "value": loc_id},
        {"name": "city_name", "type": "STRING", "value": location_update.city_name if location_update.city_name else old_loc["city_name"]}
    ]
    execute_query(query_update, params)
    
    new_loc = {**old_loc, "city_name": location_update.city_name}
    log_transaction_sync(request, "UPDATE", {"id": loc_id}, payload_before=old_loc, payload_after=new_loc)
    
    return {"message": "Ubicación actualizada exitosamente"}

@app.delete("/locations/{loc_id}")
def delete_location(loc_id: str, request: Request):
    """
    Elimina físicamente una sucursal de la base de datos de Que Vino.
    """
    query_select = "SELECT * FROM `src_database.locations` WHERE id = @id LIMIT 1"
    res = list(execute_query(query_select, [{"name": "id", "type": "STRING", "value": loc_id}]))
    if not res:
        raise HTTPException(status_code=404, detail="Ubicación no encontrada")
        
    old_loc = dict(res[0])
    query_delete = "DELETE FROM `src_database.locations` WHERE id = @id"
    execute_query(query_delete, [{"name": "id", "type": "STRING", "value": loc_id}])
    log_transaction_sync(request, "DELETE", {"id": loc_id}, payload_before=old_loc)
    return {"message": "Ubicación eliminada exitosamente"}
