
from logging.config import fileConfig

from alembic import context

from app.database.connection import Base, engine, DATABASE_URL

# 导入所有 ORM 模型，让 SQLAlchemy 注册数据表
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product import Product
from app.models.product_spu import ProductSpu
from app.models.product_tag import ProductTag
from app.models.product_tag_relation import ProductTagRelation


# 获取 Alembic 配置对象
config = context.config

# 配置日志
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 获取所有 ORM 模型的元数据
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """离线模式：生成 SQL 迁移语句"""

    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """在线模式：连接数据库并执行迁移"""

    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
