from fastapi import APIRouter
from .schema import EventSchema, EventListSchema, EventCreateSchema, EventUpdateSchema
import os

router = APIRouter()

@router.get("/")
def read_events() -> EventListSchema:
    return {
        "results": [
            {"id": 1},
            {"id": 2},
            {"id": 3}
        ]
    }
    
    
@router.post("/")
def create_events(payload:EventCreateSchema) -> EventSchema:
    print(os.environ.get("DATABASE_URL"))
    print(payload.page)
    data = payload.model_dump()
    return {"id": 123, **data}
    
@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    return {"id": event_id }

@router.put("/{event_id}")
def update_event(event_id: int, payload:EventUpdateSchema) -> EventSchema:
    print(payload.description)
    data = payload.model_dump()
    return {"id": event_id, **data}