from fastapi import Request, status
from fastapi.responses import JSONResponse
from httpx import HTTPStatusError
from .logger import logger


async def provider_exception_handler(request: Request, exc: Exception):
    """
    Handle provider-specific exceptions and map them to standard gateway errors.
    """
    if isinstance(exc, HTTPStatusError):
        status_code = exc.response.status_code
        error_data = {}
        try:
            error_data = exc.response.json()
        except:
            pass
            
        # ElevenLabs & Google Specifics
        if status_code in [401, 402]:
            logger.warning(f"Provider billing issue: {error_data}")
            return JSONResponse(
                status_code=status.HTTP_402_PAYMENT_REQUIRED,
                content={
                    "error": "CREDITS_EXHAUSTED",
                    "message": "The audio provider credits are exhausted or API key is invalid.",
                    "provider_detail": error_data
                }
            )
            
        if status_code == 404:
            logger.warning(f"Voice not found or provider object missing: {error_data}")
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={
                    "error": "VOICE_NOT_FOUND",
                    "message": "The requested voice_id does not exist in this provider.",
                    "provider_detail": error_data
                }
            )

        if status_code == 422:
            logger.warning(f"Provider rejected request payload: {error_data}")
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error": "INVALID_PAYLOAD",
                    "message": "The text or parameters sent were rejected by the provider.",
                    "provider_detail": error_data
                }
            )

        if status_code >= 500:
            logger.error(f"Provider downstream error: {status_code} - {error_data}")
            return JSONResponse(
                status_code=status.HTTP_502_BAD_GATEWAY,
                content={
                    "error": "PROVIDER_UNAVAILABLE",
                    "message": "The audio provider is currently unavailable.",
                    "provider_status": status_code
                }
            )

    # General fallback
    logger.error(f"Unhandled exception in TTS API: {str(exc)}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "INTERNAL_ERROR",
            "message": "An unexpected error occurred in the audio service."
        }
    )
