from app.models.todo import Todo
from sqlalchemy.orm import Session
from app.schemas.todo import TodoPost, TodoGet


def create_todo(todo: TodoPost, db: Session) -> TodoGet:
    db_todo = Todo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return TodoGet.model_validate(db_todo)
