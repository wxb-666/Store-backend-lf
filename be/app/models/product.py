from decimal import Decimal

from sqlalchemy import BigInteger, String, Numeric
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class Product(Base):
    """商品表 ORM 模型"""

    __tablename__ = "products"

    __table_args__ = (
        UniqueConstraint(
            "domain",
            "product_sku",
            name="uq_domain_product_sku"
        ),
    )

    product_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
        comment="商品ID"
    )

    # 店铺域名
    domain: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        comment="店铺域名"
    )

    product_sku: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        comment="商品SKU"
    )

    product_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment="商品名称"
    )

    product_slug: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        comment="商品Slug"
    )

    product_price: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        default=Decimal("0.00"),
        comment="商品金额"
    )

    product_stock: Mapped[int] = mapped_column(
        INTEGER(unsigned=True),
        nullable=False,
        default=0,
        comment="商品库存"
    )

    specifications: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        comment="商品规格"
    )

    product_image: Mapped[str | None] = mapped_column(
        String(2048),
        nullable=True,
        comment="商品图片链接"
    )
