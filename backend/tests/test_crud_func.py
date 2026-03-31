from app.models.todo import Todo
from app.schemas.todo import TodoPost, TodoUpdate
from app.crud.get_todos import get_all_todos, get_todo
from app.crud.create_todo import create_todo
from app.crud.delete_todo import delete_todo
from app.crud.update_todo import update_todo
from datetime import datetime


def test_get_all_todos_success(test_db_session):
    new_todo = Todo(title="task for test", description="this is test")
    test_db_session.add(new_todo)
    test_db_session.commit()

    good_request = get_all_todos(test_db_session)

    assert len(good_request) == 1
    assert good_request[0].title == "task for test"


def test_get_todo_success(test_db_session):
    new_todo = Todo(title="task for test", description="this is test")
    test_db_session.add(new_todo)
    test_db_session.commit()

    good_request = get_todo(new_todo.id, test_db_session)
    non_existtant_id = new_todo.id + 1
    bad_request = get_todo(non_existtant_id, test_db_session)  # 存在しないID

    assert good_request is not None
    assert good_request.title == "task for test"
    assert good_request.description == "this is test"
    assert bad_request is None


def test_create_todo_success(test_db_session):

    target_date = datetime(2026, 1, 29)

    good_todo = TodoPost(
        title="task for test",
        description="this is test",
        start_date=target_date,
        completed=False,
    )

    good_request = create_todo(good_todo, test_db_session)

    assert good_request is not None
    assert good_request.start_date == target_date


def test_update_todo_success(test_db_session):
    new_todo = Todo(title="task for test", description="this is test")
    test_db_session.add(new_todo)
    test_db_session.commit()

    todo = TodoUpdate(
        title="test for update",
        description="this is test for updating",
    )

    good_request = update_todo(1, todo, test_db_session)

    assert good_request is not None
    assert good_request.title == "test for update"


def test_delete_todo_success(test_db_session):
    new_todo = Todo(title="task for test", description="this is test")
    test_db_session.add(new_todo)
    test_db_session.commit()

    delete_todo(1, test_db_session)

    deleted_todo = test_db_session.get(Todo, 1)
    assert deleted_todo is None
