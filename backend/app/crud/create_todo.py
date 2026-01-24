from app.models.todo import Todo
from app.core.database import SessionLocal
from app.schemas.todo import TodoPost, TodoGet

def create_todo(todo: TodoPost) -> TodoGet:
    with SessionLocal() as db:
        db_todo = Todo(**todo.dict())
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return TodoGet.model_validate(db_todo)