from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.database.database import get_db
from ..controllers import category
from ..controllers.category import createTab, createExplanation, showExplanation, get_all_explanation, showTabs, createInstruction, get_instructions
from ..schema.categories.schema import CategoryModel, CategoryModelResponse
from ..schema.tabs.schema import TabModel
from ..schema.explanation.schema import ExplanationModel
from ..schema.education.schema import EducationDayModelBase
from ..schema.instruction.schema import InstructionModel
routerCategories = APIRouter(
    prefix="/categories",
    tags=["Category"]
)


@routerCategories.post("", status_code=status.HTTP_201_CREATED)
def create_category(
        request: CategoryModel,
        db: Session = Depends(get_db),
):
    return category.createCategory(request, db)


@routerCategories.get("")
def get_categories(db: Session = Depends(get_db)):
    return category.get_all(db)


@routerCategories.get("/{id}", status_code=200)
def get_category_id(id, db: Session = Depends(get_db)):
    return category.showCategories(id, db)


@routerCategories.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category_id(id, db: Session = Depends(get_db)):
    return category.deleteCategory(id, db)


@routerCategories.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_category_id(id, request: CategoryModel, db: Session = Depends(get_db)):
    return category.updateCategory(id, request, db)



@routerCategories.post("/{category_id}/tabs")
def create_tabs(
        category_id,
        request: TabModel,
        db: Session = Depends(get_db),
):
    return createTab(category_id, request, db)

@routerCategories.post("/{category_id}/tabs/{tab_id}/explanation")
def create_explanation(
        category_id,
        tab_id,
        request: ExplanationModel,
        db: Session = Depends(get_db),
):
    return createExplanation(category_id,tab_id, request, db)


@routerCategories.get("/tabs/", status_code=200)
def get_all_tab(
        db: Session = Depends(get_db),
):
    return showTabs( db)




@routerCategories.get("/{category_id}/tabs/explanation")
def show_explanation(
        category_id,
        db: Session = Depends(get_db),
):
    return showExplanation(category_id, db)

@routerCategories.get("/tabs/explanation")
def get_explanation(db: Session = Depends(get_db)):
    return get_all_explanation(db)

@routerCategories.post("/{category_id}/tabs/{tab_id}/instruction")
def create_instruction(
        category_id,
        tab_id,
        request: InstructionModel,
        db: Session = Depends(get_db),
):
    return createInstruction(category_id,tab_id, request, db)

@routerCategories.get("/tabs/instructions")
def get_all_instructions(db: Session = Depends(get_db)):
    return get_instructions(db)

