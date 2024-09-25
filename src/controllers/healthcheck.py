import logging

from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

logger = logging.getLogger(__name__)
healthcheck_router = APIRouter(include_in_schema=False)


@healthcheck_router.get("", response_class=PlainTextResponse)
async def healthcheck() -> PlainTextResponse:
    return PlainTextResponse(content="Healthy", status_code=200)
