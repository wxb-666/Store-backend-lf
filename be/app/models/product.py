from decimal import Decimal

from sqlalchemy import BigInteger, String, Numeric
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class Product(Base):
    """商品表 ORM 模型"""

    __tablename__ = "products"

    # 商品 ID：主键，自增
    product_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
        comment="商品ID"
    )

    # 商品 SKU：唯一，不允许为空
    product_sku: Mapped[str] = mapped_column(
        String(64),
        unique=True,
        nullable=False,
        comment="商品SKU"
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

    # 商品价格
    product_price: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        default=Decimal("0.00"),
        comment="商品金额"
    )

    # 商品库存：MySQL 无符号 INT
    product_stock: Mapped[int] = mapped_column(
        INTEGER(unsigned=True),
        nullable=False,
        default=0,
        comment="商品库存"
    )

    # 商品规格
    specifications: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        comment="商品规格"
    )

    # 商品图片链接
    product_image: Mapped[str | None] = mapped_column(
        String(2048),
        nullable=True,
        comment="商品图片链接"
    )
