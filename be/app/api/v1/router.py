from fastapi import APIRouter

from app.api.v1 import orders


router = APIRouter()

# 注册路由
router.include_router(orders.router)