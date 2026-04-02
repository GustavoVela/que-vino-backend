from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional, Any, Dict
import uuid


class APITransactionBase(BaseModel):
    transaction_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    performed_by_user_id: Optional[str] = None
    transaction_api_type: str  # GET, POST
    transaction_api_path: str
    transaction_parameters: Optional[Dict[str, Any]] = None
    payload_request: Optional[Any] = None
    payload_response: Optional[Any] = None
    event_timestamp: datetime = Field(default_factory=datetime.utcnow)
    ingestion_timestamp: Optional[datetime] = None

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "transaction_api_type": "POST",
                "transaction_api_path": "/audio/generate"
            }
        }
    )


class AudioGenerationLog(BaseModel):
    generation_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    api_transaction_id: str
    performed_by_user_id: str
    provider: str  # ELEVENLABS, GOOGLE
    voice_id: str
    is_enriched: bool = False
    text_input: str
    text_processed: Optional[str] = None
    status: str  # SUCCESS, ERROR_OUT_OF_CREDITS, ERROR_PROVIDER_DOWN
    event_timestamp: datetime = Field(default_factory=datetime.utcnow)
    ingestion_timestamp: Optional[datetime] = None

    model_config = ConfigDict(
        from_attributes=True
    )
