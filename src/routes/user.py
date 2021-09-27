from fastapi import APIRouter, Depends, status

from src.schema.user.schema import UserModel
from sqlalchemy.orm import Session
from src.database.database import get_db
from src.database.models.models import User
from ..security.password import Hash

routerUser = APIRouter(
    tags=["User"]
)


@routerUser.post("/signin", status_code=status.HTTP_201_CREATED)
def create_user(
        request: UserModel,
        db: Session = Depends(get_db),
):
    new_user = User(
        login=request.login,
        password=Hash.bcrypt(request.passsword)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# @router.get("/get")
# def get_users(id= int, db: Session = Depends(get_db)):
#     return db.query(User).filter(User.id == id).first()
