import odoorpc
from odoorpc.error import RPCError
from lxml import objectify

url = 'localhost'
# Port and protocol for DeployV
# protocol = 'jsonrpc+ssl'
# port = 443
# Port and protocol for Local
protocol = 'jsonrpc'
port = 8069

database = 'iho130'
username = 'hector.herrera.mx@gmail.com'
password = '2MJmw8CQiLhfYnf'

odoo = odoorpc.ODOO(url, protocol, port)
odoo.login(database, username, password)
