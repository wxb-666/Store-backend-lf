from datetime import date, datetime, time, timedelta

from sqlalchemy import select, func, or_
from sqlalchemy.orm import Session

from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product import Product


# 定义允许使用的排序字段
SORT_COLUMNS = {
    "payment_time": Order.payment_time,
    "generation_time": Order.generation_time,
    "total_amount": Order.total_amount,
    "order_number": Order.order_number,
}


# 获取订单列表
def get_order_list(
    db: Session,
    page: int = 1,
    page_size: int = 20,
    start_date: date | None = None,
    end_date: date | None = None,
    country_region: str | None = None,
    payment_method: str | None = None,
    payment_status: str | None = None,
    domain: str | None = None,
    q: str | None = None,
    sort_by: str = "payment_time",
    sort_order: str = "desc",
):
    #  构建查询条件
    filters = []

    # 支付时间：开始日期（包括当天）
    if start_date:
        start_datetime = datetime.combine(start_date, time.min)
        filters.append(Order.payment_time >= start_datetime)

    # 支付时间：结束日期（包括当天）
    if end_date:
        end_datetime = datetime.combine(
            end_date + timedelta(days=1),
            time.min
        )
        filters.append(Order.payment_time < end_datetime)

    if country_region:
        filters.append(Order.country_region == country_region)

    if payment_method:
        filters.append(Order.payment_method == payment_method)

    if payment_status:
        filters.append(Order.payment_status == payment_status)

    if domain:
        filters.append(Order.domain == domain)

    # 订单编号或商品 slug 搜索
    if q:
        product_exists = (
            select(1)
            .select_from(OrderItem)
            .join(
                Product,
                OrderItem.product_sku == Product.product_sku
            )
            .where(
                OrderItem.order_number == Order.order_number,
                Product.product_slug.is_not(None),
                Product.product_slug.contains(q, autoescape=True)
            )
            .exists()
        )

        filters.append(
            or_(
                Order.order_number.contains(q, autoescape=True),
                product_exists
            )
        )

    # 查询符合条件的订单总数
    count_statement = (
        select(func.count())
        .select_from(Order)
        .where(*filters)
    )

    total = db.scalar(count_statement) or 0

    # 检查排序字段
    sort_column = SORT_COLUMNS.get(sort_by)

    if sort_column is None:
        raise ValueError(f"不支持的排序字段：{sort_by}")

    if sort_order not in ("asc", "desc"):
        raise ValueError(f"不支持的排序方向：{sort_order}")

    if sort_order == "asc":
        order_by = sort_column.asc()
    else:
        order_by = sort_column.desc()

    # 分页查询订单
    offset = (page - 1) * page_size

    order_statement = (
        select(Order)
        .where(*filters)
        .order_by(order_by, Order.order_id.desc())
        .offset(offset)
        .limit(page_size)
    )

    orders = db.scalars(order_statement).all()

    # 查询当前页订单对应的商品明细
    product_items_map = {}

    if orders:
        order_numbers = [order.order_number for order in orders]

        item_statement = (
            select(OrderItem, Product)
            .join(
                Product,
                OrderItem.product_sku == Product.product_sku
            )
            .where(OrderItem.order_number.in_(order_numbers))
            .order_by(OrderItem.id.asc())
        )

        item_results = db.execute(item_statement).all()

        # 按订单编号整理商品明细
        for order_item, product in item_results:
            product_items_map.setdefault(
                order_item.order_number,
                []
            ).append((order_item, product))

    # 返回查询结果
    return orders, total, product_items_map
