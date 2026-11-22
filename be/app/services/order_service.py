
from datetime import date

from sqlalchemy.orm import Session

from app.repositories.order_repository import get_order_list as get_order_list_repo

from app.schemas.order import (
    OrderListApiResponse,
    OrderListDataResponse,
    OrderListResponse,
)

from app.schemas.order_item import OrderListProductResponse


def get_order_list_service(
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
) -> OrderListApiResponse:

    # 调用 Repository 层，查询订单数据
    orders, total, product_items_map = get_order_list_repo(
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

    # 整理当前页的订单数据
    order_list = []

    for order in orders:

        # 获取当前订单对应的商品明细
        order_items = product_items_map.get((order.domain, order.order_number), [])[:3]

        # 整理当前订单的商品信息
        product_list = []

        for order_item, product in order_items:
            product_response = OrderListProductResponse(
                product_id=product.product_id,
                product_name=product.product_name,
                product_number=order_item.product_number,
                product_sku=product.product_sku,
                product_image=product.product_image,
            )

            product_list.append(product_response)

        # 整理当前订单的信息
        order_response = OrderListResponse(
            order_id=order.order_id,
            order_number=order.order_number,
            payment_time=order.payment_time,
            payment_status=order.payment_status,
            payment_method=order.payment_method,
            logistics_status=order.logistics_status,
            total_amount=order.total_amount,
            currency_code=order.currency_code,
            number_of_products=order.number_of_products,
            product_items=product_list,
            domain=order.domain,
            country_region=order.country_region,
        )

        order_list.append(order_response)

    # 组装完整的 API 响应结构
    data_response = OrderListDataResponse(
        total=total,
        page=page,
        page_size=page_size,
        items=order_list,
    )

    return OrderListApiResponse(
        code=200,
        message="success",
        data=data_response,
    )
