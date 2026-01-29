import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import todo
from app.core.database import Base
TEST_DATABASE_URL = "sqlite:///:memory:"

@pytest.fixture(scope="function")
def test_db_session():
    engine = create_engine(
        TEST_DATABASE_URL, connect_args={"check_same_thread":False}
    )
    Base.metadata.create_all(bind=engine)

    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()