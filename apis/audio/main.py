import time
import uuid
from datetime import datetime
from typing import Any, Callable

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.background import BackgroundTasks
from httpx import HTTPStatusError

from config import settings
from core.auth_middleware import AuthMiddleware
from core.db import bq_service
from core.logger import logger
from core.exceptions import provider_exception_handler
from schemas.bq_models import APITransactionBase
from services.audio_service import audio_service

# Módulo principal de la Audio Generation API (Que Vino!?).
# Implementado siguiendo la Constitución v1.5.1.

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)


# Manejadores de Excepciones Globales (Sección 5.175)
app.add_exception_handler(HTTPStatusError, provider_exception_handler)
app.add_exception_handler(Exception, provider_exception_handler)

# CORS
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

# Auth Middleware (Sección 4.150)
app.add_middleware(AuthMiddleware)


# Middleware de Auditoría de Transacciones API (Sección 6.192)
class APILoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable):
        transaction_id = str(uuid.uuid4())
        request.state.transaction_id = transaction_id
        start_time = time.time()

        # Captura del cuerpo solo en rutas críticas de generación
        request_body = None
        if request.method == "POST" and "/audio/generate" in request.url.path:
            try:
                body_bytes = await request.body()
                try:
                    import json
                    request_body = json.loads(body_bytes.decode())
                except Exception:
                    request_body = {"raw": body_bytes.decode()}
                
                async def receive():
                    return {"type": "http.request", "body": body_bytes}
                request._receive = receive
            except Exception:
                request_body = None

        response = await call_next(request)
        
        user_id = getattr(request.state, "user", {}).get("uid")
        bg_tasks = BackgroundTasks()
        
        if request.url.path not in ["/docs", "/openapi.json", "/health", "/"]:
            log_entry = APITransactionBase(
                transaction_id=transaction_id,
                performed_by_user_id=user_id,
                transaction_api_type=request.method,
                transaction_api_path=request.url.path,
                transaction_parameters=dict(request.query_params),
                payload_request=request_body,
                event_timestamp=datetime.utcnow()
            )
            bg_tasks.add_task(bq_service.log_api_transaction, log_entry)

        return response


app.add_middleware(APILoggingMiddleware)


@app.get("/health")
def health_check():
    return {"status": "ok", "service": settings.APP_NAME}


@app.get("/audio/providers/voices")
async def list_voices():
    """Listado unificado de voces disponibles con caché de 24h."""
    return await audio_service.get_all_voices()


@app.get("/audio/providers/models")
async def list_models():
    """Listado unificado de modelos de síntesis disponibles."""
    return await audio_service.get_all_models()


@app.post("/audio/generate")
async def generate_audio(
    payload: dict, 
    request: Request,
    bg_tasks: BackgroundTasks
):
    """
    Genera audio a partir de texto y lo entrega como stream binario.
    La auditoría en GCS y BigQuery se dispara en segundo plano.
    """
    text = payload.get("text")
    provider = payload.get("provider")
    voice_id = payload.get("voice_id")
    model_id = payload.get("model_id") or payload.get("model") # Accept both
    output_format = payload.get("output_format", "mp3")
    enrich_audio = payload.get("enrich_audio", False)

    if not all([text, provider, voice_id]):
        return Response(status_code=422, content="Faltan parámetros obligatorios: text, provider o voice_id")

    # 1. Orquestación de Síntesis y Enriquecimiento
    audio_bytes, metadata = await audio_service.generate_audio(
        text=text,
        provider_key=provider,
        voice_id=voice_id,
        model_id=model_id,
        output_format=output_format,
        enrich_audio=enrich_audio
    )

    # 2. Persistencia de Auditoría Asíncrona (Sección 6.192 / T023)
    user_id = getattr(request.state, "user", {}).get("uid", "anonymous")
    bg_tasks.add_task(
        audio_service.persist_audit_async,
        audio_bytes,
        metadata,
        provider,
        voice_id,
        user_id,
        request.state.transaction_id
    )

    # 3. Respuesta Binaria con Headers de Trazabilidad (Sección 5.176 / T022)
    media_type = "audio/mpeg" if output_format == "mp3" else "audio/wav"
    headers = {
        "X-Generation-ID": metadata["generation_id"],
        "X-Enrichment-Status": metadata["enrichment_status"]
    }
    
    return Response(
        content=audio_bytes, 
        media_type=media_type, 
        headers=headers,
        status_code=201
    )


@app.get("/")
def root():
    return {"message": f"Bienvenido a {settings.APP_NAME}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
