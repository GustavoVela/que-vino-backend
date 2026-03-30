import logging
from typing import Dict, Any
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.background import BackgroundTasks
import firebase_admin
from firebase_admin import auth
from .db import execute_query
import uuid
from datetime import datetime

# Initialize Firebase App if not already initialized
try:
    firebase_admin.get_app()
except ValueError:
    firebase_admin.initialize_app()

def verify_firebase_token(id_token: str) -> Dict[str, Any]:
    """Valida el token JWT con Firebase."""
    return auth.verify_id_token(id_token)

def log_authentication(email: str, status: str, user_id: str = None, error_message: str = None):
    """Inserta log de forma asíncrona."""
    query = """
    INSERT INTO `src_api_transactions.authentication_log`
    (transaction_id, user_id, email, status, error_message, event_timestamp, ingestion_timestamp)
    VALUES (@tid, @uid, @email, @status, @error, @ts, CURRENT_TIMESTAMP())
    """
    params = [
        {"name": "tid", "type": "STRING", "value": str(uuid.uuid4())},
        {"name": "uid", "type": "STRING", "value": user_id},
        {"name": "email", "type": "STRING", "value": email},
        {"name": "status", "type": "STRING", "value": status},
        {"name": "error", "type": "STRING", "value": error_message},
        {"name": "ts", "type": "TIMESTAMP", "value": datetime.utcnow().isoformat() + "Z"}
    ]
    try:
        execute_query(query, params)
    except Exception as e:
        logging.error(f"Error asincrono guardando auth log: {e}")

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path in ["/docs", "/openapi.json", "/redoc", "/favicon.ico"] or request.method == "OPTIONS":
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
            bg_tasks.add_task(log_authentication, email=decoded_token.get("email", "UNKNOWN"), status="SUCCESS", user_id=decoded_token.get("uid"))
            
        except auth.ExpiredIdTokenError as e:
            bg_tasks.add_task(log_authentication, email="UNKNOWN", status="FAILED", error_message="Expired token")
            return JSONResponse(
                status_code=401,
                content={"error_code": "TOKEN_EXPIRED", "message": "Token expired", "detail": str(e)},
                background=bg_tasks
            )
        except auth.RevokedIdTokenError as e:
            bg_tasks.add_task(log_authentication, email="UNKNOWN", status="FAILED", error_message="Revoked token")
            return JSONResponse(
                status_code=401,
                content={"error_code": "TOKEN_REVOKED", "message": "Token revoked", "detail": str(e)},
                background=bg_tasks
            )
        except auth.InvalidIdTokenError as e:
            bg_tasks.add_task(log_authentication, email="UNKNOWN", status="FAILED", error_message="Invalid token structure")
            return JSONResponse(
                status_code=401,
                content={"error_code": "INVALID_TOKEN", "message": "Token invalid", "detail": str(e)},
                background=bg_tasks
            )
        except Exception as e:
            bg_tasks.add_task(log_authentication, email="UNKNOWN", status="FAILED", error_message=f"Internal Auth Error: {str(e)}")
            return JSONResponse(
                status_code=500,
                content={"error_code": "AUTH_INTERNAL_ERROR", "message": "Internal error during authentication", "detail": str(e)},
                background=bg_tasks
            )
        except Exception as e:
            bg_tasks.add_task(log_authentication, email="UNKNOWN", status="FAILED", error_message=f"Internal Auth Error: {str(e)}")
            return JSONResponse(
                status_code=500,
                content={"error_code": "AUTH_INTERNAL_ERROR", "message": "Internal error during authentication", "detail": str(e)},
                background=bg_tasks
            )

        response = await call_next(request)
        response.background = bg_tasks
        return response
