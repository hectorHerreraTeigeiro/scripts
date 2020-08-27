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

>>> print( odoo.env['account.move.line'].browse(578134).tax_ids )
[]

>>> print(odoo.env['account.move.line'].browse(578134).move_id.name)
TIMP/2018/13768

>>> print(odoo.env['account.move.line'].browse(578134).move_id.line_ids)
Recordset('account.move.line', [578135, 578134, 568315, 568314, 568313, 568312])

>>> for rec in odoo.env['account.move.line'].browse(578134).move_id.line_ids:
...     print(rec.tax_ids)
...     
... 
Recordset('account.tax', [])
Recordset('account.tax', [])
Recordset('account.tax', [])
Recordset('account.tax', [43])
Recordset('account.tax', [])
Recordset('account.tax', [43])
 

aml_ids = odoo.env['account.move.line'].search([('id','=',568314)])

aml_ids = odoo.env['account.move.line'].search([('company_id','!=',3),('tax_ids','!=',False)])
for aml_id in aml_ids: 
    tax_ids = odoo.env['account.move.line'].browse(aml_id).tax_ids
    for tax_id in tax_ids:
        if tax_id == 90:
            print (aml_id)
