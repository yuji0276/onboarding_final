# Todo Application (Fullstack)

## Tech Stack
- **Frontend**: React (Vite) + TypeScript
- **Backend**: FastAPI (Python)

## Requirements
- Node.js (v18+)
- Python (3.9+)

## Setup

### 1. Frontend
```bash
cd frontend
npm install
npm run dev
```

### 2. Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Project Structure
```
project/
├── frontend/          # React (Vite)
├── backend/           # FastAPI
└── docs/              # Documentation
```
