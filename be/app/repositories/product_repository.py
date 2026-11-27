
from decimal import Decimal

from sqlalchemy import select, func, or_
from sqlalchemy.orm import Session

from app.models.product_spu import ProductSpu
from app.models.product_tag import ProductTag
from app.models.product_tag_relation import ProductTagRelation


# 获取商品 SPU 列表
def get_product_list(
    db: Session,
    page: int = 1,
    page_size: int = 20,
    q: str | None = None,
    domain: str | None = None,
    min_price: Decimal | None = None,
    max_price: Decimal | None = None,
    tag_id: int | None = None,
    is_listed: int | None = None,
):
    # 1. 构建查询条件
    filters = []

    # 关键词：匹配商品名称、Slug、SPU
    if q:
        q = q.strip()

        if q:
            filters.append(
                or_(
                    ProductSpu.product_name.contains(
                        q,
                        autoescape=True
                    ),
                    ProductSpu.product_slug.contains(
                        q,
                        autoescape=True
                    ),
                    ProductSpu.product_spu.contains(
                        q,
                        autoescape=True
                    )
                )
            )

    # 店铺域名：精确匹配
    if domain:
        filters.append(ProductSpu.domain == domain.strip())

    # 最低价格：包含边界值
    if min_price is not None:
        filters.append(ProductSpu.product_price >= min_price)

    # 最高价格：包含边界值
    if max_price is not None:
        filters.append(ProductSpu.product_price <= max_price)

    # 标签筛选：只筛选关联了指定标签的 SPU
    if tag_id is not None:
        tag_exists = (
            select(1)
            .select_from(ProductTagRelation)
            .where(
                ProductTagRelation.product_id == ProductSpu.product_id,
                ProductTagRelation.tag_id == tag_id
            )
            .exists()
        )

        filters.append(tag_exists)

    # 商品上架状态筛选
    if is_listed is not None:
        filters.append(ProductSpu.is_listed == is_listed)

    # 2. 查询符合条件的商品总数
    count_statement = (
        select(func.count())
        .select_from(ProductSpu)
        .where(*filters)
    )

    total = db.scalar(count_statement) or 0

    # 3. 分页查询商品 SPU
    offset = (page - 1) * page_size

    product_statement = (
        select(ProductSpu)
        .where(*filters)
        .order_by(ProductSpu.product_id.desc())
        .offset(offset)
        .limit(page_size)
    )

    products = db.scalars(product_statement).all()

    # 4. 查询当前页商品关联的全部标签
    product_tags_map = {}

    if products:
        product_ids = [
            product.product_id
            for product in products
        ]

        tag_statement = (
            select(
                ProductTagRelation.product_id,
                ProductTag.tag_id,
                ProductTag.tag_name
            )
            .join(
                ProductTag,
                ProductTagRelation.tag_id == ProductTag.tag_id
            )
            .where(
                ProductTagRelation.product_id.in_(product_ids)
            )
            .order_by(
                ProductTagRelation.product_id.asc(),
                ProductTag.tag_id.asc()
            )
        )

        tag_results = db.execute(tag_statement).all()

        # 按 SPU ID 整理标签
        for product_id, tag_id, tag_name in tag_results:
            product_tags_map.setdefault(product_id, []).append(
                {
                    "tag_id": tag_id,
                    "tag_name": tag_name
                }
            )

    # 5. 返回查询结果
    return products, total, product_tags_map