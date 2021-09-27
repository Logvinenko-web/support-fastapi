
from pydantic import BaseModel


class CategoryModelResponse(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True


class CategoryModel(BaseModel):
    name: str
    icon: str
    path: str

