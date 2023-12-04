# -*- coding: utf-8 -*-

from odoo import models, fields, api

import lazop_sdk as lazop

class lazada_product_template(models.Model):
    _inherit = 'product.template'
    
    skus_status = fields.Char(string="Skus Status")
    skus_quantity = fields.Char(string="Skus Quantiy")
    skus_product_weight = fields.Char(string="Skus Product Weight")
    seller_sku=fields.Char(string="Seller Skus")
    skus_shopSku=fields.Char(string="ShopSku Skus")
    skus_url=fields.Char(string="Skus Url")
    skus_package_width=fields.Char(string="Skus Package Width")
    skus_special_to_time=fields.Char(string="Skus Special to time")
    skus_special_from_time=fields.Char(string="Skus Special from time")
    skus_package_height=fields.Char(string="Skus Package Height")
    skus_special_price=fields.Integer(string="Skus Special Price")
    skus_package_length=fields.Char(string="Skus Special Lenght")
    skus_package_weight=fields.Char(string="Skus Special Weight")
    skus_available=fields.Integer(string="Skus Availiable")
    sku_id=fields.Char(string="Skus ID")
    skus_special_to_date=fields.Char(string="Skus Special to Date")
    suspendedSkus=fields.Char(string="Suspended Skus")
    subStatus=fields.Char(string="Substatus")
    trialProduct=fields.Boolean(string="Trial Product")
    rejectReason_suggestion=fields.Char(string="Reject Reason Suggetion")
    rejectReason_violationDetail=fields.Char(string="Reject Reason Violation")
    short_description=fields.Char(string="Short Description")
    warranty_type=fields.Char(string="Warrenty Type")
    brand=fields.Char(string="Brand")
    status=fields.Char(string="Status")
    
    def get_product(self):
        access_token = ""
        url = "https://api.lazada.com.ph/rest"
        appkey = 115604
        appSecret = ""
        client = lazop.LazopClient(url, appkey ,appSecret)
        request = lazop.LazopRequest('/products/get','GET')
        request.add_api_param('filter', 'live')
        request.add_api_param('offset', '0')
        request.add_api_param('limit', '50')
        request.add_api_param('update_after', '2023-01-10T09:00:00+08:00')
        request.add_api_param('options', '1')
        response = client.execute(request, access_token)
        # print("This is response",response.body)
        # print(response.body['data']['products'])
        # res_data=response.body['data']
        for res in response.body['data']['products']:
            # print(res['created_at'])
            name=res['attributes']['name']
            list_price=res['skus'][0]['price']
            brand=res['attributes']['brand']
            status=res['status']
            product_vals={'name':name,'list_price':list_price,'brand':brand,'status':status}
            product_res=self.env['product.template'].create(product_vals)
            print(product_res.id)
    

class sale_order_list(models.Model):
    _inherit = 'sale.order.line'
    
    pick_up_store_address = fields.Char(string="Pickup Store Address")
    pick_up_store_name = fields.Char(string="Pickup Store Name")
    pick_up_store_code = fields.Char(string="Pickup Store Code")
    pick_up_store_open_hour = fields.Char(string="Pickup Store Open Hour")
    tax_amount=fields.Float(string="Tax Amount")
    reason=fields.Char(string="Reason")
    sla_time_stamp=fields.Char(string="SLA Time")
    voucher_seller=fields.Char(string="Voucher Seller")
    purchase_order_id=fields.Char(string="Purchase OID")
    voucher_code_seller=fields.Char(string="Voucher Code Seller")
    voucher_code=fields.Char(string="SLA Time")
    package_id=fields.Char(string="Package ID")
    buyer_id=fields.Char(string="Buyer ID")
    variation=fields.Char(string="Variation")
    voucher_code_platform=fields.Char(string="Variation")
    purchase_order_number=fields.Char(string="Purchase Order#")
    sku=fields.Char(string="SKU")
    order_type=fields.Char(string="Order Type")
    invoice_number=fields.Char(string="Invoice#")
    cancel_return_initiator=fields.Char(string="Cancel Return Initiator")
    shop_sku=fields.Char(string="Shop SKU")
    
    is_reroute=fields.Char(string="Is Reroute")
    stage_pay_status=fields.Char(string="stage_pay_status")
    sku_id=fields.Char(string="SKU ID")
    tracking_code_pre=fields.Char(string="Tracking Code Pre")
    shop=fields.Char(string="Shop")
    order_flag=fields.Char(string="Order Flag")
    is_fbl=fields.Char(string="ID FBL")
    
    delivery_option_sof=fields.Char(string="Delivery Option Sof")
    fulfillment_sla=fields.Char(string="fulfillment_sla")
    status=fields.Char(string="Status")
    voucher_platform=fields.Char(string="Voucher Platform")
    warehouse_code=fields.Char(string="Warehouse Code")
    promised_shipping_time=fields.Char(string="Promised shipping time")
    shipping_type=fields.Char(string="Shipping Type")
    voucher_seller_lpi=fields.Char(string="Voucher Seller LIP")
    shipping_fee_discount_platform=fields.Char(string="Shipping fee Disount Plateform")
    
    shipping_provider_type=fields.Char(string="shipping_provider_type")
    voucher_platform_lpi=fields.Char(string="voucher_platform_lpi")
    shipping_fee_original=fields.Char(string="shipping_fee_original")
    is_digital=fields.Char(string="is_digital")
    shipping_service_cost=fields.Char(string="shipping_service_cost")
    tracking_code=fields.Char(string="tracking_code")
    shipping_fee_discount_seller=fields.Char(string="Delivery Option Sof")
    shipping_amount=fields.Char(string="shipping_amount")
    reason_detail=fields.Char(string="reason_detail")
    return_status=fields.Char(string="return_status")
    shipment_provider=fields.Char(string="shipment_provider")
    priority_fulfillment_tag=fields.Char(string="priority_fulfillment_tag")
    voucher_amount=fields.Char(string="voucher_amount")
    digital_delivery_info=fields.Char(string="digital_delivery_info")
    extra_attributes=fields.Char(string="extra_attributes")
    
    
    


class sale_lazada(models.Model):
    _inherit = 'sale.order'
    
    
    voucher = fields.Char(string="Voucher")
    warehouse_code=fields.Char(string="Warehouse Code")
    order_number=fields.Char(string="Order#")
    voucher_code=fields.Char(string="Voucher Code")
    gift_option=fields.Char(string="Gift Option")
    shipping_fee_discount_platform=fields.Char(string="Shipping Discount")
    promised_shipping_times=fields.Char(string="Shipping Promised Times")
    national_registration_number=fields.Char(string="Registration#")
    shipping_fee_original=fields.Float(string="Shipping Fee Original")
    payment_method=fields.Char(string="Payment Method")
    shipping_fee_discount_seller=fields.Float(string="Shipping Fee Discount")
    shipping_fee=fields.Float(string="Shipping Fee")
    branch_number=fields.Char(string="Branch#")
    tax_code=fields.Char(string="TAX Code")
    items_count=fields.Char(string="Items Count")
    delivery_info=fields.Char(string="Items Count")
    # address_billing_country=fields.Char(string="Billing Country")
    # address_billing_city=fields.Char(string="Billing City")
    # address_billing_address1=fields.Char(string="Billing Address1")
    # address_billing_address2=fields.Char(string="Billing Address2")
    # address_billing_address3=fields.Char(string="Billing Address3")
    # address_billing_address4=fields.Char(string="Billing Address4")
    # address_billing_address5=fields.Char(string="Billing Address5")
    # address_billing_phone=fields.Char(string="Billing Phone")
    # address_billing_phone2=fields.Char(string="Billing Phone2")
    # address_billing_post_code=fields.Char(string="Billing Postal Code")
    # address_billing_first_name=fields.Char(string="Billing First Name")
    # address_billing_last_name=fields.Char(string="Billing Last Name")
    
    # address_shipping_country=fields.Char(string="Shipping Country")
    # address_shipping_city=fields.Char(string="Shipping City")
    # address_shipping_address1=fields.Char(string="Shipping Address1")
    # address_shipping_address2=fields.Char(string="Shipping Address2")
    # address_shipping_address3=fields.Char(string="Shipping Address3")
    # address_shipping_address4=fields.Char(string="Shipping Address4")
    # address_shipping_address5=fields.Char(string="Shipping Address5")
    # address_shipping_phone=fields.Char(string="Shipping Phone")
    # address_shipping_phone2=fields.Char(string="Shipping Phone2")
    # address_shipping_post_code=fields.Char(string="Shipping Postal Code")
    # address_shipping_first_name=fields.Char(string="Shipping First Name")
    # address_shipping_last_name=fields.Char(string="Shipping Last Name")
    
    lazada_order_id = fields.Char(string="Lazada Order ID")
    gift_message= fields.Char(string="Gift Message")
    remarks =fields.Char(string="Remarks")
    order_status=fields.Char(string="Order Status")
    request_id=fields.Char(string="Request ID")
    
    def status_update(self):
        access_token = "50000801a16kXNupe6ccu9rU2Cig1b2e553fLlYgTWCGxmxuBvr1RLrzw0ACPwRu"
        url = "https://api.lazada.com.ph/rest"
        appkey = 115604
        appSecret = "hLDS2i4h0UW8fHgBZpekBXlaOpJgXd4b"
        client = lazop.LazopClient(url, appkey ,appSecret)
        request = lazop.LazopRequest('/order/get','GET')
        all_records = self.env['sale.order'].search([])
        all_order_ids=[]
        for rec in all_records:
           all_order_ids.append(rec['lazada_order_id'])
           lazada_ids=list(filter(bool,all_order_ids))      
        for ids in lazada_ids:
            request.add_api_param('order_id', ids)
            response = client.execute(request, access_token)
            order_status=response.body['data']['statuses'][0]
            lazada_status = self.env['sale.order'].search([('lazada_order_id', '=', ids )])
            # print("Update ID",lazada_status.lazada_order_id)
            lazada_status.write({'order_status': order_status})
            print("Save",order_status)
            
         
    def get_order(self):
        print("Order here")
        access_token = "50000801a16kXNupe6ccu9rU2Cig1b2e553fLlYgTWCGxmxuBvr1RLrzw0ACPwRu"
        url = "https://api.lazada.com.ph/rest"
        appkey = 115604
        appSecret = "hLDS2i4h0UW8fHgBZpekBXlaOpJgXd4b"

        client = lazop.LazopClient(url, appkey ,appSecret)
        request = lazop.LazopRequest('/orders/get','GET')
        request.add_api_param('update_before', '2023-02-10T16:00:00+08:00')
        request.add_api_param('sort_direction', 'DESC')
        request.add_api_param('offset', '0')
        request.add_api_param('limit', '10')
        request.add_api_param('update_after', '2023-01-10T09:00:00+08:00')
        request.add_api_param('sort_by', 'updated_at')
        request.add_api_param('created_before', '2023-02-10T16:00:00+08:00')
        request.add_api_param('created_after', '2023-01-10T09:00:00+08:00')
        response = client.execute(request, access_token)
        # print(response.body['orders'][0])
        res_data=response.body['data']
        for res in res_data['orders']:
            print(res['created_at'])
            voucher=res['voucher']
            warehouse_code=res['warehouse_code']
            order_number=res['order_number']
            voucher_code=res['voucher_code']
            gift_option=res['gift_option']
            shipping_fee_discount_platform=res['shipping_fee_discount_platform']
            promised_shipping_times=res['promised_shipping_times']
            national_registration_number=res['national_registration_number']
            shipping_fee_original=res['shipping_fee_original']
            payment_method=res['payment_method']
            shipping_fee_discount_seller=res['shipping_fee_discount_seller']
            shipping_fee=res['shipping_fee']    
            branch_number=res['branch_number']
            tax_code=res['tax_code']
            items_count=res['items_count']
            delivery_info=res['delivery_info']
            lazada_order_id=res['order_id']
            gift_message=res['gift_message']
            remarks=res['remarks']
            # request_id=res['request_id']
            
            
            customer_name=res['address_shipping']['first_name'] + res['address_shipping']['last_name']
            mobile=res['address_shipping']['phone2']
        
            vals={'name':customer_name,'mobile':mobile}
            partner=self.env['res.partner'].create(vals)
            partner_id=partner.id
            print("Partner ID",partner_id)
            
            
 
            street=res['address_shipping']['address1']
            street1=res['address_shipping']['address2']
            city=res['address_shipping']['city']
            zip=res['address_shipping']['post_code']
            phone=res['address_shipping']['phone']
            # shipping_vals={'type':delivery,'street':street,'street2':street1,'city':city,'zip':zip,'parent_id':partner_id}
            shipping_vals={'type':'delivery','street':street,'street2':street1,'city':city,'zip':zip,'parent_id':partner_id}
            partner_shipping_id=self.env['res.partner'].create(shipping_vals)
            print(partner_shipping_id.id)
            invoice_street=res['address_billing']['address1']
            invoice_street1=res['address_billing']['address2']
            invoice_city=res['address_billing']['city']
            invoice_zip=res['address_billing']['post_code']
            invoice_phone=res['address_billing']['phone']
            invoice_mobile=res['address_billing']['phone2']
            
            invoice_vals={'type':'invoice','street':invoice_street,'street2':invoice_street1,'city':invoice_city,'zip':invoice_zip,'parent_id':partner_id}
            partner_invoice_id=self.env['res.partner'].create(invoice_vals)
            print("Partner Invoice ID",partner_invoice_id.id)
            
            req_values = {'voucher':voucher,'warehouse_code':warehouse_code,'order_number':order_number,'voucher_code':voucher_code,
                        'gift_option':gift_option,'shipping_fee_discount_platform':shipping_fee_discount_platform,'promised_shipping_times':promised_shipping_times,
                        'national_registration_number':national_registration_number,'shipping_fee_original':shipping_fee_original,'payment_method':payment_method,
                        'shipping_fee_discount_seller':shipping_fee_discount_seller,'shipping_fee':shipping_fee,
                        'branch_number':branch_number,'tax_code':tax_code,'items_count':items_count,'delivery_info':delivery_info,'lazada_order_id':lazada_order_id,
                        'gift_message':gift_message,'remarks':remarks,'partner_id':partner_id
                        }
            
            sale_order_id=self.env['sale.order'].create(req_values)
            print("sale order id",sale_order_id.id)

