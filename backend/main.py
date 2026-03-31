from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.api import todos
app = FastAPI()

@app.middleware("http")
async def add_charset_utf8_header(request: Request, call_next):
    response = await call_next(request)
    content_type = response.headers.get("content-type")
    if content_type and "application/json" in content_type:
        response.headers["content-type"] = "application/json; charset=utf-8"
    return response

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

#各エンドポイントへのルータの登録
app.include_router(todos.router) # /api/todos

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
