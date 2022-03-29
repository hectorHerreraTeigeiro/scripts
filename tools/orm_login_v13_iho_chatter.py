import odoorpc
from odoorpc.error import RPCError
from lxml import objectify

url = 'erp.iho.com.mx'
# Port and protocol for DeployV
protocol = 'jsonrpc+ssl'
port = 443
# Port and protocol for Local
# protocol = 'jsonrpc'
# port = 8069

database = 'iho130'
username = 'hector_herrera_mx@yahoo.com'
password = 'yahoo'

odoo = odoorpc.ODOO(url, protocol, port)
odoo.login(database, username, password)

saleid = odoo.env['sale.order'].search([('name', '=', 'QPY003036')])
saleorderrecord = odoo.env['sale.order'].browse(saleid)
allpartners = saleorderrecord.message_partner_ids
