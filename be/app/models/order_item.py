
from sqlalchemy import BigInteger, String, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class OrderItem(Base):
    """订单明细表 ORM 模型"""

    __tablename__ = "order_items"

    # 同一订单中的同一个 SKU 只保留一条明细
    __table_args__ = (
        UniqueConstraint(
            "order_number",
            "product_sku",
            name="uq_order_number_product_sku"
        ),
    )

    # 明细 ID：主键，自增
    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
        comment="订单明细ID"
    )

    # 订单编号：外键，关联 order 表
    order_number: Mapped[str] = mapped_column(
        String(64),
        ForeignKey("orders.order_number"),
        nullable=False,
        comment="订单编号"
    )

    # 商品 SKU：外键，关联 product 表
    product_sku: Mapped[str] = mapped_column(
        String(64),
        ForeignKey("products.product_sku"),
        nullable=False,
        comment="商品SKU"
    )

    # 商品数量
    product_number: Mapped[int] = mapped_column(
        INTEGER(unsigned=True),
        nullable=False,
        comment="商品数量"
    )
