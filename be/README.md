# 后端服务设计

本目录用于存放店铺后台的 Python 后端服务。采用 FastAPI、SQLAlchemy 和 MySQL：  
FastAPI 负责 HTTP API，SQLAlchemy 负责数据库访问，MySQL 用于保存订单、商品和客户等业务数据。

## 后端结构

```text
be/
│
├── app/
│   │
│   ├── main.py                       # 应用入口，创建 FastAPI 实例
│   │
│   ├── api/                          # API 接口层
│   │   ├── __init__.py
│   │   ├── deps.py                   # 公共依赖（数据库会话、权限等）
│   │   │
│   │   └── v1/                       # API 版本管理
│   │       ├── __init__.py
│   │       ├── router.py             # 注册所有 v1 路由
│   │       ├── orders.py             # 订单相关接口
│   │       ├── products.py           # 商品相关接口
│   │       └── customers.py          # 客户相关接口
│   │
│   ├── models/                       # SQLAlchemy 数据模型
│   │   ├── __init__.py
│   │   ├── order.py                  # 订单主表模型
│   │   ├── order_item.py             # 订单商品明细模型
│   │   ├── product.py                # 商品模型
│   │   ├── product_image.py          # 商品图片模型
│   │   └── customer.py               # 客户模型
│   │
│   ├── schemas/                      # Pydantic 请求和响应模型
│   │   ├── __init__.py
│   │   ├── order.py                  # 订单请求、响应结构
│   │   ├── order_item.py             # 订单商品数据结构
│   │   ├── product.py                # 商品数据结构
│   │   └── customer.py               # 客户数据结构
│   │
│   ├── services/                     # 业务逻辑层
│   │   ├── __init__.py
│   │   ├── order_service.py          # 订单查询、筛选、分页等
│   │   ├── product_service.py       # 商品业务逻辑
│   │   └── customer_service.py      # 客户业务逻辑
│   │
│   ├── repositories/                 # 数据访问层
│   │   ├── __init__.py
│   │   ├── order_repository.py       # 订单数据库查询
│   │   ├── product_repository.py    # 商品数据库查询
│   │   └── customer_repository.py   # 客户数据库查询
│   │
│   ├── db/                           # 数据库基础配置
│   │   ├── __init__.py
│   │   ├── session.py                # SQLAlchemy 引擎和 Session
│   │   └── base.py                   # ORM 模型基类和模型注册
│   │
│   ├── core/                         # 核心配置
│   │   ├── __init__.py
│   │   ├── config.py                 # 环境变量和应用配置
│   │   ├── exceptions.py             # 自定义异常处理
│   │   └── logging.py                # 日志配置
│   │
│   └── storage/                      # 图片等文件存储
│       ├── __init__.py
│       └── image_storage.py          # 图片存储服务
│
├── alembic/                          # 数据库迁移管理
│   ├── versions/                     # 数据库迁移版本文件
│   └── env.py
│
├── tests/                             # 测试代码
│   ├── __init__.py
│   ├── test_orders.py
│   ├── test_products.py
│   └── test_customers.py
│
├── .env                               # 环境变量（不提交 Git）
├── .env.example                       # 环境变量示例
├── .gitignore
├── alembic.ini                        # Alembic 配置
├── requirements.txt                   # Python 依赖清单
├── Dockerfile                         # 后端镜像构建定义
└── README.md                          # 项目说明
```

## 各层职责

- api 只处理请求参数、调用服务并返回响应，不直接编写复杂查询逻辑。
- services 负责订单筛选、分页、状态变更等业务规则。
- models 定义数据库表和表之间的关联关系。
- schemas 明确前后端数据契约，避免直接暴露数据库模型。
- db 集中管理数据库连接、会话和事务。
- core 统一读取数据库地址、调试开关和跨域白名单等配置。

## 图片存储

数据库建议只保存商品图片的 URL、替代文本和排序等元数据；图片文件本身放在对象存储中。  
本地开发可以使用 MinIO，部署环境可使用 OSS、COS 或 S3 等兼容服务。

订单接口返回的商品项可以包含以下字段：

    {
      "product_id": 12,
      "title": "Snowboard",
      "quantity": 1,
      "image_url": "https://cdn.example.com/products/snowboard.jpg"
    }

## 接口示例

    GET   /api/orders                 # 成功订单列表，支持分页和关键词筛选
    GET   /api/orders/{order_id}      # 订单详情
    POST  /api/orders                 # 创建订单
    PATCH /api/orders/{order_id}      # 更新订单状态或其他字段

订单列表接口建议返回 items、total、page 和 page_size 等分页信息，以便前端替换当前写死的订单数据。

## 容器化建议

后端服务、MySQL 和图片对象存储建议在 docker-compose.yml 中作为独立服务运行。  
数据库应挂载命名卷，保证容器重建后订单数据仍能保留；后端通过 Compose 服务名连接数据库。
