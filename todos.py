from fastapi import APIRouter, Path
from model import Todo


todo_router = APIRouter()

todo_list = []

@todo_router.post("/todos")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {'message': 'Todo added successfully'}


@todo_router.get("/todos")
async def retrieve_todos() -> dict:
    return {'todos': todo_list}

@todo_router.get("/todos/{todo_id}")
async def retrieve_single_todo(todo_id: int=Path(..., title="The ID of the todo to retrieve")) -> dict:
    """
        Retrieves the todo with given ID using path parameter.
    """
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo,
            }
    return {"message": "Todo with supplied ID doesn't exist."}
