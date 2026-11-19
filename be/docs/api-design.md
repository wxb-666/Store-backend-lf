# API-DESIGN

| 版本   | 修改日期   | 修改内容                                     |
|--------|------------|----------------------------------------------|
| v0.1.0 | 2026-11-19 | 新增 api 设计文档，完成订单模块的 api 设计。 |

## 1. 文档说明

本文档用于描述订单模块和商品模块的接口设计，共前端页面调用及后端开发参考。

## 2. 通用约定

> 1. API 前缀：`/api/v1`
> 2. 数据格式：JSON
> 3. 请求与响应编码：UTF-8
> 4. 金额字段使用字符串返回，避免浮点数精度影响。
> 5. 时间格式：`YYYY-MM-DD HH:mm:ss`

## 3. 订单模块 API

### 3.1 获取订单列表

#### 3.1.1 接口信息

| 项目     | 说明                                     |
|----------|------------------------------------------|
| 接口名称 | 获取订单列表                             |
| 请求方式 | GET                                      |
| 接口地址 | `/api/v1/orders`                         |
| 功能说明 | 获取订单列表，支持分页、筛选和关键词搜索 |

#### 3.1.2 请求参数

所有参数均为 URL 查询参数，均为可选参数；不传时使用默认值。

| 参数名         | 类型    | 是否必填 | 默认值       | 说明                               |
|----------------|---------|----------|--------------|------------------------------------|
| page           | integer | 否       | 1            | 页码，从 1 开始                    |
| page_size      | integer | 否       | 20           | 每页记录数                         |
| start_date     | string  | 否       | -            | 开始日期，格式 `YYYY-MM-DD`        |
| end_date       | string  | 否       | -            | 结束日期，格式 `YYYY-MM-DD`        |
| country_region | string  | 否       | -            | 国家/地区                          |
| payment_method | string  | 否       | -            | 支付方式                           |
| payment_status | string  | 否       | -            | 支付状态                           |
| domain         | string  | 否       | -            | 店铺域名                           |
| q              | string  | 否       | -            | 搜索关键词，支持订单编号或商品slug |
| sort_by        | string  | 否       | payment_time | 排序字段                           |
| sort_order     | string  | 否       | desc         | 排序方向：`asc` 或 `desc`          |

示例请求：

```http
GET /api/v1/orders?page=1&page_size=20&payment_status=Paid&country_region=United%20States&q=D11

GET /api/v1/orders?page=1&page_size=20&domain=lfshop.com&q=classic-t-shirt
```
#### 3.1.3 成功响应

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
        "order_number": "53956M100016",
        "payment_time": "2026-11-17 04:45:00",
        "payment_status": "Paid",
        "payment_method": "PayPal",
        "logistics_status": "Delivered",
        "total_amount": "150.00",
        "currency_code": "USD",
        "number_of_products": 2,
        "product_items": [
            {
                "product_id": 101,
                "product_name": "Classic T-Shirt",
                "product_number": 1,
                "product_sku": "SWH698555-PIN2XL",
                "product_image": "https://example.com/classic-t-shirt.jpg"
            },
            {
                "product_id": 102,
                "product_name": "Canvas Bag",
                "product_number": 1,
                "product_sku": "SWH698666-PIN2XL",
                "product_image": "https://example.com/canvas-bag.jpg"
            }
        ],
        "domain": "lfshop.com",
        "country_region": "United States"
      },
      {
        "order_id": 10,
        "order_number": "53956M100076",
        "payment_time": "2026-11-17 02:17:00",
        "payment_status": "Paid",
        "payment_method": "PayPal",
        "logistics_status": "Unfulfilled",
        "total_amount": "693.45",
        "currency_code": "USD",
        "number_of_products": 1,
        "product_items": [
            {
                "product_id": 121,
                "product_name": "Classic T-Shirt22",
                "product_number": 1,
                "product_sku": "SWH6987666-PIN2XL",
                "product_image": "https://example.com/classic-t-shirt2.jpg"
            }
        ],
        "domain": "lfshop.com",
        "country_region": "Canada"
      }
    ]
  }
}
```

#### 3.1.4 响应字段说明

| 字段名                         | 类型        | 说明                                         |
|--------------------------------|-------------|----------------------------------------------|
| total                          | integer     | 符合筛选条件的订单总数                       |
| page                           | integer     | 当前页码                                     |
| page_size                      | integer     | 每页记录数                                   |
| items                          | array       | 当前页订单列表                               |
| order_id                       | integer     | 订单数据库 ID，用于查询订单详情              |
| order_number                   | string      | 订单编号                                     |
| payment_time                   | string/null | 支付时间，未支付时可以为空                   |
| payment_status                 | string      | 支付状态                                     |
| payment_method                 | string/null | 支付方式                                     |
| logistics_status               | string      | 物流状态                                     |
| total_amount                   | string      | 订单总金额                                   |
| currency_code                  | string      | 货币代码                                     |
| number_of_products             | integer     | 订单商品总件数，不是商品种类数               |
| product_items                  | array       | 订单商品信息列表，用于展示商品图片及相关信息 |
| product_items[].product_id     | integer     | 商品 ID                                      |
| product_items[].product_name   | string      | 商品名称                                     |
| product_items[].product_number | integer     | 该商品在当前订单中的购买数量                 |
| product_items[].product_sku    | string      | 商品 SKU                                     |
| product_items[].product_image  | string/null | 商品图片地址                                 |
| domain                         | string/null | 店铺域名                                     |
| country_region                 | string/null | 国家/地区                                    |

### 3.2 获取订单详情

