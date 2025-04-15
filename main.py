from fastapi import FastAPI
from tortoise import Tortoise
from routers import auth
from db import init_db

app = FastAPI()

app.include_router(auth.router)

@app.on_event("startup")
async def startup():
    await init_db()
    print("DB Connected ✅")

@app.on_event("shutdown")
async def shutdown():
    await Tortoise.close_connections()
    print("DB Disconnected ❌")
