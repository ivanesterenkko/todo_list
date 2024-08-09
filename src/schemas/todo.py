from pydantic import UUID4, BaseModel

class TodoListResponse(BaseModel):
    id: UUID4
    title: str

class TodoListRequest(BaseModel):
    title: str

class TodoItemResponse(BaseModel):
    id: UUID4
    title: str
    list_id: UUID4
    completed: bool

class TodoItemRequest(BaseModel):
    title: str
    list_id: UUID4


