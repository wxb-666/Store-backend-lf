from sqlalchemy import and_, select
from sqlalchemy.orm import Session

from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product import Product


# 获取订单详情及其商品明细
def get_order_detail(
    db: Session,
    order_id: int,
    domain: str,
):
    # 根据订单 ID 和店铺域名查询订单
    order_statement = select(Order).where(
        Order.order_id == order_id,
        Order.domain == domain,
    )

    order = db.scalar(order_statement)

    # 订单不存在，返回 None
    if order is None:
        return None

    # 查询订单明细，并关联同一店铺下的商品
    item_statement = (
        select(OrderItem, Product)
        .join(
            Product,
            and_(
                OrderItem.domain == Product.domain,
                OrderItem.product_sku == Product.product_sku,
            ),
        )
        .where(
            OrderItem.domain == order.domain,
            OrderItem.order_number == order.order_number,
        )
        .order_by(OrderItem.id.asc())
    )

    item_results = [
        (order_item, product)
        for order_item, product in db.execute(item_statement).all()
    ]

    return order, item_results