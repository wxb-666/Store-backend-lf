export interface OrderProductPreview {
  product_id: number
  product_name: string
  product_number: number
  product_sku: string
  product_image: string | null
}

export interface OrderListItem {
  order_id: number
  order_number: string
  payment_time: string | null
  payment_status: string | null
  payment_method: string | null
  logistics_status: string | null
  total_amount: string
  currency_code: string
  number_of_products: number
  product_items: OrderProductPreview[]
  domain: string | null
  country_region: string | null
}

interface OrderListResponse {
  code: number
  message: string
  data: { total: number; page: number; page_size: number; items: OrderListItem[] }
}

export interface OrderListParams {
  page: number
  pageSize: number
  query?: string
  paymentMethod?: string
  domain?: string
  sortOrder?: 'asc' | 'desc'
}

export interface OrderDetailProduct {
  id: number
  product_id: number
  product_name: string
  product_number: number
  product_sku: string
  specifications: string | null
  product_image: string | null
}

export interface OrderDetail {
  order_info: {
    order_id: number
    order_number: string
    domain: string
    order_status: string
    generation_time: string
    total_amount: string
    currency_code: string
    number_of_products: number
  }
  payment_info: {
    payment_status: string | null
    payment_method: string | null
    payment_time: string | null
    payment_number: string | null
  }
  customer_info: {
    customer_name: string | null
    mailbox: string | null
    phone: string | null
    country_region: string | null
    province_state: string | null
    city: string | null
    address: string | null
    apartment: string | null
    postcode: string | null
    extra_information: string | null
  }
  logistics_info: {
    logistics_status: string | null
    logistic_order_number: string | null
  }
  order_items: OrderDetailProduct[]
}

interface OrderDetailResponse {
  code: number
  message: string
  data: OrderDetail
}

export async function fetchOrderDetail(orderId: number, domain: string, signal?: AbortSignal) {
  const search = new URLSearchParams({ domain })
  const response = await fetch(`/api/v1/orders/${orderId}?${search.toString()}`, { signal })
  if (!response.ok) {
    if (response.status === 404) throw new Error('Order not found for this store.')
    throw new Error(`Unable to load order details (${response.status})`)
  }
  const result = await response.json() as OrderDetailResponse
  if (result.code !== 200) throw new Error(result.message || 'Unable to load order details')
  return result.data
}

export async function fetchOrders(params: OrderListParams, signal?: AbortSignal) {
  const search = new URLSearchParams({
    page: String(params.page),
    page_size: String(params.pageSize),
    sort_by: 'payment_time',
    sort_order: params.sortOrder ?? 'desc',
  })
  if (params.query) search.set('q', params.query)
  if (params.paymentMethod) search.set('payment_method', params.paymentMethod)
  if (params.domain) search.set('domain', params.domain)

  const response = await fetch(`/api/v1/orders?${search.toString()}`, { signal })
  if (!response.ok) throw new Error(`Unable to load orders (${response.status})`)
  const result = await response.json() as OrderListResponse
  if (result.code !== 200) throw new Error(result.message || 'Unable to load orders')
  return result.data
}
