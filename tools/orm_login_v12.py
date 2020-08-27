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
