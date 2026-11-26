
from sqlalchemy import (
    BigInteger,
    String,
    ForeignKeyConstraint,
    UniqueConstraint,
)
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class OrderItem(Base):
    """订单明细表 ORM 模型"""

    __tablename__ = "order_items"

    __table_args__ = (
        # 同一店铺、同一订单中的同一个 SKU 只保留一条明细
        UniqueConstraint(
            "domain",
            "order_number",
            "product_sku",
            name="uq_domain_order_number_product_sku"
        ),

        # domain + order_number 联合外键，关联订单表
        ForeignKeyConstraint(
            ["domain", "order_number"],
            ["orders.domain", "orders.order_number"],
            name="fk_order_item_order"
        ),

        # domain + product_sku 联合外键，关联 SKU 商品表
        ForeignKeyConstraint(
            ["domain", "product_sku"],
            ["products_sku.domain", "products_sku.product_sku"],
            name="fk_order_item_product"
        ),
    )

    # 明细 ID：主键，自增
    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
        comment="订单明细ID"
    )

    # 订单编号
    order_number: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        comment="订单编号"
    )

    # 店铺域名
    domain: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        comment="店铺域名"
    )

    # 商品 SKU
    product_sku: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        comment="商品SKU"
    )

    # 商品数量
    product_number: Mapped[int] = mapped_column(
        INTEGER(unsigned=True),
        nullable=False,
        comment="商品数量"
    )
