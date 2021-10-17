from typing import Optional

from pydantic import BaseModel
from uuid import UUID

class TabModel(BaseModel):
    name: str

    class Config:
        orm_mode = True


