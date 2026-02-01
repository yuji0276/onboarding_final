from app.models.todo import Todo
from sqlalchemy.orm import Session


def get_all_todos(
    db: Session,
) -> list[Todo]:
    return db.query(Todo).all()


def get_todo(todo_id: int, db: Session) -> Todo | None:
    todo = db.get(Todo, todo_id)
    return todo
