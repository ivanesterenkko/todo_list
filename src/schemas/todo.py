from pydantic import UUID4, BaseModel


class TodoListResponse(BaseModel):
    id: UUID4
    title: str


class TodoListRequest(BaseModel):
    title: str