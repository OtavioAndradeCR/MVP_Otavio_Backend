from flask import Blueprint
from flask_openapi3 import APIBlueprint
from schemas.user_schemas import UserCreateRequest, UserResponse, UserUpdateRequest
from schemas.path_schemas import UserIdPath
from database import db, User

users_bp = APIBlueprint('users', __name__, url_prefix='/api/users')

@users_bp.post('/')
def create_user(body: UserCreateRequest):
    """Criar um novo usuário"""
    # Verificar se usuário já existe
    existing_user = User.query.filter(
        (User.username == body.username) | (User.email == body.email)
    ).first()
    
    if existing_user:
        return {'error': 'Usuário ou email já existe'}, 400
    
    new_user = User(
        username=body.username,
        email=body.email,
        password=body.password  # Em produção, seria hasheada
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    response = UserResponse(
        id=new_user.id,
        username=new_user.username,
        email=new_user.email
    )
    return response.model_dump(), 201

@users_bp.get('/')
def get_users():
    """Buscar todos os usuários"""
    users = User.query.all()
    response = [
        UserResponse(
            id=user.id,
            username=user.username,
            email=user.email
        ).model_dump() for user in users
    ]
    return response, 200

@users_bp.get('/<int:user_id>')
def get_user(path: UserIdPath):
    """Buscar usuário por ID"""
    user = User.query.get(path.user_id)
    if not user:
        return {'error': 'Usuário não encontrado'}, 404
    
    response = UserResponse(
        id=user.id,
        username=user.username,
        email=user.email
    )
    return response.model_dump(), 200

@users_bp.put('/<int:user_id>')
def update_user(path: UserIdPath, body: UserUpdateRequest):
    """Atualizar usuário"""
    user = User.query.get(path.user_id)
    if not user:
        return {'error': 'Usuário não encontrado'}, 404
    
    if body.username:
        user.username = body.username
    if body.email:
        user.email = body.email
    if body.password:
        user.password = body.password
    
    db.session.commit()
    
    response = UserResponse(
        id=user.id,
        username=user.username,
        email=user.email
    )
    return response.model_dump(), 200

@users_bp.delete('/<int:user_id>')
def delete_user(path: UserIdPath):
    """Deletar usuário"""
    user = User.query.get(path.user_id)
    if not user:
        return {'error': 'Usuário não encontrado'}, 404
    
    db.session.delete(user)
    db.session.commit()
    return {'message': 'Usuário deletado com sucesso'}, 200

