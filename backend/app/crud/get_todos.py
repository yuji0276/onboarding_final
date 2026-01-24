from app.models.todo import Todo
from app.core.database import SessionLocal
from app.schemas.todo import TodoGet

def get_all_todos() -> list[TodoGet]:
    with SessionLocal() as db:
        todos = db.query(Todo).all()
        return todos