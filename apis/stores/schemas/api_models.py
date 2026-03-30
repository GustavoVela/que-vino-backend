from pydantic import BaseModel, Field
from typing import Optional, Dict

class StoreCreate(BaseModel):
    id: Optional[str] = None
    name: str = Field(..., max_length=50)
    type: Optional[str] = None
    digital_platform: Optional[str] = None
    is_producer: bool
    has_wine_club: bool
    representative_name: Optional[str] = None
    country_code: str = Field(..., max_length=2)
    country_name: str
    state_code: Optional[str] = None
    state_name: Optional[str] = None
    city_code: str
    city_name: str
    address: Optional[str] = None
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None
    website_url: Optional[str] = None
    social_media: Optional[Dict[str, str]] = None
    description: Optional[str] = None

class StoreUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=50)
    type: Optional[str] = None
    digital_platform: Optional[str] = None
    is_producer: Optional[bool] = None
    has_wine_club: Optional[bool] = None
    representative_name: Optional[str] = None
    country_code: Optional[str] = Field(None, max_length=2)
    country_name: Optional[str] = None
    state_code: Optional[str] = None
    state_name: Optional[str] = None
    city_code: Optional[str] = None
    city_name: Optional[str] = None
    address: Optional[str] = None
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None
    website_url: Optional[str] = None
    social_media: Optional[Dict[str, str]] = None
    description: Optional[str] = None

class StoreRead(StoreCreate):
    id: str
    created_at: str
    updated_at: str
    
    class Config:
        from_attributes = True
