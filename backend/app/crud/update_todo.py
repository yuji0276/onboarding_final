from app.models.todo import Todo
from sqlalchemy.orm import Session
from app.schemas.todo import TodoUpdate, TodoGet


def update_todo(todo_id: int, todo_update: TodoUpdate, db: Session) -> TodoGet | None:
    todo = db.get(Todo, todo_id)  # 失敗時はNoneが返る

    update_data = todo_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(todo, key, value)

    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo
