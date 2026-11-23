from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel

# 引入已经定义好的订单商品明细
from app.schemas.order_item import OrderDetailProductResponse


class OrderDetailOrderInfoResponse(BaseModel):
    # 订单基本信息
    order_id: int
    order_number: str
    domain: str
    order_status: str
    generation_time: datetime
    total_amount: Decimal
    currency_code: str
    number_of_products: int


class OrderDetailPaymentInfoResponse(BaseModel):
    # 订单支付信息
    payment_status: str | None
    payment_method: str | None
    payment_time: datetime | None
    payment_number: str | None


class OrderDetailCustomerInfoResponse(BaseModel):
    # 客户及收货信息
    customer_name: str | None
    mailbox: str | None
    phone: str | None
    country_region: str | None
    province_state: str | None
    city: str | None
    address: str | None
    apartment: str | None
    postcode: str | None
    extra_information: str | None


class OrderDetailLogisticsInfoResponse(BaseModel):
    # 订单物流信息
    logistics_status: str | None
    logistic_order_number: str | None


class OrderDetailDataResponse(BaseModel):
    # 订单详情 API 的 data 字段
    order_info: OrderDetailOrderInfoResponse
    payment_info: OrderDetailPaymentInfoResponse
    customer_info: OrderDetailCustomerInfoResponse
    logistics_info: OrderDetailLogisticsInfoResponse
    order_items: list[OrderDetailProductResponse]


class OrderDetailApiResponse(BaseModel):
    # 订单详情 API 的完整响应
    code: int
    message: str
    data: OrderDetailDataResponse
