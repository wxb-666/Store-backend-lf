
from decimal import Decimal

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.product import ProductListApiResponse
from app.services.product_service import get_product_list_service


router = APIRouter(
    prefix="/products",
    tags=["商品管理"],
)


@router.get(
    "",
    response_model=ProductListApiResponse,
    summary="获取商品 SPU 列表",
)
def get_product_list(
    db: Session = Depends(get_db),

    page: int = Query(default=1, ge=1, description="页码"),
    page_size: int = Query(default=20, ge=1, description="每页数量"),

    q: str | None = Query(
        default=None,
        description="关键词，可匹配商品名称、Slug 或 SPU",
    ),

    domain: str | None = Query(
        default=None,
        description="店铺域名",
    ),

    min_price: Decimal | None = Query(
        default=None,
        ge=0,
        description="最低商品价格",
    ),

    max_price: Decimal | None = Query(
        default=None,
        ge=0,
        description="最高商品价格",
    ),

    tag_id: int | None = Query(
        default=None,
        description="商品标签 ID",
    ),
):
    # 1. 校验价格范围
    if (
        min_price is not None
        and max_price is not None
        and min_price > max_price
    ):
        raise HTTPException(
            status_code=422,
            detail="最低价格不能大于最高价格",
        )

    # 2. 调用 Service 层，获取商品列表
    result = get_product_list_service(
        db=db,
        page=page,
        page_size=page_size,
        q=q,
        domain=domain,
        min_price=min_price,
        max_price=max_price,
        tag_id=tag_id,
    )

    # 3. 返回 API 响应
    return result