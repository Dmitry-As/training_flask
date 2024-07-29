from typing import Optional
from pydantic import BaseModel


class Task(BaseModel):
    id: int
    name: str
    completed: bool = False
    definition: Optional [str] = None


class CreateTask(BaseModel):
    name: str
    completed: bool = False
    definition: Optional [str] = None
  