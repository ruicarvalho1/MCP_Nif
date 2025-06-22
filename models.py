from pydantic import BaseModel
from typing import Optional, List

class Company(BaseModel):
    nif: str
    name: str
    city: str
    activity: str
    status: str
    address: str
    phone: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    cae: List[str] = []
    racius: Optional[str] = None
    portugalio: Optional[str] = None