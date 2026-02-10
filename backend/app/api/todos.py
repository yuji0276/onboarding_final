from app.schemas.todo import TodoPost, TodoGet, TodoUpdate
from app.core.database import get_db_session
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends
from app.crud.get_todos import get_all_todos, get_todo
from app.crud.create_todo import create_todo
from app.crud.update_todo import update_todo
from app.crud.delete_todo import delete_todo

router = APIRouter()


@router.get("/api/todos", response_model=list[TodoGet], status_code=200)
def get_todos(db: Session = Depends(get_db_session)):
    return get_all_todos(db)


@router.post("/api/todos", response_model=TodoGet, status_code=201)
def create_new_todo(todo: TodoPost, db: Session = Depends(get_db_session)):
    return create_todo(todo, db)


@router.get("/api/todos/{id}", response_model=TodoGet, status_code=200)
def read_todo(id: int, db: Session = Depends(get_db_session)) -> TodoGet | None:
    todo = get_todo(id, db)

    if todo is None:
        raise HTTPException(status_code=404, detail="todo not found")
    return todo


@router.delete("/api/todos/{id}", status_code=204)
def delete_todo_item(id: int, db: Session = Depends(get_db_session)):
    is_delete_success = delete_todo(id, db)

    if is_delete_success:
        raise HTTPException(status_code=404, detail="todo not found")
    return None


@router.patch("api/todos/{id}", response_model=TodoGet, status_code=200)
def update_todo_item(id: int, todo: TodoUpdate, db: Session = Depends(get_db_session)):
    updated_todo = update_todo(id, todo, db=Depends(get_db_session))
    if updated_todo is None:
        raise HTTPException(status_code=404, detail="todo not found")
    return updated_todo
