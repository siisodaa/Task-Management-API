from sqlalchemy.orm import Session
from models import TaskCreate, TaskDB, UserLogin
from database import get_db

def create_task(task: TaskCreate, user: UserLogin):
    db = get_db()
    new_task = TaskDB(title=task.title, description=task.description, user=user.username)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_tasks(user: UserLogin):
    db = get_db()
    return db.query(TaskDB).filter(TaskDB.user == user.username).all()

def delete_task(task_id: int, user: UserLogin):
    db = get_db()
    task = db.query(TaskDB).filter(TaskDB.id == task_id, TaskDB.user == user.username).first()
    if task:
        db.delete(task)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Task not found")
