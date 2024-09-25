import logging

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from datetime import datetime
from src.models.custom_model import CustomModel

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/", response_model=CustomModel, response_class=JSONResponse)
async def get() -> CustomModel:
    response = CustomModel(
        date=datetime.utcnow().isoformat(),
        message="Hello, World!",
    )
    return response
