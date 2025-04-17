# main.py

from fastapi import FastAPI
from models import user
from database import engine
from routers import auth as user_router

# Ma'lumotlar bazasini yaratish
user.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Routerni ilovaga qo‘shish
app.include_router(user_router.router)
