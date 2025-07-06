from flask import Blueprint
from flask_openapi3 import APIBlueprint
from schemas.appointment_schemas import AppointmentCreateRequest, AppointmentResponse, AppointmentUpdateRequest
from schemas.path_schemas import AppointmentIdPath
from database import db, Appointment, User

appointments_bp = APIBlueprint('appointments', __name__, url_prefix='/api/appointments')

@appointments_bp.post('/')
def create_appointment(body: AppointmentCreateRequest):
    """Criar um novo agendamento"""
    # Verificar se o usuário existe
    user = User.query.get(body.user_id)
    if not user:
        return {'error': 'Usuário não encontrado'}, 404
    
    new_appointment = Appointment(
        user_id=body.user_id,
        title=body.title,
        description=body.description,
        date_time=body.date_time,
        status='agendado'
    )
    
    db.session.add(new_appointment)
    db.session.commit()
    
    response = AppointmentResponse(
        id=new_appointment.id,
        user_id=new_appointment.user_id,
        title=new_appointment.title,
        description=new_appointment.description,
        date_time=new_appointment.date_time,
        status=new_appointment.status
    )
    return response.model_dump(), 201

@appointments_bp.get('/')
def get_appointments():
    """Buscar todos os agendamentos"""
    appointments = Appointment.query.all()
    response = [
        AppointmentResponse(
            id=appointment.id,
            user_id=appointment.user_id,
            title=appointment.title,
            description=appointment.description,
            date_time=appointment.date_time,
            status=appointment.status
        ).model_dump() for appointment in appointments
    ]
    return response, 200

@appointments_bp.get('/<int:appointment_id>')
def get_appointment(path: AppointmentIdPath):
    """Buscar agendamento por ID"""
    appointment = Appointment.query.get(path.appointment_id)
    if not appointment:
        return {'error': 'Agendamento não encontrado'}, 404
    
    response = AppointmentResponse(
        id=appointment.id,
        user_id=appointment.user_id,
        title=appointment.title,
        description=appointment.description,
        date_time=appointment.date_time,
        status=appointment.status
    )
    return response.model_dump(), 200

@appointments_bp.put('/<int:appointment_id>')
def update_appointment(path: AppointmentIdPath, body: AppointmentUpdateRequest):
    """Atualizar agendamento"""
    appointment = Appointment.query.get(path.appointment_id)
    if not appointment:
        return {'error': 'Agendamento não encontrado'}, 404
    
    if body.title:
        appointment.title = body.title
    if body.description:
        appointment.description = body.description
    if body.date_time:
        appointment.date_time = body.date_time
    if body.status:
        appointment.status = body.status
    
    db.session.commit()
    
    response = AppointmentResponse(
        id=appointment.id,
        user_id=appointment.user_id,
        title=appointment.title,
        description=appointment.description,
        date_time=appointment.date_time,
        status=appointment.status
    )
    return response.model_dump(), 200

@appointments_bp.delete('/<int:appointment_id>')
def delete_appointment(path: AppointmentIdPath):
    """Deletar agendamento"""
    appointment = Appointment.query.get(path.appointment_id)
    if not appointment:
        return {'error': 'Agendamento não encontrado'}, 404
    
    db.session.delete(appointment)
    db.session.commit()
    return {'message': 'Agendamento deletado com sucesso'}, 200

