"""增加店铺约束，也就是加 domain 字段

Revision ID: 0f1ad2b3f96d
Revises: a8fea4661e3d
Create Date: 2026-11-20 13:40:05.277804

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f1ad2b3f96d'
down_revision: Union[str, Sequence[str], None] = 'a8fea4661e3d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    # 删除订单明细表原来的单列外键
    op.drop_constraint(
        op.f('order_items_ibfk_1'),
        'order_items',
        type_='foreignkey'
    )

    op.drop_constraint(
        op.f('order_items_ibfk_2'),
        'order_items',
        type_='foreignkey'
    )

    # 删除原来的单列唯一索引
    op.drop_index(
        op.f('uq_order_number_product_sku'),
        table_name='order_items'
    )

    op.drop_index(
        op.f('order_number'),
        table_name='orders'
    )

    op.drop_index(
        op.f('product_sku'),
        table_name='products'
    )

    # 商品表增加 domain 字段
    op.add_column(
        'products',
        sa.Column(
            'domain',
            sa.String(length=64),
            nullable=False,
            comment='店铺域名'
        )
    )

    # 商品表创建联合唯一约束
    op.create_unique_constraint(
        'uq_domain_product_sku',
        'products',
        ['domain', 'product_sku']
    )

    # 订单表创建联合唯一约束
    op.create_unique_constraint(
        'uq_domain_order_number',
        'orders',
        ['domain', 'order_number']
    )

    # 订单明细表增加 domain 字段
    op.add_column(
        'order_items',
        sa.Column(
            'domain',
            sa.String(length=64),
            nullable=False,
            comment='店铺域名'
        )
    )

    # 订单明细表创建联合唯一约束
    op.create_unique_constraint(
        'uq_domain_order_number_product_sku',
        'order_items',
        ['domain', 'order_number', 'product_sku']
    )

    # 创建订单明细表的两组联合外键

    # 关联订单表
    op.create_foreign_key(
        'fk_order_item_order',
        'order_items',
        'orders',
        ['domain', 'order_number'],
        ['domain', 'order_number']
    )

    # 关联商品表
    op.create_foreign_key(
        'fk_order_item_product',
        'order_items',
        'products',
        ['domain', 'product_sku'],
        ['domain', 'product_sku']
    )


def downgrade() -> None:
    """Downgrade schema."""

    # 删除订单明细表的两组联合外键
    op.drop_constraint(
        'fk_order_item_order',
        'order_items',
        type_='foreignkey'
    )

    op.drop_constraint(
        'fk_order_item_product',
        'order_items',
        type_='foreignkey'
    )

    # 删除订单明细表的联合唯一约束
    op.drop_constraint(
        'uq_domain_order_number_product_sku',
        'order_items',
        type_='unique'
    )

    # 删除订单表和商品表的联合唯一约束
    op.drop_constraint(
        'uq_domain_order_number',
        'orders',
        type_='unique'
    )

    op.drop_constraint(
        'uq_domain_product_sku',
        'products',
        type_='unique'
    )

    # 恢复原来的单列唯一索引
    op.create_index(
        op.f('order_number'),
        'orders',
        ['order_number'],
        unique=True
    )

    op.create_index(
        op.f('product_sku'),
        'products',
        ['product_sku'],
        unique=True
    )

    op.create_index(
        op.f('uq_order_number_product_sku'),
        'order_items',
        ['order_number', 'product_sku'],
        unique=True
    )

    # 删除新增的 domain 字段
    op.drop_column('order_items', 'domain')
    op.drop_column('products', 'domain')

    # 恢复原来的单列外键
    op.create_foreign_key(
        op.f('order_items_ibfk_1'),
        'order_items',
        'orders',
        ['order_number'],
        ['order_number']
    )

    op.create_foreign_key(
        op.f('order_items_ibfk_2'),
        'order_items',
        'products',
        ['product_sku'],
        ['product_sku']
    )