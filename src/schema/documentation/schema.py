from typing import Optional

from pydantic import BaseModel
from uuid import UUID


class  DocumentationModelBase(BaseModel):
    id: Optional[UUID]
    description: str

    class Config:
        orm_mode = True