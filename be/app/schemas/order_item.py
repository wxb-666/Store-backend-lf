from decimal import Decimal

from pydantic import BaseModel

class OrderListProductResponse(BaseModel):
    # 订单列表中的商品信息

    product_id: int
    product_name: str
    product_number: int
    product_sku: str
    product_image: str | None = None

class OrderDetailProductResponse(BaseModel):
    # 订单详情中的商品信息

    id: int  # 订单明细表中的id
    product_id: int  # 商品id
    product_name: str 
    product_number: int
    product_sku: str
    product_price: Decimal
    specifications: str | None = None
    product_image: str | None = None
