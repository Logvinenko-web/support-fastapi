
from pydantic import BaseModel

class ExplanationModel(BaseModel):
    description: str

    class Config:
        orm_mode = True


