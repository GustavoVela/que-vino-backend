from pydantic import BaseModel, Field
from typing import Optional, Dict

class LocationCreate(BaseModel):
    id: Optional[str] = None
    country_code: str = Field(..., max_length=2)
    country_name: str
    state_code: Optional[str] = None
    state_name: Optional[str] = None
    city_code: str
    city_name: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class LocationUpdate(BaseModel):
    country_code: Optional[str] = Field(None, max_length=2)
    country_name: Optional[str] = None
    state_code: Optional[str] = None
    state_name: Optional[str] = None
    city_code: Optional[str] = None
    city_name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class LocationRead(LocationCreate):
    id: str
    created_at: str
    updated_at: str
    
    class Config:
        from_attributes = True
