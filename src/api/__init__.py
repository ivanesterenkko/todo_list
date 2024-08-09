from api.todo_items import router as todo_items_router
from api.todo_list import router as todo_list_router


def include_routers(app):
    app.include_router(todo_items_router, tags = ["todos"])
    app.include_router(todo_list_router, tags = ["lists"])

