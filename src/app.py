from contextlib import asynccontextmanager
from databases import Database
from fastapi import FastAPI
from api import include_routers
from core.settings import get_settings
import controller.todo as todo_module

config = get_settings()

db = Database(config.db.dsn)

@asynccontextmanager
async def lifespan(_app: FastAPI):
    await db.connect()
    todo_module.todo_controller = todo_module.TodoController(db)
    yield
    await db.disconnect()


app = FastAPI(
    lifespan=lifespan, 
    title="Fasr API - todo list Ivan")
include_routers(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host = "0.0.0.0", port = 8000)






# GET
# POST
# DELETE
# PATCH