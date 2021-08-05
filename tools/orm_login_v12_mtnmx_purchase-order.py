import odoorpc
from odoorpc.error import RPCError
from lxml import objectify

url = 'erp.mtnmx.com'
# Port and protocol for DeployV
protocol = 'jsonrpc+ssl'
port = 443
# Port and protocol for Local
# protocol = 'jsonrpc'
# port = 8069

database = 'mtnmx120'
username = 'Soporte Jarsa'
password = '1'

odoo = odoorpc.ODOO(url, protocol, port)
odoo.login(database, username, password)

po_id = odoo.env['purchase.order'].browse(20467)
for line in po_id.order_line:
    print(line.product_id.name, '<*>', line.product_id.categ_id.name, '<*>', line.product_id.default_code, line.product_id.default_code[:7])

not all(line.product_id.default_code and line.product_id.default_code[:7] == 'SP Cont' for line in po_id.order_line)
