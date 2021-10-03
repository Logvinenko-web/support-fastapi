from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from src.database.models.models import  Education_Days, Education_Tasks


def get_all(db: Session):
    days = db.query(Education_Days).all()
    return days

def get_all_task(db: Session):
    tasks = db.query(Education_Tasks).all()
    return tasks

def createEducationDay(request, db: Session):
    new_day = Education_Days(
        day=request.day,
    )
    db.add(new_day)
    db.commit()
    db.refresh(new_day)
    return new_day

def createEducationTask(id, request, db: Session):
    new_doc = Education_Tasks(
        education_day_id=id,
        name=request.name,
        link=request.link,
        description=request.description
    )
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    return new_doc

def deleteEducationTask(id: str, db: Session):
    education_task = db.query(Education_Tasks).filter(Education_Tasks.id == id)
    if not education_task.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Category with id {id} not found")

    education_task.delete(synchronize_session=False)
    db.commit()
    return 'done'



