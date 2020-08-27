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

user_ids = odoo.env['res.users'].search([('active', '=', True)])
for user_id in user_ids:
    user = odoo.env['res.users'].browse(user_id)
    print(user.name, user.login, user.password)
