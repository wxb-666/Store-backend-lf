from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal

# 从 order_item.py 中导入 OrderListProductResponse
from app.schemas.order_item import OrderListProductResponse

class OrderListResponse(BaseModel):
    # 订单列表中单个订单的响应数据模型，items 字段中的每个元素都是这个模型的实例

    order_id: int
    order_number: str
    payment_time: datetime | None
    payment_status: str | None
    payment_method: str | None
    logistics_status: str
    total_amount: Decimal
    currency_code: str
    number_of_products: int

    product_items: list[OrderListProductResponse]  # 使用导入的 OrderListProductResponse 模型

    domain: str
    country_region: str

class OrderListDataResponse(BaseModel):
    # 订单列表 api 的 data 字段响应数据模型

    total: int
    page: int
    page_size: int
    items: list[OrderListResponse]  # 使用 OrderListResponse 模型

class OrderListApiResponse(BaseModel):
    # 订单列表 api 的响应数据模型

    code: int
    message: str
    data: OrderListDataResponse  # 使用 OrderListDataResponse 模型