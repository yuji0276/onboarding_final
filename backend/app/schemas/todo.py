from pydantic import BaseModel
from datetime import datetime

class TodoBase(BaseModel):
    title: str
    description: str
    start_date: datetime
    end_date: datetime
    completed: bool = False

class TodoGet(TodoBase):
    id: int
    title: str
    description: str
    end_date: datetime
    completed: bool
    created_at: datetime 

class TodoPost(TodoBase):
    pass

class TodoUpdate(TodoBase):
    pass

class TodoDelete(TodoBase):
    pass