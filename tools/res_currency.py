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

database = 'iho120'
username = 'hector_herrera_mx@yahoo.com'
password = '1'

odoo = odoorpc.ODOO(url, protocol, port)
odoo.login(database, username, password)

rr = odoo.env.ref("base.USD")
print (rr)
print (rr.rate, rr.name, rr.id, rr.currency_unit_label)

rr = odoo.env.ref("base.MXN")
print (rr)
print (rr.rate, rr.name, rr.id, rr.currency_unit_label)
