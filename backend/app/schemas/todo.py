from pydantic import BaseModel, ConfigDict, Field, model_validator
from datetime import datetime
from typing import Optional


class TodoBase(BaseModel):
    title: str = Field(
        min_length=1,
    )
    description: str | None = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    completed: bool = False

    model_config = ConfigDict(from_attributes=True)

    @model_validator(mode="after")
    def check_date_order(self):
        start = self.start_date
        end = self.end_date
        if start and end and start > end:
            raise ValueError("Please ensure the end date is after the start date.")
        return self


class TodoGet(TodoBase):
    id: int
    created_at: datetime


class TodoPost(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1)
    description: str | None = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    completed: bool | None = None

    model_config = ConfigDict(from_attributes=True)

    @model_validator(mode="after")
    def check_date_order(self):
        start = self.start_date
        end = self.end_date
        if start and end and start > end:
            raise ValueError("Please ensure the end date is after the start date.")
        return self


class TodoDelete(TodoBase):
    pass
