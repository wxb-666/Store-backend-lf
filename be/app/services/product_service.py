from sqlalchemy.orm import Session
from decimal import Decimal
from app.repositories.product_repository import get_product_list as get_product_list_repo

from app.schemas.product import (
    ProductListApiResponse,
    ProductListDataResponse,
    ProductSpuListItemResponse,
    ProductTagResponse,
)


# 获取商品 SPU 列表
def get_product_list_service(
    db: Session,
    page: int = 1,
    page_size: int = 20,
    q: str | None = None,
    domain: str | None = None,
    min_price: Decimal | None = None,
    max_price: Decimal | None = None,
    tag_id: int | None = None,
    is_listed: int | None = None,
) -> ProductListApiResponse:

    # 1. 调用 Repository 层，查询商品数据
    products, total, product_tags_map = get_product_list_repo(
        db=db,
        page=page,
        page_size=page_size,
        q=q,
        domain=domain,
        min_price=min_price,
        max_price=max_price,
        tag_id=tag_id,
        is_listed=is_listed,
    )

    # 2. 整理当前页的商品数据
    product_list = []

    for product in products:

        # 获取当前 SPU 关联的全部标签
        product_tags = product_tags_map.get(
            product.product_id,
            []
        )

        # 将标签数据转换为响应模型
        tag_list = [
            ProductTagResponse(**tag)
            for tag in product_tags
        ]

        # 整理当前商品的信息
        product_response = ProductSpuListItemResponse(
            product_id=product.product_id,
            domain=product.domain,
            product_spu=product.product_spu,
            product_name=product.product_name,
            product_slug=product.product_slug,
            product_price=str(product.product_price),
            currency_code=product.currency_code,
            product_stock=product.product_stock,
            is_listed=product.is_listed,
            product_image=product.product_image,
            tags=tag_list,
        )

        product_list.append(product_response)

    # 3. 组装完整的 API 响应结构
    data_response = ProductListDataResponse(
        total=total,
        page=page,
        page_size=page_size,
        items=product_list,
    )

    return ProductListApiResponse(
        code=200,
        message="success",
        data=data_response,
    )
