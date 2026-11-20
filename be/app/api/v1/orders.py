
from datetime import date
from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.order import OrderListApiResponse
from app.services.order_service import get_order_list_service


router = APIRouter(
    prefix="/orders",
    tags=["订单管理"],
)


@router.get(
    "",
    response_model=OrderListApiResponse,
    summary="获取订单列表",
)
def get_order_list(
    db: Session = Depends(get_db),

    page: int = Query(default=1, ge=1, description="页码"),
    page_size: int = Query(default=20, ge=1, description="每页数量"),

    start_date: date | None = Query(default=None, description="开始日期"),
    end_date: date | None = Query(default=None, description="结束日期"),

    country_region: str | None = Query(default=None, description="国家或地区"),
    payment_method: str | None = Query(default=None, description="支付方式"),
    payment_status: str | None = Query(default=None, description="支付状态"),
    domain: str | None = Query(default=None, description="域名"),

    q: str | None = Query(default=None, description="订单编号或商品 slug"),

    sort_by: Literal[
        "payment_time",
        "generation_time",
        "total_amount",
        "order_number",
    ] = Query(default="payment_time", description="排序字段"),

    sort_order: Literal["asc", "desc"] = Query(
        default="desc",
        description="排序方向",
    ),
):
    # 校验日期范围
    if start_date and end_date and start_date > end_date:
        raise HTTPException(
            status_code=422,
            detail="开始日期不能晚于结束日期",
        )

    # 调用 Service 层，获取订单列表
    result = get_order_list_service(
        db=db,
        page=page,
        page_size=page_size,
        start_date=start_date,
        end_date=end_date,
        country_region=country_region,
        payment_method=payment_method,
        payment_status=payment_status,
        domain=domain,
        q=q,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    # 返回 API 响应
    return result
