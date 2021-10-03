from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.database.database import get_db
from ..controllers import education

from ..schema.education.schema import EducationDayModelBase, EducationTaskModelBase, EducationTaskModelTest

routerEducations = APIRouter(
    prefix="/educations",
    tags=["Education"]
)


@routerEducations.post("", status_code=status.HTTP_201_CREATED)
def create_education_day(
        request: EducationDayModelBase,
        db: Session = Depends(get_db),
):
    return education.createEducationDay(request, db)

@routerEducations.get("")
def get_days(db: Session = Depends(get_db)):
    return education.get_all(db)

@routerEducations.get("/education_tasks")
def get_education_task(db: Session = Depends(get_db)):
    return education.get_all_task(db)

@routerEducations.post("/{id}/education_task")
def create_education_task(
        id,
        request: EducationTaskModelBase,
        db: Session = Depends(get_db),
):
    return education.createEducationTask(id, request, db)

@routerEducations.delete("/education_task/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category_id(id, db: Session = Depends(get_db)):
    return education.deleteEducationTask(id, db)





