from pydantic import BaseModel
from datetime import datetime

class AppointmentCreateRequest(BaseModel):
    user_id: int
    title: str
    description: str | None = None
    date_time: datetime

class AppointmentResponse(BaseModel):
    id: int
    user_id: int
    title: str
    description: str | None = None
    date_time: datetime
    status: str

class AppointmentUpdateRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    date_time: datetime | None = None
    status: str | None = None

