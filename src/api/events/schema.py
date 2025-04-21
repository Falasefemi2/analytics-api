from typing import List, Optional
from pydantic import BaseModel

class EventCreateSchema(BaseModel):
    page: str
    
class EventUpdateSchema(BaseModel):
    description: str
    
class EventSchema(BaseModel):
    id: int
    page: Optional[str] = None
    
class EventListSchema(BaseModel):
    results: List[EventSchema]
