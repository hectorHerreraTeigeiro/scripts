import odoorpc
from odoorpc.error import RPCError
from lxml import objectify

# Port and protocol for DeployV
# url = 'erp.mtnmx.com'
# protocol = 'jsonrpc+ssl'
# port = 443
# Port and protocol for Local:
url = 'localhost'
protocol = 'jsonrpc'
port = 8069

database = 'mt120'
username = 'hherrera@mtnmx.com'
password = 'gnEUsV8qZBJsMnT'

odoo = odoorpc.ODOO(url, protocol, port)
odoo.login(database, username, password)

prj_to_remove = 4180
prj_to_set = 5159
sale_orders = odoo.env['sale.order'].search([('account_analytic_tag_id', '=', prj_to_remove)])
for rec in sale_orders:
  rec.write({'account_analytic_tag_id': prj_to_set})

