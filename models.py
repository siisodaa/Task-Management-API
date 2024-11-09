from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Column, Integer, String
from database import Base

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class Task(TaskCreate):
    id: int

class UserLogin(BaseModel):
    username: str

# SQLAlchemy Task model
class TaskDB(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    user = Column(String, index=True)
