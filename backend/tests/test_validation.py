from app.schemas.todo import TodoBase
from pydantic import ValidationError
import pytest
from datetime import datetime


def test_todo_validation_fail():
    # title空文字の時エラー
    with pytest.raises(ValidationError) as excinfo:
        TodoBase(title="", description="this is test")

    # start_date > end_dateの時エラー
    with pytest.raises(ValidationError) as exinfo:
        bad_start = datetime(2026, 1, 1)
        bad_end = datetime(2025, 1, 1)
        TodoBase(title="test", start_date=bad_start, end_date=bad_end)
