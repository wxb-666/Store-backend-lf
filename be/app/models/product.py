
from sqlalchemy import (
    BigInteger,
    String,
    UniqueConstraint,
    ForeignKeyConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class Product(Base):
    """商品 SKU 表 ORM 模型"""

    __tablename__ = "products_sku"

    __table_args__ = (
        # 同一个店铺下，SKU 不能重复
        UniqueConstraint(
            "domain",
            "product_sku",
            name="uq_domain_product_sku"
        ),

        # SKU 关联所属 SPU
        ForeignKeyConstraint(
            ["domain", "product_spu"],
            ["products_spu.domain", "products_spu.product_spu"],
            name="fk_product_sku_spu"
        ),
    )

    # SKU ID：主键，自增
    product_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
        comment="SKU ID"
    )

    # 店铺域名
    domain: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        comment="店铺域名"
    )

    # 所属 SPU
    product_spu: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        comment="所属商品SPU"
    )

    # 商品 SKU
    product_sku: Mapped[str] = mapped_column(
        String(64),
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

    # 商品规格
    specifications: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        comment="商品规格"
    )

    # 商品图片
    product_image: Mapped[str | None] = mapped_column(
        String(2048),
        nullable=True,
        comment="商品图片链接"
    )