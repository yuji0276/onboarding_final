from app.models.todo import Todo
from sqlalchemy.orm import Session


def delete_todo(todo_id: int, db: Session) -> None:
    db_todo = db.get(Todo, todo_id)
    if not db_todo:
        print("Todo not found")
        return None
    db.delete(db_todo)
    db.commit()
    print("Todo deleted successfully")
    return None
