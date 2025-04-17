from database import Base
from sqlalchemy import Column, String, Integer


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=True)
    password = Column(String, nullable=True)