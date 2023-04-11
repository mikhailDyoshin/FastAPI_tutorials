from pydantic import BaseModel
from typing import List


# An example of nested models
class Item(BaseModel):
    item: str
    status: str

class Todo(BaseModel):
    id: int
    item: Item

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
    