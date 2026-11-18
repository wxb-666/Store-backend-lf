from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class ProductTag(Base):
    """商品标签表 ORM 模型"""

    __tablename__ = "product_tags"

    # 标签 ID：主键，自增
    tag_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
        comment="标签ID"
    )

    # 标签名称
    tag_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        comment="标签名称"
    )
