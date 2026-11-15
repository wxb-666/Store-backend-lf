# 后端服务设计

本目录用于存放店铺后台的 Python 后端服务。采用 FastAPI、SQLAlchemy 和 MySQL：  
FastAPI 负责 HTTP API，SQLAlchemy 负责数据库访问，MySQL 用于保存订单、商品和客户等业务数据。

## 后端结构

    be/
    ├─ app/
    │  ├─ main.py                 # 应用入口，创建 FastAPI 实例并注册路由
    │  ├─ api/
    │  │  └─ orders.py             # 订单列表、详情、创建和更新接口
    │  ├─ models/                  # SQLAlchemy 数据模型
    │  │  ├─ order.py              # 订单和订单项模型
    │  │  ├─ product.py            # 商品和商品图片模型
    │  │  └─ customer.py           # 客户模型
    │  ├─ schemas/                 # Pydantic 请求和响应模型
    │  │  └─ order.py              # 订单接口的数据结构和参数校验
    │  ├─ services/                # 业务逻辑层
    │  │  └─ order_service.py      # 订单查询、筛选、分页和状态处理
    │  ├─ db/                      # 数据库连接和会话
    │  │  ├─ session.py            # SQLAlchemy 引擎与会话依赖
    │  │  └─ base.py               # 模型注册基类
    │  └─ core/                    # 配置、异常处理和安全等基础能力
    │     └─ config.py             # 环境变量与应用配置
    ├─ tests/                      # 接口和业务逻辑测试
    ├─ requirements.txt            # Python 依赖清单
    ├─ Dockerfile                  # 后端镜像构建定义
    └─ README.md                   # 本说明文件

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
