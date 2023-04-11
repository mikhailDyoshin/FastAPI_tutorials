from fastapi import APIRouter, Path
from model import Todo, TodoItem


todo_router = APIRouter()

todo_list = []

@todo_router.post("/todos")
async def add_todo(todo: Todo) -> dict:
    """
        Adds todos to the todo-list.
    """
    todo_list.append(todo)
    return {'message': 'Todo added successfully'}

@todo_router.get("/todos")
async def retrieve_todos() -> dict:
    """
        Retrieves all existing todos.
    """
    return {'todos': todo_list}

@todo_router.get("/todos/{todo_id}")
async def retrieve_single_todo(todo_id: int=Path(..., title="The ID of the todo to retrieve")) -> dict:
    """
        Retrieves the todo with given ID using a path parameter.
    """
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo,
            }
    return {"message": "Todo with supplied ID doesn't exist."}

@todo_router.put("/todos/{todo_id}")
async def update_todo(todo_data:TodoItem, todo_id:int=Path(..., title="The ID of the todo to be updated")) -> dict:
    """
        Updates the todo with given ID using a path parameter.
    """
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {"message": "Todo updated succesfully."}
        
    return {"message": "Todo with supplied ID doesn't exist."}

@todo_router.delete("/todos/{todo_id}")
async def delete_single_todo(todo_id:int=Path(..., title="The ID of the todo to be deleted")) -> dict:
    """
        Deletes the todo with given ID using a path parameter.
    """
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list.pop(index)
            return {"message": "Todo deleted successfully!"}
        
    return {"message": "Todo with supplied ID doesn't exist."}

@todo_router.delete("/todos")
async def delete_all_todos() -> dict:
    todo_list.clear()
    return {"message": "Todos deleted successfully"}
