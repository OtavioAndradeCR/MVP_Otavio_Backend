# Sistema de Agendamento e Gestão - Backend

## Descrição do Projeto

Este é o backend do Sistema de Agendamento e Gestão para Pequenos Negócios. O sistema oferece uma API RESTful completa para gerenciamento de usuários e agendamentos, implementada com Flask, Pydantic e flask-openapi3.

## Tecnologias Utilizadas

- **Python 3.11+**
- **Flask** - Framework web para Python
- **flask-openapi3** - Extensão para documentação automática da API com OpenAPI/Swagger
- **Pydantic** - Validação de dados e serialização
- **SQLAlchemy** - ORM para banco de dados
- **Flask-SQLAlchemy** - Integração do SQLAlchemy com Flask
- **SQLite** - Banco de dados relacional leve
- **Flask-CORS** - Suporte a Cross-Origin Resource Sharing

## Estrutura do Projeto

```

│   ├── __init__.py
│   ├── main.py              # Arquivo principal da aplicação
│   ├── database.py          # Configuração do banco de dados
│   ├── api/
│   │   ├── __init__.py
│   │   ├── users.py         # Rotas para gerenciamento de usuários
│   │   └── appointments.py  # Rotas para gerenciamento de agendamentos
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py          # Modelo Pydantic para usuários
│   │   └── appointment.py   # Modelo Pydantic para agendamentos
│   └── schemas/
│       ├── __init__.py
│       ├── user_schemas.py      # Schemas de requisição/resposta para usuários
│       ├── appointment_schemas.py # Schemas de requisição/resposta para agendamentos
│       └── path_schemas.py      # Schemas para parâmetros de path
├── requirements.txt         # Dependências do projeto
└── README.md               # Este arquivo
```

## Instalação e Configuração

### Pré-requisitos

- Python 3.11 ou superior
- pip (gerenciador de pacotes do Python)

### Passos para Instalação

1. **Clone o repositório ou navegue até a pasta do backend:**
   ```bash
   cd backend
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a aplicação:**
   ```bash
   python main.py
   ```

4. **A aplicação estará disponível em:**
   - API: http://localhost:5000
   - Documentação Swagger: http://localhost:5000/openapi/swagger

## Configuração do Banco de Dados

O sistema utiliza SQLite como banco de dados, que é criado automaticamente na primeira execução da aplicação. O arquivo do banco será criado em `app/instance/agendamento.db`.

### Modelos de Dados

#### Usuários (users)
- `id` (Integer, Primary Key)
- `username` (String, Unique)
- `email` (String, Unique)
- `password` (String)
- `created_at` (DateTime)

#### Agendamentos (appointments)
- `id` (Integer, Primary Key)
- `user_id` (Integer, Foreign Key)
- `title` (String)
- `description` (Text, Optional)
- `date_time` (DateTime)
- `status` (String, Default: 'agendado')
- `created_at` (DateTime)

## Endpoints da API

### Usuários

#### POST /api/users/
Criar um novo usuário

**Corpo da Requisição:**
```json
{
  "username": "string",
  "email": "string",
  "password": "string"
}
```

**Resposta (201):**
```json
{
  "id": 1,
  "username": "string",
  "email": "string"
}
```

#### GET /api/users/
Buscar todos os usuários

**Resposta (200):**
```json
[
  {
    "id": 1,
    "username": "string",
    "email": "string"
  }
]
```

#### GET /api/users/{user_id}
Buscar usuário por ID

**Resposta (200):**
```json
{
  "id": 1,
  "username": "string",
  "email": "string"
}
```

#### PUT /api/users/{user_id}
Atualizar usuário

**Corpo da Requisição:**
```json
{
  "username": "string",
  "email": "string",
  "password": "string"
}
```

#### DELETE /api/users/{user_id}
Deletar usuário

**Resposta (200):**
```json
{
  "message": "Usuário deletado com sucesso"
}
```

### Agendamentos

#### POST /api/appointments/
Criar um novo agendamento

**Corpo da Requisição:**
```json
{
  "user_id": 1,
  "title": "string",
  "description": "string",
  "date_time": "2025-07-01T10:00:00"
}
```

**Resposta (201):**
```json
{
  "id": 1,
  "user_id": 1,
  "title": "string",
  "description": "string",
  "date_time": "2025-07-01T10:00:00",
  "status": "agendado"
}
```

#### GET /api/appointments/
Buscar todos os agendamentos

#### GET /api/appointments/{appointment_id}
Buscar agendamento por ID

#### PUT /api/appointments/{appointment_id}
Atualizar agendamento

#### DELETE /api/appointments/{appointment_id}
Deletar agendamento

## Comandos de Inicialização

Para iniciar o servidor de desenvolvimento:

```bash
python main.py
```

O servidor será iniciado em modo debug na porta 5000.

## Documentação da API

A documentação completa da API está disponível através do Swagger UI em:
http://localhost:5000/openapi/swagger