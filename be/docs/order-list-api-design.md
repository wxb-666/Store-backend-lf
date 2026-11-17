---
doc_id: API-ORDERS-LIST-001
title: 订单列表 API 接口设计
owner: TBD
status: DRAFT
last_reviewed: 2026-11-18
source_of_truth: false
supersedes: []
related_docs:
  - be/docs/database-design.md
related_code_paths:
  - fe/src/views/OrdersView.vue
  - fe/src/components/orders/OrdersToolbar.vue
  - fe/src/components/orders/OrdersTable.vue
change_triggers:
  - 订单列表筛选条件发生变化
  - 订单列表展示字段或商品图片预览规则发生变化
  - 订单数据库字段发生变化
---

# 订单列表 API 接口设计

## 文档信息

| 项目 | 内容 |
| --- | --- |
| 项目名称 | Store Backend |
| 版本/阶段 | V1 / 订单列表 |
| 设计范围 | 查询订单列表、按订单编号或订单 slug 搜索、按支付方式筛选、返回列表商品图片预览 |
| 对应功能详细设计 | TBD |
| 对应 UI 详细设计 | 当前订单列表前端页面：`fe/src/views/OrdersView.vue` |
| 创建日期 | 2026-11-18 |
| 最后更新 | 2026-11-18 |
| 文档状态 | DRAFT |

## 1. 文档定位

### 1.1 文档职责边界

- 本文档定义订单列表查询接口的 HTTP 契约、筛选语义、分页语义和列表图片预览字段。
- 本文档不定义订单详情、创建、更新、导出、批量操作接口，也不替代数据库表结构设计。
- 正式机器契约以 `openapi.yaml` 为准；本文件是供评审和生成机器契约使用的结构化设计草稿。
- 如果本文档与已评审的数据库设计或 OpenAPI 冲突，应先确定事实源并同步更新相关文档，不得只改实现。

### 1.2 输入基线

| 文档/代码 | 用途 | 约束 |
| --- | --- | --- |
| `be/docs/database-design.md` | 订单、商品、订单明细字段现状 | 作为当前数据字段基线；本文指出的字段缺口需经数据库设计确认后补充 |
| `fe/src/components/orders/OrdersToolbar.vue` | 当前列表搜索框与支付方式选项 | 搜索框接收单个文本值；当前页面有日期、国家和支付状态控件，但本接口暂不支持这些筛选 |
| `fe/src/components/orders/OrdersTable.vue` | 当前列表展示列与静态数据 | 本接口需支撑列表摘要字段；商品图片列待前端页面补充 |
| OpenAPI / 鉴权 / 错误码文档 | 当前仓库未发现 | 待建立时同步本设计 |

### 1.3 契约分层约定

| 层级 | 事实源 | 冲突处理 |
| --- | --- | --- |
| P0 | 评审通过的 `openapi.yaml`（当前尚未发现） | 后续以 OpenAPI 为机器契约，并回写本文档 |
| P1 | 本 API 设计文档 | 用于设计评审和生成 OpenAPI |
| P2 | 数据库设计和页面代码 | 用于约束字段来源及页面消费方式；必要时先更新上游设计 |

### 1.4 单接口固定结构

- 接口说明
- Method / Path
- Path 参数
- Query 参数
- Body 参数
- 成功响应
- 业务规则
- 业务错误码

## 2. 全局接口约定

### 2.1 Base Path 与版本

- Base Path：`/api/v1`
- 资源名：复数小写 `orders`
- 版本策略：破坏性契约变更通过新 API 版本发布；兼容性字段新增保持向后兼容。

### 2.2 认证与安全边界

- 认证方式：TBD；该接口属于店铺管理后台，生产环境不得匿名访问。
- 授权边界：调用方只能查询当前登录用户有权访问的店铺订单。租户/店铺识别方式为 TBD。
- 返回字段不得包含卡号、凭证、密码等敏感支付数据。
- 审计要求：只读查询是否记录审计日志为 TBD；至少记录认证失败和授权失败事件。

### 2.3 列表接口公共参数

- 分页方式：页码分页；`page` 从 `1` 开始，默认 `1`。
- 每页条数：`page_size` 默认 `20`，最大 `100`。
- 默认排序：`generation_time` 降序，同一时间按稳定订单主键降序。客户端不得依赖未声明的数据库自然顺序。
- 本版本不开放排序参数。
- 业务筛选仅有：`q`（订单编号或订单 slug）与 `payment_method`。
- 搜索与支付方式筛选同时提供时，两个条件按 AND 组合；`q` 内的订单编号和订单 slug 两个字段按 OR 匹配。

### 2.4 请求参数约定

- 字段命名使用 `snake_case`。
- 文本参数执行首尾空白去除；空字符串按未提供处理。
- `q` 对订单编号和订单 slug 执行不区分大小写的包含匹配。通配符字符按普通输入字符处理，不允许用户借此构造 SQL 模式。
- `payment_method` 使用稳定代码值，不使用展示文案。代码词典见第 2.6 节。

### 2.5 响应结果约定

- 成功响应使用 JSON。
- 空结果返回 `200 OK`，`items` 为空数组，分页总数为 `0`。
- 金额使用十进制字符串和独立币种代码，避免浮点精度损失。
- 时间使用 RFC 3339 / ISO 8601 时区格式；持久化和传输统一使用 UTC。
- 列表中的商品图片仅为预览数据，不代表订单详情完整商品明细。
- 缺少商品图片时 `image_url` 返回 `null`，前端显示默认占位图。

### 2.6 状态与枚举词典

| 字段 | 契约值 | 页面展示示例 | 状态 |
| --- | --- | --- | --- |
| `payment_method` | `credit_card`、`paypal`、`shop_pay` | Credit card、PayPal、Shop Pay | 建议值，需与实际支付配置确认 |
| `payment_status` | TBD | Paid | 需与订单状态设计统一 |
| `logistics_status` | TBD | Unfulfilled、Fulfilled | 需与物流状态设计统一 |
| `country_region.code` | ISO 3166-1 alpha-2 | US、CA | 推荐值，需确认现有数据兼容性 |

### 2.7 越界内容禁止项

- 不在本文中复制数据库 DDL 或迁移脚本。
- 不在本文中设计订单详情、订单创建、订单导出或批量操作的完整契约。
- 不在本接口中返回全部订单商品明细；详情接口负责完整明细。

## 3. 接口目录

#### MOD-ORDERS-LIST 订单列表查询

| 接口名称 | Method | Path | 用途 |
| --- | --- | --- | --- |
| 查询订单列表 | GET | `/api/v1/orders` | 分页查询当前店铺订单；以单个关键词匹配订单编号或订单 slug，并可按支付方式筛选 |

## 4. 模块详细设计

### 4.1 MOD-ORDERS-LIST 订单列表查询

#### 4.1.1 查询订单列表

- 接口说明：供订单列表页首次加载及搜索/支付方式筛选时查询订单摘要数据。
- 调用方：前端订单列表页。
- Method / Path：`GET /api/v1/orders`
- 鉴权：需要后台用户认证；店铺数据权限规则 TBD。
- 兼容性：响应新增可选字段为向后兼容；字段改名、删除或枚举语义改变属于破坏性变更。

Path 参数

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| N/A | N/A | N/A | 集合查询接口无 Path 参数 |

Query 参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `page` | integer | 否 | `1` | 页码，从 `1` 开始；最小值 `1` |
| `page_size` | integer | 否 | `20` | 每页条数；范围 `1..100` |
| `q` | string | 否 | N/A | 单个搜索值；在 `order_number` 或 `order_slug` 中任一匹配即可。两字段匹配关系为 OR |
| `payment_method` | string | 否 | N/A | 支付方式代码；与 `q` 条件按 AND 组合。允许值以支付方式词典为准 |

Body 参数

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| N/A | N/A | N/A | GET 列表请求不使用 Body |

请求示例

```http
GET /api/v1/orders?page=1&page_size=20&q=D11&payment_method=paypal
Accept: application/json
Authorization: Bearer <access_token>
```

响应数据示例

```json
{
  "items": [
    {
      "order_id": "ord_123",
      "order_number": "#D11",
      "payment_time": "2026-11-17T11:45:00Z",
      "payment_status": "paid",
      "payment_method": "paypal",
      "logistics_status": "unfulfilled",
      "total_amount": "150.00",
      "currency": "USD",
      "number_of_products": 3,
      "country_region": {
        "code": "US",
        "name": "United States"
      },
      "product_previews": [
        {
          "product_name": "Snowboard",
          "product_sku": "SNOW-01",
          "image_url": "https://cdn.example.com/products/snowboard.jpg",
          "quantity": 2
        },
        {
          "product_name": "Helmet",
          "product_sku": "HELMET-01",
          "image_url": "https://cdn.example.com/products/helmet.jpg",
          "quantity": 1
        }
      ],
      "additional_product_count": 0
    }
  ],
  "pagination": {
    "page": 1,
    "page_size": 20,
    "total_items": 1,
    "total_pages": 1
  }
}
```

成功响应

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `items` | array | 当前页订单摘要；无结果时为空数组 |
| `items[].order_id` | string | 稳定的内部订单 ID；数据库当前设计未列出该字段，待确认并补充 |
| `items[].order_number` | string | 面向商家的订单编号，如 `#D11` |
| `items[].payment_time` | string \| null | 支付时间，UTC RFC 3339；未支付时为 `null` |
| `items[].payment_status` | string | 支付状态代码 |
| `items[].payment_method` | string | 支付方式代码 |
| `items[].logistics_status` | string | 物流状态代码 |
| `items[].total_amount` | string | 订单总金额的十进制字符串 |
| `items[].currency` | string | ISO 4217 币种代码；数据库当前设计未列出该字段，待确认并补充 |
| `items[].number_of_products` | integer | 订单商品总件数，即所有订单明细数量之和 |
| `items[].country_region` | object \| null | 国家/地区摘要；未提供时为 `null` |
| `items[].country_region.code` | string | 国家/地区代码 |
| `items[].country_region.name` | string | 国家/地区展示名 |
| `items[].product_previews` | array | 最多 `3` 个订单商品明细预览；具体上限需前端确认 |
| `items[].product_previews[].product_name` | string | 下单商品名称；建议使用下单快照 |
| `items[].product_previews[].product_sku` | string | 商品 SKU |
| `items[].product_previews[].image_url` | string \| null | 商品图片 URL；为 `null` 时前端展示占位图 |
| `items[].product_previews[].quantity` | integer | 该明细的商品数量 |
| `items[].additional_product_count` | integer | 未包含在 `product_previews` 中的订单明细行数量，不是商品件数 |
| `pagination.page` | integer | 当前页码 |
| `pagination.page_size` | integer | 每页条数 |
| `pagination.total_items` | integer | 筛选后的总订单数 |
| `pagination.total_pages` | integer | 筛选结果的总页数；无结果时为 `0` |

业务规则（仅接口级承接）

- 先按当前调用方可访问的店铺范围限定订单，再应用筛选条件和分页。
- `q` 缺省或去空白后为空时不执行文本筛选；否则按不区分大小写的包含匹配，匹配 `order_number` 或 `order_slug` 任一字段。
- 当前数据库设计有 `product_slug`，没有 `order_slug`。本接口中的 slug 特指订单 slug；该字段在数据库确认前不得直接用 `product_slug` 代替。
- `payment_method` 缺省或去空白后为空时不执行该筛选；提供时必须匹配支付方式代码。无效枚举返回 `422`。
- 若同时提供 `q` 和 `payment_method`，返回同时满足支付方式条件且（订单编号匹配或订单 slug 匹配）的订单。
- 分页在筛选之后执行。默认按订单创建时间降序；同一创建时间以稳定的订单主键降序作为次级排序。
- `product_previews` 建议最多返回 `3` 条明细，按订单明细顺序返回；如果明细有图片，图片预览至少包含一条有非空 `image_url` 的明细。没有任何图片时允许图片字段均为 `null`，前端必须展示占位图。
- `additional_product_count = max(订单明细行总数 - product_previews 数量, 0)`。`number_of_products` 为明细数量之和，与明细行数不可混用。
- 列表图片优先使用订单明细中的商品图片快照。若当前阶段不存快照，可通过 SKU 关联商品表读取当前图片，但商品图片变更后历史订单列表图片也会变化。
- 数据读取必须采用分页查询和批量读取当前页商品预览，不得对每一条订单单独发起商品图片查询。
- 该接口只读，无状态变更、副作用、幂等键或重试写入要求。客户端遇到网络错误或 `5xx` 可重试 GET；遇到 `401/403` 应按认证/授权流程处理，`422` 应修正参数。
- 当前页面的日期、国家和支付状态控件不属于本版本接口筛选范围；若后续启用，需更新本契约。

业务错误码

| HTTP 状态 | 错误码 | 说明 |
| --- | --- | --- |
| 400 | `INVALID_QUERY_PARAMETER` | 分页参数格式错误或越界 |
| 401 | `UNAUTHENTICATED` | 缺少有效身份凭据 |
| 403 | `FORBIDDEN` | 调用方无权访问当前店铺订单 |
| 422 | `INVALID_PAYMENT_METHOD` | `payment_method` 不在有效枚举中 |
| 500 | `INTERNAL_ERROR` | 未预期的服务端错误；响应不得包含堆栈或数据库敏感信息 |

统一错误响应格式：

```json
{
  "error": {
    "code": "INVALID_PAYMENT_METHOD",
    "message": "The payment_method value is not supported.",
    "request_id": "req_123"
  }
}
```

## 5. 契约同步清单

### 5.1 OpenAPI 同步

| 模块 | 同步项 | 当前状态 | 说明 |
| --- | --- | --- | --- |
| 订单列表 | `GET /api/v1/orders` | TODO | 增加 query 参数、分页响应、错误响应和枚举 |
| 订单列表 | 商品预览 schema | TODO | 定义 `product_previews` 上限、空图语义和排序规则 |

### 5.2 错误码 / RBAC / 监控同步

| 模块 | 类型 | 当前状态 | 说明 |
| --- | --- | --- | --- |
| 订单列表 | ErrorCode | TODO | 将本文错误码纳入统一错误码规范 |
| 订单列表 | RBAC | TBD | 明确店铺级订单读取权限 |
| 订单列表 | Metric | TODO | 记录请求耗时、结果数量、错误率；不得记录敏感搜索内容 |
| 订单列表 | Database | TODO | 确认 `order_slug`、内部订单 ID、币种、订单明细图片快照及明细顺序字段 |

契约增量清单：

- 新增列表端点 `GET /api/v1/orders`。
- 新增 query 参数：`page`、`page_size`、`q`、`payment_method`。
- 新增订单列表摘要和 `product_previews` 响应结构。
- 定义 `q` 对订单编号或订单 slug 的 OR 匹配，以及 `payment_method` 与 `q` 的 AND 组合语义。
- 定义订单支付方式、支付状态、物流状态、币种和国家/地区代码词典。
- 同步认证授权、错误码和分页边界。

## 6. AI 实施摘要

| 模块 | 当前阶段 | 重点范围 | 下一步建议 |
| --- | --- | --- | --- |
| 订单列表查询 | DRAFT | 单一 `q` 搜索订单编号或订单 slug；支付方式筛选；分页；每单最多 3 个商品预览 | 确认第 7 节事项后，将契约同步到 OpenAPI，再实现 Schema、查询服务和接口测试 |

## 7. 待确认事项

| 编号 | 问题 | 影响模块 | 状态 |
| --- | --- | --- | --- |
| API-TBD-001 | 这里的 slug 是否确指订单 slug？当前数据库只有商品表 `product_slug`，没有订单 slug | 搜索字段、数据库 | OPEN |
| API-TBD-002 | 订单表是否增加稳定内部主键 `order_id`？ | 订单资源标识、响应结构 | OPEN |
| API-TBD-003 | 每个订单返回最多几张商品图？本文示例采用最多 `3` 张 | 列表响应、前端展示 | OPEN |
| API-TBD-004 | 订单明细是否保存商品名称、SKU、图片的下单时快照及稳定明细顺序？ | 图片与历史数据一致性 | OPEN |
| API-TBD-005 | 币种、支付方式、支付状态、物流状态的正式字段和枚举是什么？ | 响应 schema、筛选验证 | OPEN |
| API-TBD-006 | 后台认证方式、店铺级授权与统一错误响应规范是什么？ | 安全、错误响应 | OPEN |
| API-TBD-007 | 默认排序是否采用下单时间降序，是否需要支持客户端排序？ | 分页结果顺序 | OPEN |
