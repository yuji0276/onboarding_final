from app.models.todo import Todo
from sqlalchemy.orm import Session
from app.schemas.todo import TodoUpdate, TodoGet


def update_todo(todo_id: int, todo: TodoUpdate, db: Session) -> TodoGet | None:
    db_todo = db.get(Todo, todo_id)
    if not db_todo:
        return None

    todo_data = todo.model_dump()
    for key, value in todo_data.items():
        setattr(db_todo, key, value)

    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return TodoGet.model_validate(db_todo)
