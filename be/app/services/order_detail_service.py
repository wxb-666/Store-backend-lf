from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.order_detail_repository import (
    get_order_detail as get_order_detail_repo,
)
from app.schemas.order_detail import (
    OrderDetailApiResponse,
    OrderDetailCustomerInfoResponse,
    OrderDetailDataResponse,
    OrderDetailLogisticsInfoResponse,
    OrderDetailOrderInfoResponse,
    OrderDetailPaymentInfoResponse,
)
from app.schemas.order_item import OrderDetailProductResponse


# 获取并组装订单详情
def get_order_detail_service(
    db: Session,
    order_id: int,
    domain: str,
) -> OrderDetailApiResponse:
    # 调用 Repository 层查询订单及商品明细
    result = get_order_detail_repo(
        db=db,
        order_id=order_id,
        domain=domain,
    )

    # 订单不存在，返回 404
    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found!",
        )

    order, order_item_results = result

    # 组装订单商品明细
    order_items = []

    for order_item, product in order_item_results:
        order_item_response = OrderDetailProductResponse(
            id=order_item.id,
            product_id=product.product_id,
            product_name=product.product_name,
            product_number=order_item.product_number,
            product_sku=product.product_sku,
            specifications=product.specifications,
            product_image=product.product_image,
        )

        order_items.append(order_item_response)

    # 组装完整的订单详情响应
    data_response = OrderDetailDataResponse(
        order_info=OrderDetailOrderInfoResponse(
            order_id=order.order_id,
            order_number=order.order_number,
            domain=order.domain,
            order_status=order.order_status,
            generation_time=order.generation_time,
            total_amount=order.total_amount,
            number_of_products=order.number_of_products,
        ),
        payment_info=OrderDetailPaymentInfoResponse(
            payment_status=order.payment_status,
            payment_method=order.payment_method,
            payment_time=order.payment_time,
            payment_number=order.payment_number,
        ),
        customer_info=OrderDetailCustomerInfoResponse(
            customer_name=order.customer_name,
            mailbox=order.mailbox,
            phone=order.phone,
            country_region=order.country_region,
            province_state=order.province_state,
            city=order.city,
            address=order.address,
            apartment=order.apartment,
            postcode=order.postcode,
            extra_information=order.extra_information,
        ),
        logistics_info=OrderDetailLogisticsInfoResponse(
            logistics_status=order.logistics_status,
            logistic_order_number=order.logistic_order_number,
        ),
        order_items=order_items,
    )

    return OrderDetailApiResponse(
        code=200,
        message="success",
        data=data_response,
    )