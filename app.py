from fastapi import FastAPI, Depends, HTTPException, status
from auth import get_current_user, create_access_token
from crud import create_task, get_tasks, delete_task
from models import Task, TaskCreate, User, UserLogin
from database import init_db

app = FastAPI()

# Initialize database
init_db()

@app.post("/token")
def login(user: UserLogin):
    token = create_access_token(user)
    return {"access_token": token, "token_type": "bearer"}

@app.post("/tasks/", response_model=Task)
def add_task(task: TaskCreate, user: User = Depends(get_current_user)):
    return create_task(task, user)

@app.get("/tasks/", response_model=list[Task])
def list_tasks(user: User = Depends(get_current_user)):
    return get_tasks(user)

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int, user: User = Depends(get_current_user)):
    delete_task(task_id, user)
    return {"detail": "Task deleted"}
