from app.models.todo import Todo
from sqlalchemy.orm import Session
from app.schemas.todo import TodoGet


def get_all_todos(db: Session) -> list[TodoGet]:
    todos = db.query(Todo).all()
    return [TodoGet.model_validate(todo) for todo in todos]


def get_todo(todo_id: int, db: Session) -> TodoGet | None:
    todo = db.get(Todo, todo_id)
    if todo:
        return TodoGet.model_validate(todo)
    return
