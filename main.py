import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, redirect
from flask_openapi3 import OpenAPI, Info
from flask_cors import CORS
from database import db
from api.users import users_bp
from api.appointments import appointments_bp

info = Info(title='Sistema de Agendamento e Gestão', version='1.0.0')
app = OpenAPI(__name__, info=info)

# Configurar banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agendamento.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar banco de dados
db.init_app(app)

# Configurar CORS para permitir acesso do frontend
CORS(app, origins="*")

# Registrar blueprints
app.register_api(users_bp)
app.register_api(appointments_bp)

@app.route('/')
def home():
    return redirect('/openapi/swagger')

# Criar tabelas do banco de dados
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

