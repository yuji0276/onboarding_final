from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class TodoBase(BaseModel):
    title: str
    description: str
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    completed: bool = False


class TodoPost(TodoBase):
    pass


class TodoUpdate(TodoBase):
    pass


class TodoGet(TodoBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class TodoDelete(TodoBase):
    pass
