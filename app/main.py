from fastapi import FastAPI

from app.database import create_db_and_tables
from app.routers import auth, users, tasks

app = FastAPI(title="Task Management API")


@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()


app.include_router(auth.router)
app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"status": "API is running 🚀"}