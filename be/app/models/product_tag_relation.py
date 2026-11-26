from sqlalchemy import BigInteger, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class ProductTagRelation(Base):
    """商品标签关联表 ORM 模型"""

    __tablename__ = "product_tag_relations"

    __table_args__ = (
        UniqueConstraint(
            "product_id",
            "tag_id",
            name="uq_product_id_tag_id"
        ),
    )

    # 关联 ID：主键，自增
    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
        comment="关联ID"
    )

    # 商品 SPU ID：关联 products_spu 表
    product_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("products_spu.product_id"),
        nullable=False,
        comment="商品SPU ID"
    )

    # 标签 ID：关联 product_tags 表
    tag_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("product_tags.tag_id"),
        nullable=False,
        comment="标签ID"
    )
