from pydantic import BaseModel

class OrderListProductResponse(BaseModel):
    # 订单列表中的商品信息

    product_id: int
    product_name: str
    product_number: int
    product_sku: str
    product_image: str

class OrderDetailProductResponse(BaseModel):
    # 订单详情中的商品信息

    id: int  # 订单明细表中的id
    product_id: int  # 商品id
    product_name: str 
    product_number: int
    product_sku: str
    product_image: str | None = None
    unit_price: str  # 商品单价，但店铺后台不显示
    quantity: int    # 商品数量，在本订单中的数量