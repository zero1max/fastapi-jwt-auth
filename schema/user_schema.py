from pydantic import BaseModel, EmailStr
from models.user import User  # Tortoise User modelidan import

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True  # Bu orqali Pydantic Tortoise ORM modelidan foydalanadi

class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True  # Tortoise ORM ma'lumotlaridan to'g'ri ishlash uchun

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: str  # Pydantic `datetime` tipini stringga o'zgartiradi

    class Config:
        orm_mode = True  # Tortoise ORM modelidan foydalanish

