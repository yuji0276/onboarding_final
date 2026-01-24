from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.api import todos
app = FastAPI()

# CORS configuration
origins = [
    "http://localhost:5173",  # Vite default port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todos.router) # /api/todos

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
