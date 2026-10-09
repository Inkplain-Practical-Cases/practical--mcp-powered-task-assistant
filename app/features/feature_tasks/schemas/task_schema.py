# Validate the task content; a model cannot create arbitrary priority levels.
from datetime import date
from typing import Literal
from pydantic import BaseModel, Field, field_validator

class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=160)
    due_date: date
    priority: Literal["normal", "urgent"] = "normal"

    @field_validator("due_date")
    @classmethod
    def reject_past_date(cls, value: date) -> date:
        if value < date.today():
            raise ValueError("due_date must not be in the past")
        return value
