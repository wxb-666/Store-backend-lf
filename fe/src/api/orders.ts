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
