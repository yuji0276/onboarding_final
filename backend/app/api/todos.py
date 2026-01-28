from fastapi import APIRouter, HTTPException
from app.crud.get_todos import get_all_todos, get_todo
from app.crud.create_todo import create_todo
from app.crud.update_todo import update_todo
from app.crud.delete_todo import delete_todo
from app.schemas.todo import TodoPost, TodoGet, TodoUpdate
from app.core.database import session_local
router = APIRouter()

@router.get("/api/todos", response_model=list[TodoGet], status_code=200)
def get_todos():
    return get_all_todos(session_local)

@router.post("/api/todos", response_model=TodoGet, status_code=201)
def create_new_todo(todo: TodoPost):
    return create_todo(todo, session_local)

@router.get("/api/todos/{id}", response_model=TodoGet, status_code=200)
def read_todo(id: int):
    return get_todo(id, session_local)

@router.delete("/api/todos/{id}", status_code=204)
def delete_todo_item(id: int):
    result = delete_todo(id,session_local)
    if result is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}

@router.put("/api/todos/{id}", response_model=TodoGet, status_code=200)
def update_todo_item(id: int, todo: TodoUpdate):
    updated_todo = update_todo(id, todo,session_local)
    if updated_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo
