# 订单模块 API 设计文档

## 1. 文档说明

本文档描述订单模块的接口设计，供前端页面调用及后端开发参考。

当前订单模块包含两个核心接口：

1. 获取订单列表
2. 获取订单详情

## 2. 通用约定

- API 前缀：`/api/v1`
- 数据格式：JSON
- 请求与响应编码：UTF-8
- 金额字段使用字符串返回，避免浮点数精度问题。
- 时间格式：`YYYY-MM-DD HH:mm:ss`
- 以下示例中的订单状态、支付方式等枚举值为示例，实际值以项目约定为准。

## 3. 获取订单列表

### 3.1 接口信息

|项目|说明|
|---|---|
|接口名称|获取订单列表|
|请求方式|GET|
|接口地址|`/api/v1/orders`|
|功能说明|获取订单列表，支持分页、筛选和关键词搜索|

### 3.2 请求参数

所有参数均为 URL 查询参数，均为可选参数；不传时使用默认值。

|参数名|类型|是否必填|默认值|说明|
|---|---|---|---|---|
|page|integer|否|1|页码，从 1 开始|
|page_size|integer|否|20|每页记录数|
|start_date|string|否|-|开始日期，格式 `YYYY-MM-DD`|
|end_date|string|否|-|结束日期，格式 `YYYY-MM-DD`|
|country_region|string|否|-|国家/地区|
|payment_method|string|否|-|支付方式|
|payment_status|string|否|-|支付状态|
|q|string|否|-|关键词，可用于搜索订单编号|
|sort_by|string|否|payment_time|排序字段|
|sort_order|string|否|desc|排序方向：`asc` 或 `desc`|

示例请求：

```http
GET /api/v1/orders?page=1&page_size=20&payment_status=Paid&country_region=United%20States&q=D11
```

### 3.3 成功响应

HTTP 状态码：`200 OK`

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "total": 2,
    "page": 1,
    "page_size": 20,
    "items": [
      {
        "order_id": 11,
        "order_number": "#D11",
        "payment_time": "2026-11-17 04:45:00",
        "payment_status": "Paid",
        "payment_method": "Credit card",
        "logistics_status": "Unfulfilled",
        "total_amount": "150.00",
        "number_of_products": 1,
        "country_region": "United States"
      },
      {
        "order_id": 10,
        "order_number": "#D10",
        "payment_time": "2026-11-17 02:17:00",
        "payment_status": "Paid",
        "payment_method": "PayPal",
        "logistics_status": "Unfulfilled",
        "total_amount": "693.45",
        "number_of_products": 3,
        "country_region": "Canada"
      }
    ]
  }
}
```

### 3.4 响应字段说明

|字段名|类型|说明|
|---|---|---|
|total|integer|符合筛选条件的订单总数|
|page|integer|当前页码|
|page_size|integer|每页记录数|
|items|array|当前页订单列表|
|order_id|integer|订单数据库 ID，用于查询订单详情|
|order_number|string|订单编号|
|payment_time|string/null|支付时间，未支付时可以为空|
|payment_status|string|支付状态|
|payment_method|string/null|支付方式|
|logistics_status|string|物流状态|
|total_amount|string|订单总金额|
|number_of_products|integer|订单商品总件数，不是商品种类数|
|country_region|string/null|国家/地区|

## 4. 获取订单详情

### 4.1 接口信息

|项目|说明|
|---|---|
|接口名称|获取订单详情|
|请求方式|GET|
|接口地址|`/api/v1/orders/{order_id}`|
|功能说明|根据订单 ID 获取订单基本信息、支付信息、客户信息、物流信息及订单商品明细|

### 4.2 路径参数

|参数名|类型|是否必填|说明|
|---|---|---|---|
|order_id|integer|是|订单数据库 ID|

示例请求：

```http
GET /api/v1/orders/11
```

### 4.3 成功响应

HTTP 状态码：`200 OK`

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "order_info": {
      "order_id": 11,
      "order_number": "#D11",
      "order_status": "Open",
      "generation_time": "2026-11-17 04:30:00",
      "total_amount": "150.00",
      "number_of_products": 1
    },
    "payment_info": {
      "payment_status": "Paid",
      "payment_method": "Credit card",
      "payment_time": "2026-11-17 04:45:00",
      "payment_number": "PAY123456"
    },
    "customer_info": {
      "customer_name": "John Smith",
      "mailbox": "john@example.com",
      "phone": "+1 1234567890",
      "country_region": "United States",
      "province_state": "California",
      "city": "Los Angeles",
      "address": "123 Main Street",
      "apartment": "Apt 101",
      "postcode": "90001",
      "extra_information": "Please leave at the door"
    },
    "logistics_info": {
      "logistics_status": "Unfulfilled",
      "logistic_order_number": null
    },
    "order_items": [
      {
        "id": 1,
        "product_id": 101,
        "product_name": "Classic T-Shirt",
        "product_sku": "TSHIRT-001",
        "product_image": "https://example.com/image.jpg",
        "unit_price": "150.00",
        "quantity": 1,
        "subtotal": "150.00"
      }
    ]
  }
}
```

### 4.4 响应字段说明

#### 订单信息 `order_info`

|字段名|类型|说明|
|---|---|---|
|order_id|integer|订单数据库 ID|
|order_number|string|订单编号|
|order_status|string|订单状态|
|generation_time|string|订单创建时间|
|total_amount|string|订单总金额|
|number_of_products|integer|订单商品总件数|

#### 支付信息 `payment_info`

|字段名|类型|说明|
|---|---|---|
|payment_status|string|支付状态|
|payment_method|string/null|支付方式|
|payment_time|string/null|支付时间|
|payment_number|string/null|支付流水号或支付编号|

#### 客户信息 `customer_info`

|字段名|类型|说明|
|---|---|---|
|customer_name|string|客户姓名|
|mailbox|string/null|客户邮箱|
|phone|string/null|联系电话|
|country_region|string/null|国家/地区|
|province_state|string/null|省/州|
|city|string/null|城市|
|address|string/null|详细地址|
|apartment|string/null|公寓、楼栋或单元等补充地址|
|postcode|string/null|邮政编码|
|extra_information|string/null|客户补充说明|

#### 物流信息 `logistics_info`

|字段名|类型|说明|
|---|---|---|
|logistics_status|string|物流状态|
|logistic_order_number|string/null|物流单号|

#### 订单商品明细 `order_items`

|字段名|类型|说明|
|---|---|---|
|id|integer|订单明细 ID|
|product_id|integer|商品 ID|
|product_name|string|下单时的商品名称|
|product_sku|string|下单时的商品 SKU|
|product_image|string/null|下单时的商品图片地址|
|unit_price|string|下单时的商品单价|
|quantity|integer|购买数量|
|subtotal|string|该商品明细小计，通常为单价乘以数量|

## 5. 错误响应

### 5.1 订单不存在

HTTP 状态码：`404 Not Found`

```json
{
  "code": 404,
  "message": "Order not found",
  "data": null
}
```

### 5.2 请求参数错误

HTTP 状态码：`422 Unprocessable Entity`

```json
{
  "code": 422,
  "message": "Invalid request parameters",
  "data": null
}
```

## 6. 数据查询说明

- 订单列表接口主要查询 `orders` 表。
- 订单详情接口查询 `orders` 表，并通过订单明细关联 `order_items` 和 `products`，组装完整响应。
- `order_items` 建议保存下单时的商品名称、SKU、图片和单价等快照字段，避免商品资料后续修改影响历史订单展示。
- `number_of_products` 表示订单中商品的总件数。例如商品 A 购买 2 件、商品 B 购买 3 件，则该值为 5。

## 7. 待项目确认事项

- `order_status`、`payment_status`、`payment_method`、`logistics_status` 的具体可选值。
- 日期筛选使用订单创建时间还是支付时间。本设计暂按列表中的支付时间理解，实际开发时应与前端筛选定义保持一致。
- `sort_by` 允许排序的字段应由后端限定，不能直接将前端传入的任意字符串拼接进 SQL。
- 如果订单尚未支付，`payment_time`、`payment_method`、`payment_number` 等字段允许返回 `null`。
