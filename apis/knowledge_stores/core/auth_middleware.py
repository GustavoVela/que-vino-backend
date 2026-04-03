import logging
from typing import Dict, Any, Optional
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.background import BackgroundTasks
import firebase_admin
from firebase_admin import auth
import uuid
from datetime import datetime

from config import settings
from .db import execute_query, log_event_async

# Initialize Firebase App
try:
    firebase_admin.get_app()
except ValueError:
    firebase_admin.initialize_app()

def verify_firebase_token(id_token: str) -> Dict[str, Any]:
    """Valida el token JWT con Firebase."""
    return auth.verify_id_token(id_token)

def log_authentication(email: str, status: str, user_id: str = None, error_message: str = None):
    """Encapsula el log de autenticación para BigQuery."""
    row = {
        "transaction_id": str(uuid.uuid4()),
        "user_id": user_id,
        "email": email,
        "status": status,
        "error_message": error_message,
        "event_timestamp": datetime.utcnow().isoformat() + "Z"
    }
    log_event_async(settings.bq_dataset_transactions, settings.table_auth_log, row)

def upsert_user_bq(decoded_token: Dict[str, Any]):
    """Realiza el Upsert del perfil del usuario en BigQuery."""
    uid = decoded_token.get("uid")
    email = decoded_token.get("email")
    display_name = decoded_token.get("name", email.split('@')[0] if email else "Unknown")
    photo_url = decoded_token.get("picture")
    phone_number = decoded_token.get("phone_number")
    provider_id = decoded_token.get("firebase", {}).get("sign_in_provider")
    email_verified = decoded_token.get("email_verified", False)
    
    now = datetime.utcnow().isoformat() + "Z"
    
    # Merge/Upsert pattern for BQ
    query = f"""
    MERGE `{settings.project_id}.{settings.bq_dataset_database}.{settings.table_users}` T
    USING (SELECT @uid as id) S
    ON T.id = S.id
    WHEN MATCHED THEN
      UPDATE SET 
        email = @email, 
        display_name = @name, 
        photo_url = @photo, 
        phone_number = @phone, 
        provider_id = @provider, 
        email_verified = @verified,
        updated_at = @now
    WHEN NOT MATCHED THEN
      INSERT (id, email, display_name, photo_url, phone_number, provider_id, email_verified, created_at, updated_at)
      VALUES (@uid, @email, @name, @photo, @phone, @provider, @verified, @now, @now)
    """
    
    params = [
        {"name": "uid", "type": "STRING", "value": uid},
        {"name": "email", "type": "STRING", "value": email},
        {"name": "name", "type": "STRING", "value": display_name},
        {"name": "photo", "type": "STRING", "value": photo_url},
        {"name": "phone", "type": "STRING", "value": phone_number},
        {"name": "provider", "type": "STRING", "value": provider_id},
        {"name": "verified", "type": "BOOL", "value": email_verified},
        {"name": "now", "type": "TIMESTAMP", "value": now}
    ]
    
    try:
        execute_query(query, params)
    except Exception as e:
        logging.error(f"Error upserting user {uid}: {str(e)}")

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Public endpoints and health checks
        if request.url.path in ["/docs", "/openapi.json", "/redoc", "/health"] or request.method == "OPTIONS":
            return await call_next(request)

        auth_header = request.headers.get("Authorization")
        bg_tasks = BackgroundTasks()

        if not auth_header or not auth_header.startswith("Bearer "):
            bg_tasks.add_task(log_authentication, email="UNKNOWN", status="FAILED", error_message="Authorization header missing")
            return JSONResponse(
                status_code=401,
                content={"error_code": "UNAUTHORIZED", "message": "Authorization header missing", "detail": "Add Bearer token"},
                background=bg_tasks
            )

        token = auth_header.split(" ")[1]
        try:
            decoded_token = verify_firebase_token(token)
            request.state.user = decoded_token
            
            # Async logging and profile sync
            bg_tasks.add_task(log_authentication, email=decoded_token.get("email", "UNKNOWN"), status="SUCCESS", user_id=decoded_token.get("uid"))
            bg_tasks.add_task(upsert_user_bq, decoded_token)
            
        except Exception as e:
            error_code = "INVALID_TOKEN"
            msg = str(e)
            bg_tasks.add_task(log_authentication, email="UNKNOWN", status="FAILED", error_message=msg)
            return JSONResponse(
                status_code=401,
                content={"error_code": error_code, "message": "Token authentication failed", "detail": msg},
                background=bg_tasks
            )

        response = await call_next(request)
        response.background = bg_tasks
        return response
