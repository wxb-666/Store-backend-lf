from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    BigInteger,
    String,
    DateTime,
    Numeric,
    Text,
    Integer,
    func,
)
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import Mapped, mapped_column

# 导入基类
from app.database.connection import Base


class Order(Base):
    """订单表"""

    __tablename__ = "orders"

    # ==================== 基础订单信息 ====================

    order_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
        comment="订单ID"
    )

    order_number: Mapped[str] = mapped_column(
        String(64),
        unique=True,
        nullable=False,
        comment="订单编号"
    )

    order_status: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        index=True,
        comment="订单状态"
    )

    generation_time: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now(),
        index=True,
        comment="订单生成时间"
    )

    # ==================== 支付信息 ====================

    payment_time: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
        comment="订单支付时间"
    )

    payment_status: Mapped[str | None] = mapped_column(
        String(32),
        nullable=True,
        comment="支付状态"
    )

    payment_method: Mapped[str | None] = mapped_column(
        String(64),
        nullable=True,
        comment="支付方式"
    )

    payment_number: Mapped[str | None] = mapped_column(
        String(128),
        nullable=True,
        comment="支付流水号或第三方支付交易编号"
    )

    total_amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        default=Decimal("0.00"),
        comment="订单总金额"
    )

    currency_code: Mapped[str] = mapped_column(
        String(3),
        nullable=False,
        comment="货币代码，例如USD、EUR、CNY"
    )

    # ==================== 物流信息 ====================

    logistic_order_number: Mapped[str | None] = mapped_column(
        String(128),
        nullable=True,
        comment="物流单号"
    )

    logistics_status: Mapped[str | None] = mapped_column(
        String(32),
        nullable=True,
        comment="物流状态"
    )

    # ==================== 客户及收货信息 ====================

    customer_name: Mapped[str | None] = mapped_column(
        String(128),
        nullable=True,
        comment="客户姓名或收件人姓名"
    )

    address: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        comment="收货地址"
    )

    apartment: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        comment="公寓、套房或单元号"
    )

    city: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
        comment="城市"
    )

    country_region: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
        comment="国家或地区"
    )

    province_state: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
        comment="省份或州"
    )

    postcode: Mapped[str | None] = mapped_column(
        String(32),
        nullable=True,
        comment="邮政编码"
    )

    phone: Mapped[str | None] = mapped_column(
        String(32),
        nullable=True,
        comment="联系电话"
    )

    mailbox: Mapped[str | None] = mapped_column(
        String(254),
        nullable=True,
        comment="客户邮箱"
    )

    # ==================== 其他订单信息 ====================

    extra_information: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
        comment="订单补充信息或客户备注"
    )

    domain: Mapped[str | None] = mapped_column(
        String(64),
        nullable=True,
        comment="域名"
    )

    number_of_products: Mapped[int] = mapped_column(
        INTEGER(unsigned=True),
        nullable=False,
        default=0,
        comment="订单包含的商品总件数"
    )
