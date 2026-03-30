import time
from fastapi import Request, HTTPException
from typing import Dict

# Very simple in-memory rate limiting for demonstration/stateless Cloud Run nodes
# Limits to 100 requests per minute per IP
RATE_LIMIT = 100
TIME_WINDOW = 60.0

clients: Dict[str, list] = {}

async def rate_limit_middleware(request: Request, call_next):
    """
    Middleware que asegura un máximo de 100 req/minuto por cliente (IP).
    Lanza 429 Too Many Requests en formato estandarizado si se supera.
    """
    client_ip = request.client.host if request.client else "unknown"
    current_time = time.time()
    
    if client_ip not in clients:
        clients[client_ip] = []
        
    # Limpiamos requests viejos
    clients[client_ip] = [timestamp for timestamp in clients[client_ip] if current_time - timestamp < TIME_WINDOW]
    
    if len(clients[client_ip]) >= RATE_LIMIT:
        from fastapi.responses import JSONResponse
        return JSONResponse(
            status_code=429,
            content={
                "error_code": "RATE_LIMIT_EXCEEDED",
                "message": f"Too many requests. Limit is {RATE_LIMIT} per minute.",
                "detail": "Please try again later."
            }
        )
    
    clients[client_ip].append(current_time)
    response = await call_next(request)
    return response
