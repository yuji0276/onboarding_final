#
from app.models.todo import Todo
from sqlalchemy.orm import Session
from app.schemas.todo import TodoPost, TodoGet


def create_todo(todo: TodoPost, db: Session) -> TodoGet:
    todo = Todo(**todo.model_dump())  # pydanticモデルをORMのモデルに変換
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return TodoGet.model_validate(todo)  # ORMモデルをpydanticモデルに変換
