from fastapi import APIRouter

from . import custom_controller

router = APIRouter()
router.include_router(
    custom_controller.router, prefix="/hello_world", tags=["add_tags_here"]
)
