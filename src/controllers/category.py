from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from src.database.models.models import Categories, Tabs, Education_Days, Explanation, Instructions

#
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


def createTab(id, request, db: Session):
    new_tab = Tabs(
        category_id=id,
        name=request.name
    )
    db.add(new_tab)
    db.commit()
    db.refresh(new_tab)
    return new_tab


def createExplanation(category_id, tab_id, request, db: Session):
    new_explanation = Explanation(
        category_id=category_id,
        tab_id=tab_id,
        description=request.description
    )
    db.add(new_explanation)
    db.commit()
    db.refresh(new_explanation)
    return new_explanation



def showTabs(db: Session):
    tabs = db.query(Tabs).all()
    return tabs


def showExplanation(category_id: str, db: Session):
    explanation = db.query(Explanation) \
        .filter(Explanation.category_id == category_id) \
        .all()
    if not explanation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f" {id} is not available")
    return explanation


def get_all_explanation(db: Session):
    get_explanation = db.query(Explanation).all()
    return get_explanation


def createInstruction(category_id, tab_id, request, db: Session):
    new_instruction = Instructions(
        category_id=category_id,
        tab_id=tab_id,
        name=request.name,
        link=request.link,
    )
    db.add(new_instruction)
    db.commit()
    db.refresh(new_instruction)
    return new_instruction

def get_instructions(db: Session):
    get_instruction = db.query(Instructions).all()
    return get_instruction