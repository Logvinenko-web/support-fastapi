from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.database.database import get_db
from ..controllers import category
from ..controllers.category import createDocumentation, showDocumentations
from ..schema.categories.schema import CategoryModel, CategoryModelResponse
from ..schema.documentation.schema import DocumentationModelBase

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


@routerCategories.get("",
                      # response_model=List[CategoryModelResponse]
                      )
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



@routerCategories.post("/{id}/documentation")
def create_documentation(
        id,
        request: DocumentationModelBase,
        db: Session = Depends(get_db),
):
    return createDocumentation(id, request, db)


@routerCategories.get("/{id}/documentations")
def get_documentations(id, db: Session = Depends(get_db)):
    return showDocumentations(id, db)

# @routerCategories.get("/categories/{category_id}/documentations/{documentation_id}")
# def get_documentation_id(uuid, db: Session = Depends(get_db)):
#     return
