from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from fastapi.middleware.cors import CORSMiddleware

from src.errors import custom_http_exception_handler, validation_exception_handler, custom_exception_handler
from src.routes.authentication import router
from src.routes.categories import routerCategories
from src.routes.tasks import routerTasks
from src.routes.education import routerEducations

from src.routes.user import routerUser
from starlette.exceptions import HTTPException as StarletteHTTPException
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)
app.include_router(routerUser)
app.include_router(routerCategories)
app.include_router(routerTasks)
app.include_router(routerEducations)




app.add_exception_handler(StarletteHTTPException, custom_http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, custom_exception_handler)

