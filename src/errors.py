import logging

from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.responses import JSONResponse

logger = logging.getLogger(__name__)


async def custom_http_exception_handler(request, exc) -> JSONResponse:
    logger.error(
        "HTTP Error caused - %r",
        exc,
    )
    headers = getattr(exc, "headers", None)
    if headers:
        return JSONResponse({"message": exc.detail}, status_code=exc.status_code, headers=headers)
    else:
        return JSONResponse({"message": exc.detail}, status_code=exc.status_code)


async def validation_exception_handler(request, exc) -> JSONResponse:
    logger.error(
        "Validation error caused - %r",
        exc,
        request_id=request.scope["request_id"],
    )
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": jsonable_encoder(exc.errors()), "message": "Validation error"},
    )


async def custom_exception_handler(request, exc) -> JSONResponse:
    logger.critical(
        "Critical server error - %s: %s",
        type(exc).__name__,
        str(exc),
        exc_info=True,
    )
    return JSONResponse(status_code=500, content={"message": "Internal Server Error"})
