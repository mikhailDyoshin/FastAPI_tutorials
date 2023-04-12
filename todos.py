from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from model import Todo, TodoItem, TodoItems
from fastapi.templating import Jinja2Templates


todo_router = APIRouter()

todo_list = []

# loading templates
templates = Jinja2Templates(directory='templates/')


@todo_router.post("/todos")
async def add_todo(request: Request, todo: Todo=Depends(Todo.as_form)):
    """
        Adds todos to the todo-list.
    """
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    # Sending data to the template
    return templates.TemplateResponse(
        'todo.html',
        {
            "request": request,
            "todos": todo_list,
        }
    )


@todo_router.get("/todos", response_model=TodoItems)
async def retrieve_todos(request: Request):
    """
        Retrieves all existing todos.
    """
    return templates.TemplateResponse(
        'todo.html',
        {
            "request": request,
            "todos": todo_list,
        }
    )


@todo_router.get("/todos/{todo_id}")
async def retrieve_single_todo(request: Request, todo_id: int=Path(..., title="The ID of the todo to retrieve")) -> dict:
    """
        Retrieves the todo with given ID using a path parameter.
    """
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse(
                'todo.html',
                {
                    "request": request,
                    "todo": todo,
                }
            )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist.",
    )


@todo_router.put("/todos/{todo_id}")
async def update_todo(todo_data:TodoItem, todo_id:int=Path(..., title="The ID of the todo to be updated")) -> dict:
    """
        Updates the todo with given ID using a path parameter.
    """
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {"message": "Todo updated succesfully."}
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist."
    )


@todo_router.delete("/todos/{todo_id}")
async def delete_single_todo(todo_id:int=Path(..., title="The ID of the todo to be deleted")) -> dict:
    """
        Deletes the todo with given ID using a path parameter.
    """
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list.pop(index)
            return {"message": "Todo deleted successfully!"}
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist.",
    )

@todo_router.delete("/todos")
async def delete_all_todos() -> dict:
    todo_list.clear()
    return {"message": "Todos deleted successfully"}
