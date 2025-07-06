from pydantic import BaseModel

class UserIdPath(BaseModel):
    user_id: int

class AppointmentIdPath(BaseModel):
    appointment_id: int

