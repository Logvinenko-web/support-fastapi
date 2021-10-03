from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from src.database.models.models import Categories, Documentations, Education_Days


def get_all(db: Session):
    categories = db.query(Categories).all()
    return categories


def createCategory(request, db: Session):
    new_category = Categories(
        name=request.name,
        icon=request.icon,
        path=request.path,
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


def deleteCategory(id: str, db: Session):
    category = db.query(Categories).filter(Categories.id == id)
    if not category.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Category with id {id} not found")

    category.delete(synchronize_session=False)
    db.commit()
    return 'done'


def updateCategory(id: str, request, db: Session):
    category = db.query(Categories).filter(Categories.id == id)
    if not category.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Category with id {id} not found")
    category.update({
            "name": request.name,
            "icon": request.icon,
            "path": request.path
})
    db.commit()
    return 'upgrade'


def showCategories(id: str, db: Session):
    category = db.query(Categories).filter(Categories.id == id).first()
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Category with the id {id} is not available")
    return category


def createDocumentation(id, request, db: Session):
    new_doc = Documentations(
        category_id=id,
        description=request.description
    )
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    return new_doc


def showDocumentations(id: str, db: Session):
    doc = db.query(Documentations).filter(Documentations.category_id == id).all()
    if not doc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Documentation with the id {id} is not available")
    return doc




