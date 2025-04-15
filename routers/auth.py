from fastapi import APIRouter, HTTPException
from models.user import User
from schema.user_schema import UserCreate
from utils import get_password_hash, verify_password, create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
async def register(user: UserCreate):
    existing_user = await User.get_or_none(username=user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    hashed_password = get_password_hash(user.password)
    new_user = await User.create(username=user.username, email=user.email, password=hashed_password)
    return {"message": "User registered successfully"}

@router.post("/login")
async def login(user: UserCreate):
    db_user = await User.get_or_none(username=user.username)
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}
