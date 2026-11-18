# 后端 README

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
│   │   └── product.py                # 商品模型
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
│   ├── database/                     # 数据库基础配置
│   │   ├── __init__.py
│   │   └── connection.py             # SQLAlchemy 引擎和 Session、ORM 模型基类
│   │
│   └── core/                         # 核心配置
│      ├── __init__.py
│      ├── config.py                 # 环境变量和应用配置
│      ├── exceptions.py             # 自定义异常处理
│      └── logging.py                # 日志配置
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
├── docs/                             # 后端设计文件
│   ├── database-design.md            # 数据库设计
│   └── api-design.py                 # API设计
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
- database 集中管理数据库连接、会话和事务。
- core 统一读取数据库地址、调试开关和跨域白名单等配置。
- repositories 后端的数据访问层，负责读写数据库的代码，比如按条件查询订单、获取商品、创建或更新客户记录。
- docs/ 用于存放后端设计文档，如数据库设计、api设计等。
