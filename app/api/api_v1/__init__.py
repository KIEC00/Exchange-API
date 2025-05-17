from fastapi import APIRouter

from .public import router as public_router
from .user import router as user_router


router = APIRouter(prefix="/api_v1")

router.include_router(public_router)
router.include_router(user_router)
