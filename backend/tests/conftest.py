import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import todo
from app.core.database import Base
from main import app
from app.core.database import get_db_session
from fastapi.testclient import TestClient
from app.models.todo import Todo
from sqlalchemy.pool import StaticPool

TEST_DATABASE_URL = "sqlite:///:memory:"


@pytest.fixture(scope="function")
def test_db_session():
    engine = create_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)

    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)
        engine.dispose()


@pytest.fixture(scope="function")
def client(test_db_session):
    app.dependency_overrides[get_db_session] = lambda: test_db_session

    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


@pytest.fixture(scope="function")
def sample_todo(test_db_session):
    todo = Todo(title="test", description="this is test")
    test_db_session.add(todo)
    test_db_session.commit()
    test_db_session.refresh(todo)
    return todo
