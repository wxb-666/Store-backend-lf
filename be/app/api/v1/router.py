from fastapi import APIRouter

from app.api.v1 import orders, order_detail


router = APIRouter()

# 注册路由
router.include_router(orders.router)
router.include_router(order_detail.router)