from pydantic import BaseModel


class TaskModelBase(BaseModel):
    description: str
    status: str
    title: str

    class Config:
        orm_mode = True