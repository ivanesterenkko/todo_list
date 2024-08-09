from fastapi import APIRouter


router = APIRouter()


@router.get(
        "/lists",
        response_model=list[TodoListResponse]
        )
async def get_lists(
    todo_controller: TodoController = Depends(get_todo_controller),
) -> list[TodoListResponse]:
    result = await todo_controller.get_lists()
    return result


@router.delete(
        "/lists/{list_id}",
        status_code=204,
        )
async def delete_lists(
    list_id: UUID4,
    todo_controller: TodoController = Depends(get_todo_controller)
):
    await todo_controller.delete_list(list_id)


@router.post(
        "/lists",
        response_model=TodoListResponse,
        status_code=201,
    )
async def create_lists(
    todo_request: TodoListRequest,
    todo_controller: TodoController = Depends(get_todo_controller),

):
    result = await todo_controller.create_lists(todo_request.title)
    return result

@router.get("/lists/{list_id}/todos")
def get_todo():
    return

@router.delete("/lists/{list_id}/todos/{todo_id}")
def delete_todo():
    return

@router.post("/lists/{list_id}/todos")
def create_todo():
    return

@router.patch("/lists/{list_id}/todos/{todo_id}")
def update_todo():
    return