import pytest
from app.models.todo import Todo
from confest import test_db_session
from app.crud.get_todos import get_all_todos, get_todo
from app.crud.create_todo import create_todo
from app.crud.delete_todo import delete_todo
from app.crud.update_todo import update_todo



def test_get_all_todos(test_db_session):
    new_todo = Todo(title="task for test", description="this is test")
    test_db_session.add(new_todo)
    test_db_session.commit()

    result = get_all_todos(test_db_session)

    assert len(result) ==1
    assert result[0].title == "task for test"