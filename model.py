from pydantic import BaseModel
from typing import List, Optional
from fastapi import Form


class Todo(BaseModel):
    id: Optional[int]
    item: str

    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(item=item)

class TodoItem(BaseModel):
    """
        The model defines request body for todo-update method.
    """
    item: str

class TodoItems(BaseModel):
    """
        The responce model. It defines what retrieve_todos-get-method returns.
    """
    todos: List[TodoItem]
    