from fastapi import APIRouter

router = APIRouter(prefix="/api_v1")

from .public import router as public_router
router.include_router(public_router)

from .balance import router as balance_router
router.include_router(balance_router)

from app.api.api_v1.orders import router as orders_router
router.include_router(orders_router)