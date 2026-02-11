from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class TodoBase(BaseModel):
    title: str | None = None
    description: str | None = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    completed: bool = False

    model_config = ConfigDict(from_attributes=True)


class TodoGet(TodoBase):
    id: int
    created_at: datetime


class TodoPost(TodoBase):
    pass


class TodoUpdate(TodoBase):
    pass


class TodoDelete(TodoBase):
    pass
