# DATABASE-DESIGN

## 订单表（Order）

| 字段名                   | 字段类型          | 字段描述              |
|-----------------------|---------------|-------------------|
| order_id              | BIGINT        | 订单id，主键，订单表中的唯一标识  |
| order_number          | VARCHAR(64)   | 订单编号           |
| order_status          | VARCHAR(32)   | 订单状态              |
| generation_time       | DATETIME      | 订单生成时间            |
| payment_time          | DATETIME      | 订单支付时间            |
| payment_status        | VARCHAR(32)   | 支付状态              |
| payment_method        | VARCHAR(64)   | 支付方式              |
| payment_number        | VARCHAR(128)  | 支付流水号或第三方支付交易编号   |
| total_amount          | DECIMAL(12,2) | 订单总金额             |
| currency_code         | DECIMAL(12,2) | 货币代码             |
| logistic_order_number | VARCHAR(128)  | 物流单号              |
| logistics_status      | VARCHAR(32)   | 物流状态              |
| customer_name         | VARCHAR(128)  | 客户姓名或收件人姓名        |
| address               | VARCHAR(255)  | 收货地址              |
| apartment             | VARCHAR(255)  | 公寓、套房或单元号         |
| city                  | VARCHAR(100)  | 城市                |
| country_region        | VARCHAR(100)  | 国家或地区             |
| province_state        | VARCHAR(100)  | 省份或州              |
| postcode              | VARCHAR(32)   | 邮政编码              |
| phone                 | VARCHAR(32)   | 联系电话              |
| extra_information     | TEXT          | 订单补充信息或客户备注       |
| mailbox               | VARCHAR(254)  | 客户邮箱              |
| domain                | VARCHAR(64)   | 域名                |
| number_of_products    | INT UNSIGNED  | 订单包含的商品总件数        |

## 商品表（Product_sku）

| 字段名            | 字段类型          | 字段描述            |
|----------------|---------------|-----------------|
| product_id     | BIGINT        | 商品id，主键，商品表中的唯一标识  |
| domain         | VARCHAR(64)   | 域名                |
| product_sku    | VARCHAR(64)   | 商品sku     |
| product_name   | VARCHAR(255)  | 商品名             |
| product_slug   | VARCHAR(255)  | 商品slug          |
| specifications | VARCHAR(255)  | 商品规格          |
| product_image  | VARCHAR(2048) | 商品图片链接      |

## 商品表（Product_spu）

| 字段名            | 字段类型          | 字段描述            |
|----------------|---------------|-----------------|
| product_id     | BIGINT        | 商品id，主键，商品表中的唯一标识  |
| domain         | VARCHAR(64)   | 域名                |
| product_spu    | VARCHAR(64)   | 商品spu     |
| product_name   | VARCHAR(255)  | 商品名             |
| product_slug   | VARCHAR(255)  | 商品slug          |
| product_price  | DECIMAL(12,2) | 商品金额          |
| product_stock  | INT UNSIGNED  | 商品库存          |
| product_image  | VARCHAR(2048) | 商品图片链接      |

## 商品标签表（Product_tag）

| 字段名            | 字段类型          | 字段描述            |
|----------------|---------------|-----------------|
| tag_id         | BIGINT        | 标签id，主键，标签表中的唯一标识  |
| tag_name       | VARCHAR(100)  | 标签名 |

## 订单明细表（Order_items）

| 字段名            | 字段类型        | 字段描述            |
|----------------|-------------|-----------------|
| id             | BIGINT      | id，主键，明细表中的唯一标识  |
| domain         | VARCHAR(64) | 域名                |
| order_number   | VARCHAR(64) | 订单编号，订单表中的唯一标识  |
| product_sku    | VARCHAR(64) | 商品sku，商品表中的唯一标识 |
| product_number | INT         | 商品数量，在本订单中的数量   |

## 商品标签关联表（Product_tag_relations）

| 字段名            | 字段类型        | 字段描述            |
|----------------|-------------|-----------------|
| id             | BIGINT      | id，主键，关联表中的唯一标识  |
| product_id     | BIGINT      | 商品spu表id     |
| tag_id         | BIGINT      | 标签id   |

