from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from ..database.models.models import User
from ..security.password import hash_password


def create(request: User, db:Session):
    new_user = User(name=request.name, password=hash_password(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id:str, db:Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user