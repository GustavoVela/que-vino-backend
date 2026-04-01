from pydantic import BaseModel
from typing import Optional

class SyncRequest(BaseModel):
    bucket_name: str
    prefix: Optional[str] = None
    store_name: Optional[str] = None
