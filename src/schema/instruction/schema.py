
from pydantic import BaseModel

class InstructionModel(BaseModel):
    name: str
    link: str

    class Config:
        orm_mode = True


