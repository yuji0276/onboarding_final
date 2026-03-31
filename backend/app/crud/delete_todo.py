from app.models.todo import Todo
from app.schemas.todo import TodoGet
from sqlalchemy.orm import Session


def delete_todo(todo_id: int, db: Session) -> bool:  # idを指定して成功可否のみを返す
    deleted_todo = db.get(Todo, todo_id)  # 失敗時は　Noneが返る
    if deleted_todo is None:
        return False
    db.delete(deleted_todo)
    db.commit()
    return True
