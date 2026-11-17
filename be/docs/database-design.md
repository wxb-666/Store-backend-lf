# DATABASE-DESIGN

## 订单表

| 字段名 | 字段类型 | 字段描述 |
|---|---|---|
|order_number|VARCHAR(64)|订单编号，订单表中的唯一标识|
|order_status|VARCHAR(32)|订单状态|
|generation_time|DATETIME|订单生成时间|
|payment_time|DATETIME|订单支付时间|
|payment_status|VARCHAR(32)|支付状态|
|payment_method|VARCHAR(64)|支付方式|
|payment_number|VARCHAR(128)|支付流水号或第三方支付交易编号|
|total_amount|DECIMAL(12,2)|订单总金额|
|logistic_order_number|VARCHAR(128)|物流单号|
|logistics_status|VARCHAR(32)|物流状态|
|customer_name|VARCHAR(128)|客户姓名或收件人姓名|
|address|VARCHAR(255)|收货地址|
|apartment|VARCHAR(255)|公寓、套房或单元号|
|city|VARCHAR(100)|城市|
|country_region|VARCHAR(100)|国家或地区|
|province_state|VARCHAR(100)|省份或州|
|postcode|VARCHAR(32)|邮政编码|
|phone|VARCHAR(32)|联系电话|
|extra_information|TEXT|订单补充信息或客户备注|
|mailbox|VARCHAR(254)|客户邮箱|
|number_of_products|INT UNSIGNED|订单包含的商品总件数|

## 商品表

| 字段名 | 字段类型 | 字段描述 |
|---|---|---|
|product_sku  |VARCHAR(64)  |商品sku，商品表中的唯一标识|
|product_name |VARCHAR(255) |商品名|
|specifications |VARCHAR(255)  |商品规格|
|product_image  |VARCHAR(2048) |商品图片链接|

## 订单明细表

| 字段名 | 字段类型 | 字段描述 |
|---|---|---|
|order_number|VARCHAR(64)|订单编号，订单表中的唯一标识|
|product_sku |VARCHAR(64)|商品sku，商品表中的唯一标识|
|product_number|INT |商品数量，在本订单中的数量|