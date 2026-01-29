from app.models.todo import Todo
from app.schemas.todo import TodoPost, TodoUpdate
from app.crud.get_todos import get_all_todos, get_todo
from app.crud.create_todo import create_todo
from app.crud.delete_todo import delete_todo
from app.crud.update_todo import update_todo
from datetime import datetime


def test_get_all_todos(test_db_session):
    new_todo = Todo(title="task for test", description="this is test")
    test_db_session.add(new_todo)
    test_db_session.commit()

    result = get_all_todos(test_db_session)

    assert len(result) == 1
    assert result[0].title == "task for test"


def test_get_todo(test_db_session):
    new_todo = Todo(title="task for test", description="this is test")
    test_db_session.add(new_todo)
    test_db_session.commit()

    result = get_todo(1, test_db_session)

    assert result != None
    assert result.title == "task for test"
    assert result.description == "this is test"


def test_create_todo(test_db_session):

    target_date = datetime(2026, 1, 29)

    test_todo = TodoPost(
        title="task for test",
        description="this is test",
        start_date=target_date,
        completed=False,
    )

    result = create_todo(test_todo, test_db_session)

    assert result != None
    assert result.start_date == target_date
    assert result.end_date == None
    assert result.id is not None


def test_update_todo(test_db_session):
    new_todo = Todo(title="task for test", description="this is test")
    test_db_session.add(new_todo)
    test_db_session.commit()

    todo = TodoUpdate(
        title="test for update",
        description="this is test for updating",
    )

    result = update_todo(1, todo, test_db_session)

    assert result != None
    assert result.title == "test for update"


def test_delete_todo(test_db_session):
    new_todo = Todo(title="task for test", description="this is test")
    test_db_session.add(new_todo)
    test_db_session.commit()

    delete_todo(1, test_db_session)

    deleted_todo = test_db_session.get(Todo, 1)
    assert deleted_todo is None
