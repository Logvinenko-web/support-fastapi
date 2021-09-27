from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from src.database.models.models import Tasks
from src.schema.task.schema import TaskModelBase


def getAllTasks(db: Session):
    tasks = db.query(Tasks).all()
    return tasks


def createTask(request, db: Session):
    new_task = Tasks(
        description=request.description,
        status=request.status,
        title=request.title
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def deleteTask(id: str, db: Session):
    task = db.query(Tasks).filter(Tasks.id == id)
    if not task.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Task with id {id} not found")
    task.delete(synchronize_session=False)
    db.commit()
    return 'done'


def updateTask(id: str, request: TaskModelBase, db: Session):
    task = db.query(Tasks).filter(Tasks.id == id)
    if not task.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Task with id {id} not found")
    task.update({
        "description": request.description,
        "status": request.status,
        "title": request.title
    })
    db.commit()
    return task.first()


def showTasks(id: str, db: Session):
    task = db.query(Tasks).filter(Tasks.id == id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Task with the id {id} is not available")
    return task
