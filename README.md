# Todo Application (Fullstack)

A full-stack Todo application featuring a FastAPI backend with SQLite database and a React (Vite) frontend.

## Tech Stack

### Frontend
- **Framework**: React 19 (Vite)
- **Language**: TypeScript
- **Styling**: CSS (Vanilla)

### Backend
- **Framework**: FastAPI
- **Language**: Python 3.9+
- **Database**: SQLite (via SQLAlchemy)
- **ORM**: SQLAlchemy
- **Data Validation**: Pydantic
- **Testing**: Pytest

## Features

- **Todo Management**:
  - Create new todos
  - List all todos
  - Get specific todo details
  - Update existing todos
  - Delete todos
- **API Documentation**: Automatic interactive API docs provided by FastAPI (Swagger UI).

## Setup

### 1. Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

The server will start at `http://localhost:8000`.
- **API Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend development server will usually start at `http://localhost:5173`.

## Project Structure

```
project/
├── frontend/             # Frontend Application (React + Vite + TypeScript)
│   ├── public/           # Static assets
│   └── src/              # Source code
│       ├── assets/       # Images, styles, etc.
│       ├── App.tsx       # Main component
│       └── main.tsx      # Entry point
│
├── backend/              # Backend API (FastAPI + Python)
│   ├── app/              # Application logic
│   │   ├── api/          # API Route handlers (endpoints like todos.py)
│   │   ├── core/         # Core configurations (database connection, etc)
│   │   ├── crud/         # Database operations (create, read, update, delete)
│   │   ├── models/       # SQLAlchemy Database models
│   │   └── schemas/      # Pydantic models (Request/Response schemas)
│   ├── main.py           # Application entry point
│   ├── requirements.txt  # Python dependencies
│   └── test.db           # SQLite database file (generated after running)
│
└── docs/                 # Documentation
```
