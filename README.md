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

### Directory Tree

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
│   │   ├── api/          # API Route handlers (Endpoints)
│   │   ├── core/         # Core configurations
│   │   ├── db/           # Database configuration
│   │   ├── models/       # SQLAlchemy Database models
│   │   ├── schemas/      # Pydantic models (Request/Response schemas)
│   │   └── crud/         # Database operations (Create, Read, Update, Delete)
│   ├── main.py           # Application entry point
│   └── requirements.txt  # Python dependencies
│
└── docs/                 # Documentation
    ├── requirement.md    # Requirements definition
    └── design.md         # System design (ER Diagram, UI Flow)
```

### Key Directories

- **frontend/**: UIの実装。Viteを使用した高速な開発環境。
- **backend/app/**: バックエンドの主要ロジック。
    - **models/**: データベースのテーブル構造定義。
    - **schemas/**: APIのリクエスト・レスポンスの型定義（バリデーション用）。
    - **api/**: エンドポイントの実装。
- **docs/**: 設計書や要件定義書を格納。

