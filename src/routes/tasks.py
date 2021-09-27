
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.database.database import get_db
from ..controllers import  task
from ..schema.task.schema import TaskModelBase

routerTasks = APIRouter(
    prefix="/tasks",
    tags=["Task"]
)


@routerTasks.post("", status_code=status.HTTP_201_CREATED)
def create_task(
        request: TaskModelBase,
        db: Session = Depends(get_db),
):
    return task.createTask(request, db)


@routerTasks.get("",)
def get_tasks(db: Session = Depends(get_db)):
    return task.getAllTasks(db)


@routerTasks.get("/{id}", status_code=200)
def get_task_id(id, db: Session = Depends(get_db)):
    return task.showTasks(id, db)


@routerTasks.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id, db: Session = Depends(get_db)):
    return task.deleteTask(id, db)


@routerTasks.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_task(id, request: TaskModelBase, db: Session = Depends(get_db)):
    return task.updateTask(id, request, db)