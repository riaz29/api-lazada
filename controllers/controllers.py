# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class SaleLazada(http.Controller):
    @http.route('/sale_lazada/', auth='public',  method=["POST"],csrf=False, type='json')
    def index(self, **kw):
        
        voucher=kw['data']['voucher']
        warehouse_code=kw['data']['warehouse_code']
        order_number=kw['data']['order_number']
        voucher_code=kw['data']['voucher_code']
        gift_option=kw['data']['gift_option']
        shipping_fee_discount_platform=kw['data']['shipping_fee_discount_platform']
        promised_shipping_times=kw['data']['promised_shipping_times']
        national_registration_number=kw['data']['national_registration_number']
        shipping_fee_original=kw['data']['shipping_fee_original']
        payment_method=kw['data']['payment_method']
        shipping_fee_discount_seller=kw['data']['shipping_fee_discount_seller']
        shipping_fee=kw['data']['shipping_fee']
        
        branch_number=kw['data']['branch_number']
        tax_code=kw['data']['tax_code']
        items_count=kw['data']['items_count']
        delivery_info=kw['data']['delivery_info']
        lazada_order_id=kw['data']['order_id']
        gift_message=kw['data']['gift_message']
        remarks=kw['data']['remarks']
        request_id=kw['request_id']
        
        
        customer_name=kw['data']['address_shipping']['first_name'] + kw['data']['address_shipping']['last_name']
        mobile=kw['data']['address_shipping']['phone2']
       
        vals={'name':customer_name,'mobile':mobile}
        partner=request.env['res.partner'].sudo().create(vals)
        partner_id=partner.id
        print("Partner ID",partner_id)
        
        
        delivery="delivery" 
        street=kw['data']['address_shipping']['address1']
        street1=kw['data']['address_shipping']['address2']
        city=kw['data']['address_shipping']['city']
        zip=kw['data']['address_shipping']['post_code']
        phone=kw['data']['address_shipping']['phone']
        # shipping_vals={'type':delivery,'street':street,'street2':street1,'city':city,'zip':zip,'parent_id':partner_id}
        shipping_vals={'type':'delivery','street':street,'street2':street1,'city':city,'zip':zip,'parent_id':partner_id}
        partner_shipping_id=request.env['res.partner'].sudo().create(shipping_vals)
        print(partner_shipping_id.id)
        invoice_street=kw['data']['address_billing']['address1']
        invoice_street1=kw['data']['address_billing']['address2']
        invoice_city=kw['data']['address_billing']['city']
        invoice_zip=kw['data']['address_billing']['post_code']
        invoice_phone=kw['data']['address_billing']['phone']
        invoice_mobile=kw['data']['address_billing']['phone2']
        
        invoice_vals={'type':'invoice','street':invoice_street,'street2':invoice_street1,'city':invoice_city,'zip':invoice_zip,'parent_id':partner_id}
        partner_invoice_id=request.env['res.partner'].sudo().create(invoice_vals)
        print("Partner Invoice ID",partner_invoice_id.id)
        
        req_values = {'voucher':voucher,'warehouse_code':warehouse_code,'order_number':order_number,'voucher_code':voucher_code,
                      'gift_option':gift_option,'shipping_fee_discount_platform':shipping_fee_discount_platform,'promised_shipping_times':promised_shipping_times,
                      'national_registration_number':national_registration_number,'shipping_fee_original':shipping_fee_original,'payment_method':payment_method,
                      'shipping_fee_discount_seller':shipping_fee_discount_seller,'shipping_fee':shipping_fee,
                      'branch_number':branch_number,'tax_code':tax_code,'items_count':items_count,'delivery_info':delivery_info,'lazada_order_id':lazada_order_id,
                      'gift_message':gift_message,'remarks':remarks,'request_id':request_id,'partner_id':partner_id
                    }
        
        sale_order_id=request.env['sale.order'].sudo().create(req_values)
        print("sale order id",sale_order_id.id)
        return "Response 200"


    @http.route('/sale_order_list_lazada/', auth='public',  method=["POST"],csrf=False, type='json')
    def sale_order_list_lazada(self, **kw):
        product_id=[]
        unit_price=[] 
        sale_order_id=0
        for item in kw['data']:
            product_name=item['name']
            product_unit_price=item['item_price']
            order_id=item['order_id']
            sale_order_id=order_id
            print(product_name)
            print(product_unit_price)
            product_vals={'name':product_name,'standard_price':product_unit_price}
            product=request.env['product.template'].sudo().create(product_vals)
            product_id.append(product.id)
            unit_price.append(product_unit_price)
            print("Product ID",product_id)
        
        sale_order = request.env['sale.order'].sudo().search([('id', '=', sale_order_id )])
        so_id=sale_order.id
        for line_item in product_id:
                req_vals={'order_id':so_id,'product_id':line_item}
                order_line=request.env['sale.order.line'].sudo().create(req_vals)
                print(order_line.id)
        print(sale_order.id,sale_order.name)
        
                
        
        
        return "Reponse 200"
