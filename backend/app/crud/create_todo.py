from app.models.todo import Todo
from sqlalchemy.orm import Session


def create_todo(todo: Todo, db: Session) -> Todo:
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo