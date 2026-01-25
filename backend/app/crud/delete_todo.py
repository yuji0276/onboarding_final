from app.models.todo import Todo
from app.core.database import SessionLocal
from app.schemas.todo import  TodoGet

def delete_todo(todo_id: int) -> int | None:
    with SessionLocal() as db:
        db_todo = db.get(Todo, todo_id)
        if not db_todo:
            print("Todo not found")
            return None
        db.delete(db_todo)
        db.commit()
        print("Todo deleted successfully")
        return todo_id