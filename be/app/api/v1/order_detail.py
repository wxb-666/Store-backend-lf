from fastapi import APIRouter, Depends, Path, Query
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.order_detail import OrderDetailApiResponse
from app.services.order_detail_service import get_order_detail_service


router = APIRouter(
    prefix="/orders",
    tags=["订单管理"],
)


@router.get(
    "/{order_id}",
    response_model=OrderDetailApiResponse,
    summary="获取订单详情",
)
def get_order_detail(
    order_id: int = Path(..., ge=1, description="订单表 ID"),
    domain: str = Query(..., min_length=1, description="店铺域名"),
    db: Session = Depends(get_db),
):
    return get_order_detail_service(
        db=db,
        order_id=order_id,
        domain=domain,
    )