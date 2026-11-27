
from decimal import Decimal

from pydantic import BaseModel


class ProductTagResponse(BaseModel):
    """商品标签响应模型"""

    tag_id: int
    tag_name: str


class ProductSpuListItemResponse(BaseModel):
    """商品 SPU 列表中单个商品的响应模型"""

    product_id: int
    domain: str
    product_spu: str
    product_name: str
    product_slug: str | None
    product_price: str
    currency_code: str
    product_stock: int | None
    product_image: str | None

    # 当前 SPU 关联的全部标签
    tags: list[ProductTagResponse]


class ProductListDataResponse(BaseModel):
    """商品列表 data 字段响应模型"""

    total: int
    page: int
    page_size: int
    items: list[ProductSpuListItemResponse]


class ProductListApiResponse(BaseModel):
    """商品列表 API 完整响应模型"""

    code: int
    message: str
    data: ProductListDataResponse
