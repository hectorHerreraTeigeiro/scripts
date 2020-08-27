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
password = '33'
odoo = odoorpc.ODOO(url, protocol, port)
odoo.login(database, username, password)

# looking for id at the bank statement line side   (19392)
absl_ids = odoo.env['account.bank.statement.line'].search(
	[('amount', '=', -62337.42),('name', '=', 'Pago a genetec')])
for rec in absl_ids:
    bank_line = odoo.env['account.bank.statement.line'].browse(rec)
    print(bank_line.id, bank_line.name, bank_line.journal_entry_ids)
# 19392 Pago a genetec Recordset('account.move.line', [])


# prod BDMJ1/2020/00004, BDMJ1/2020/00005, DPM/2020/0093
am_ids = odoo.env['account.move'].search(
    [('name', 'in', ['BDMJ1/2020/00004', 'BDMJ1/2020/00005', 'DPM/2020/0093'])])
print(am_ids)
all_ids = []
for rec in am_ids:
    acc_linea = odoo.env['account.move'].browse(rec)
    print(acc_linea.id, acc_linea.name, acc_linea.line_ids)
    for acc_linea_ids in acc_linea.line_ids:
        # all_ids += [acc_linea_ids.id]
        all_ids.append(acc_linea_ids.id)

print(all_ids)

odoo.execute('account.bank.statement.line', 'write', 
    absl_ids, {'journal_entry_ids': [(6,0,all_ids)]})
# el parametro absl_ids es el SELF;  {} son los 'vals'
# Otra opcion en vez de execute:
# for rec in absl_ids:
#     bank_line = odoo.env['account.bank.statement.line'].browse(rec)
#     bank_line.journal_entry_ids = all_ids
#     print(bank_line.id, bank_line.name, bank_line.journal_entry_ids)

print(bank_line.id, bank_line.name, bank_line.journal_entry_ids)
