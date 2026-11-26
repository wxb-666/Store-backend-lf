
from decimal import Decimal

from sqlalchemy import (
    BigInteger,
    String,
    Numeric,
    UniqueConstraint,
)
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class ProductSpu(Base):
    """商品 SPU 表 ORM 模型"""

    __tablename__ = "products_spu"

    __table_args__ = (
        # 同一个店铺下，SPU 不能重复
        UniqueConstraint(
            "domain",
            "product_spu",
            name="uq_domain_product_spu"
        ),
    )

    # SPU ID：主键，自增
    product_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
        comment="SPU ID"
    )

    # 店铺域名
    domain: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        comment="店铺域名"
    )

    # 商品 SPU
    product_spu: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        comment="商品SPU"
    )

    # 商品名称
    product_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment="商品名称"
    )

    # 商品 Slug
    product_slug: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        comment="商品Slug"
    )

    # 商品金额
    product_price: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        default=Decimal("0.00"),
        comment="商品金额"
    )

    currency_code: Mapped[str] = mapped_column(
        String(3),
        nullable=False,
        comment="货币代码"
    )

    # 商品库存
    product_stock: Mapped[int] = mapped_column(
        INTEGER(unsigned=True),
        nullable=False,
        default=0,
        comment="商品库存"
    )

    # 商品图片
    product_image: Mapped[str | None] = mapped_column(
        String(2048),
        nullable=True,
        comment="商品图片链接"
    )
