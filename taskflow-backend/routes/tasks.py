from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import Form
from database import SessionLocal
from models import Task, User
from routes.auth import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/tasks")
def create_task(
    title: str = Form(...),
    description: str = Form(...),
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):

    user = db.query(User).filter(User.username == current_user).first()

    new_task = Task(
        title=title,
        description=description,
        owner_id=user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {"message": "Task created"}
#adding get tasks route to fetch all tasks for the logged in user
@router.get("/tasks")
def get_tasks(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == current_user).first()

    tasks = db.query(Task).filter(Task.owner_id == user.id).all()

    return tasks
#adding update task route to update a task for the logged in user
@router.put("/tasks/{task_id}")
def update_task(
    task_id: int,
    title: str,
    description: str,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == current_user).first()

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        return {"error": "Task not found"}

    if task.owner_id != user.id:
        return {"error": "Not allowed"}

    task.title = title
    task.description = description

    db.commit()

    return {"message": "Task updated"}
#adding delete task route to delete a task for the logged in user
@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == current_user).first()

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        return {"error": "Task not found"}

    if task.owner_id != user.id:
        return {"error": "Not allowed"}

    db.delete(task)
    db.commit()

    return {"message": "Task deleted"}