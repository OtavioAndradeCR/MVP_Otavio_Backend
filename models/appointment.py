from pydantic import BaseModel
from datetime import datetime

class Appointment(BaseModel):
    id: int | None = None
    user_id: int
    title: str
    description: str | None = None
    date_time: datetime
    status: str = "agendado"  # agendado, confirmado, cancelado

