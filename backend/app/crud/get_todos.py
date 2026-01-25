from app.models.todo import Todo
from app.core.database import SessionLocal
from app.schemas.todo import TodoGet

def get_all_todos() -> list[TodoGet]:
    with SessionLocal() as db:
        todos = db.query(Todo).all()
        return todos

def get_todo(todo_id: int) -> TodoGet | None:
    with SessionLocal() as db:
        todo = db.get(Todo, todo_id)
        if todo:
            return TodoGet.model_validate(todo)
        return None