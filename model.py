from pydantic import BaseModel
from typing import List, Optional
from fastapi import Form


# An example of nested models
class Item(BaseModel):
    item: str
    status: str

class Todo(BaseModel):
    id: Optional[int]
    item: Item

    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(item=item)

class TodoItem(BaseModel):
    """
        The model defines request body for todo-update method.
    """
    item: Item

class TodoItems(BaseModel):
    """
        The responce model. It defines what retrieve_todos-get-method returns.
    """
    todos: List[TodoItem]
    