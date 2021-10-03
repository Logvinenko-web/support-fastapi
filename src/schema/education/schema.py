from pydantic import BaseModel
from typing import List


class EducationTaskModelTest(BaseModel):
    name: str


class EducationTaskModelBase(BaseModel):
    name: str
    link: str
    description: str


class EducationDayModelBase(BaseModel):
    day: str
    # education_task: List[EducationTaskModelBase] = None

    class Config:
        orm_mode = True