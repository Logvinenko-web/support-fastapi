from pydantic import BaseModel


class UserModel(BaseModel):
    login: str
    passsword: str

    class Config:
        orm_mode = True


class Login(UserModel):
    pass
