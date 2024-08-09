from fastapi import APIRouter, Depends
from pydantic import UUID4

from controller.todo import TodoController, get_todo_controller
from schemas.todo import TodoItemRequest, TodoItemResponse


router = APIRouter()


@router.get(
        "/lists/{list_id}/todos",
        response_model=list[TodoItemResponse],
        )
async def get_todos(
    todo_controller: TodoController = Depends(get_todo_controller),
) -> list[TodoItemResponse]:
    result = await todo_controller.get_items()
    return result

@router.delete(
        "/lists/{list_id}/todos/{todo_id}",
        status_code=204,
        )
async def delete_todo(
    item_id: UUID4,
    todo_controller: TodoController = Depends(get_todo_controller)
):
    await todo_controller.delete_item(item_id)

@router.post(
        "/lists/{list_id}/todos",
        response_model=TodoItemResponse,
        status_code=201,
        )
async def create_todo(
    todo_request: TodoItemRequest,
    todo_controller: TodoController = Depends(get_todo_controller),

):
    result = await todo_controller.create_items(todo_request.title,todo_request.list_id )
    return result

@router.patch("/lists/{list_id}/todos/{todo_id}")
def update_todo():
    return