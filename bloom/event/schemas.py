from pydantic import BaseModel
from datetime import datetime


class CreateEventRequest(BaseModel):
    event_name: str
    event_location: str
    event_start: datetime
    event_end: datetime


class EventBaseResponse(BaseModel):
    event_id: int
    name: str
    location: str
    event_start: datetime
    event_end: datetime


class EventResponse(EventBaseResponse):
    class Config:
        orm_mode = True
