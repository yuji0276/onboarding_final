from fastapi import APIRouter
from app.crud.get_todos import get_all_todos
from app.crud.create_todo import create_todo
from app.crud.update_todo import update_todo
from app.schemas.todo import TodoPost, TodoGet
router = APIRouter()

@router.get("/api/todos")
def read_root():
    return get_all_todos()

@router.post("/api/todos", response_model=TodoGet)
def create_root(todo: TodoPost):
    return create_todo(todo)

@router.put("/api/todos/{id}", response_model=TodoGet)
def update_root(id: int, todo: TodoPost):
    return update_todo(id, todo)
