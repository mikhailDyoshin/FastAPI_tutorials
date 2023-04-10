from fastapi import APIRouter


todo_router = APIRouter()

todo_list = []

@todo_router.post("/todos")
async def add_todo(todo: dict) -> dict:
    todo_list.append(todo)
    return {'message': 'Todo added successfully'}


@todo_router.get("/todos")
async def retrieve_todos() -> dict:
    return {'todos': todo_list}
    