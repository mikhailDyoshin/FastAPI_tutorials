from pydantic import BaseModel


# An example of nested models
class Item(BaseModel):
    item: str
    status: str

class Todo(BaseModel):
    id: int
    item: Item