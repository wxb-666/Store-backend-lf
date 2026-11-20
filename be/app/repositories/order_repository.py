from datetime import date, datetime, time, timedelta

from sqlalchemy import select, func, or_
from sqlalchemy.orm import Session

# 引入定义好的数据模型
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product import Product

# 定义排序字段
SORT_COLUMNS = {
    "payment_time": Order.payment_time,
    "generated_time": Order.generation_time,
    "total_amount": Order.total_amount,
    "order_number": Order.order_number,
}

# 函数1：获取订单列表
# 返回值：orders（当前页的订单 ORM 对象列表）， total（符合筛选条件的订单总数），product_items_map（按订单编号整理的商品明细）
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
    q: str | None = None,  # 搜索关键字
    sort_by: str = "payment_time",
    sort_order: str = "desc",
):
    # 构建查询条件
    filters = []

    # 支付时间——开始时间（包括当天）
    if start_date:
        start_datetime = datetime.combine(start_date, time.min)
        filters.append(Order.payment_time >= start_datetime)

    # 支付时间——结束时间（包括当天）
    if end_date:
        end_datetime = datetime.combine(
            end_date + timedelta(days=1),  # 由于是右闭包，所以需要加一天 
            time.min
        )
        filters.append(Order.payment_time < end_datetime)

    if country_region:
        filters.append(Order.country_regin == country_region)

    if payment_method:
        filters.append(Order.payment_method == payment_method)

    if payment_status:
        filters.append(Order.payment_status == payment_status)
    
    if domain:
        filters.append(Order.domain == domain)

    # 搜索关键字
    if q:
        # 查询订单明细表中是否存在匹配的商品 slug 的商品
        product_exists = (
            select(1)
            .select_from(OrderItem)
            .join(
                Product,  # 关联 Product 表
                OrderItem.product_sku == Product.product_sku  # 关联条件
            )
            .where(
                OrderItem.order_number == Order.order_number,  # 关联到外层 order 表
                Product.product_slug.is_not(None),   # 商品 slug 不为空
                Product.product_slug.contains(q, autoescape = True)  # 使用模糊匹配 slug，只要 slug 包含关键字 q 就匹配
            )
            .exists()
        )

        # 订单编号 或 商品slug 有一个匹配即可
        # 简单来说，只要订单编号包含关键字 q，或者订单明细中有商品的 slug 包含关键字 q，就会匹配到该订单
        filters.append(
            or_(
                Order.order_number.contains(q, autoescape=True),  # 订单编号模糊匹配，只要包含关键字 q 就匹配
                product_exists  # 商品 slug 匹配
            )
        )

        # 查询符合条件的订单条数
        count_statement = (
            select(func.count())
            .select_from(Order)
            .where(*filters)  # 需要满足所有的筛选条件的订单
        )
        
        total = db.scalar(count_statement) or 0  # 执行查询，获取符合条件的订单总数，如果没有符合条件的订单，则 total 为 0

        # 排序
        sort_column = SORT_COLUMNS.get(sort_by, Order.payment_time)  # 获取排序字段，如果没有指定排序字段，则默认按支付时间排序

        if sort_order not in ("asc", "desc"):
            raise ValueError(f"不支持指定的排序方向：{sort_order}, 仅支持 asc 和 desc! ") 
        
        if sort_order == "asc":
            order_by = sort_column.asc()  # 升序排序
        else:
            order_by = sort_column.desc()  # 降序排序 

        # 分页查询订单
        offset = (page - 1) * page_size  # 计算页面偏移量

        order_statement = (
            select(Order)
            .where(*filters)  # 查询出满足所有条件的订单
            .order_by(order_by, Order.order_id.desc())
            .offset(offset)
            .limit(page_size)
        )

        orders = db.scalars(order_statement).all()

        # 查询当前页订单对应的商品明细

        product_item_map = {}

    # 当前页存在订单时，才查询商品明细
    if orders:
        order_numbers = [order.order_number for order in orders]

        item_statement = {
            select(OrderItem, Product)
            .join(
                Product,
                OrderItem.product_sku == Product.product_sku
            )
            .where(OrderItem.order_number.in_(order_numbers))
            .order_by(OrderItem.id.asc())
        }

        item_results = db.execute(item_statement).all()

        # 按订单编号整理商品明细
        for order_item, product in item_results:
            product_item_map.setdefault(
                order_item.order_number,
                []
            ).append((order_item, product))

    return orders, total, product_item_map