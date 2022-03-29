import odoorpc, sys
from odoorpc.error import RPCError
from lxml import objectify

# run it from ~ as
# python3 ~/odoo/scripts/tools/project_usage_report.py 4879 4881

# Port and protocol for Production
url = 'erp.mtnmx.com'
protocol = 'jsonrpc+ssl'
port = 443
database = 'mtnmx120'

# Port and protocol for Local:
# url = 'localhost'
# protocol = 'jsonrpc'
# port = 8069
# database = 'mt120'

username = 'hherrera@mtnmx.com'
password = 'Ivan/2022/Fer'

odoo = odoorpc.ODOO(url, protocol, port)
odoo.login(database, username, password)

prj_to_remove = 4880
prj_to_set = 4881

# parameters loading
if len(sys.argv) == 3:
    prj_to_remove = int(sys.argv[1])
    prj_to_set = int(sys.argv[2])
else:
    print('Error: No parameters processed')
    print(str(sys.argv), '\n')

print('Setup')
prj_to_remove_rec = odoo.env['account.analytic.tag'].browse(prj_to_remove)
if prj_to_remove_rec:
    print(
        'prj_to_remove: [', prj_to_remove, '] [', 
        prj_to_remove_rec.create_date, '] [',
        prj_to_remove_rec.account_analytic_account_ids.name, '] [', 
        prj_to_remove_rec.user_id.name, '] [', 
        prj_to_remove_rec.name, ']')
else:
    print('prj_to_remove: [', prj_to_remove, ']  Error: Not found')

prj_to_set_rec = odoo.env['account.analytic.tag'].browse(prj_to_set)
if prj_to_set_rec:
    print(
        'prj_to_set:    [', prj_to_set, '] [', 
        prj_to_set_rec.create_date, '] [',
        prj_to_set_rec.account_analytic_account_ids.name, '] [', 
        prj_to_set_rec.user_id.name, '] [', 
        prj_to_set_rec.name, ']')
else:
    print('prj_to_set: [', prj_to_set, ']  Error: Not found')

print('\nSale Orders:')
sale_orders = odoo.env['sale.order'].search(
    [('account_analytic_tag_id', 'in', [prj_to_remove, prj_to_set])])
for rec in sale_orders:
    rec_rec = odoo.env['sale.order'].browse(rec)
    print(
        'to_remove: [' 
        if prj_to_remove == rec_rec.account_analytic_tag_id.id
        else 'to_set   : [', 
        rec_rec.id, '] [', rec_rec.name, '] [', 
        rec_rec.analytic_account_id.name, '] [',
        rec_rec.user_id.name, ']')

print('\nPurchase Orders:')
purchase_orders = odoo.env['purchase.order'].search(
    [('account_analytic_tag_id', 'in', [prj_to_remove, prj_to_set])])
for rec in purchase_orders:
    rec_rec = odoo.env['purchase.order'].browse(rec)
    print(
        'to_remove: [' 
        if prj_to_remove in rec_rec.account_analytic_tag_id.ids 
        else 'to_set   : [', 
        rec_rec.id, '] [', rec_rec.project_id.name, '] [', rec_rec.name, ']')

print('\nAccount Invoices:')
account_invoices = odoo.env['account.invoice'].search(
    [('account_analytic_tag_id', 'in', [prj_to_remove, prj_to_set])])
for rec in account_invoices:
    rec_rec = odoo.env['account.invoice'].browse(rec)
    print(
        'to_remove: [' 
        if prj_to_remove in rec_rec.account_analytic_tag_id.ids 
        else 'to_set   : [', 
        rec_rec.id, '] [', rec_rec.account_analytic_id.name, '] [',
        rec_rec.user_id.name, '] [', rec_rec.display_name, ']')

print('\nCustomers:')
customers = odoo.env['res.partner'].search(
    [('account_analytic_tag_ids', 'in', [prj_to_remove, prj_to_set])])
for rec in customers:
    rec_rec = odoo.env['res.partner'].browse(rec)
    if prj_to_remove in rec_rec.account_analytic_tag_ids.ids:
        print(
            'to_remove: [', rec_rec.id, '] [', 
            rec_rec.name, ']')
    if prj_to_set in rec_rec.account_analytic_tag_ids.ids:
        print('to_set   : [', rec_rec.id, '] [', rec_rec.name, ']')

print('\nJournal items:')
journal_items = odoo.env['account.move.line'].search(
    [('analytic_tag_ids', 'in', [prj_to_remove, prj_to_set])])
for rec in journal_items:
    rec_rec = odoo.env['account.move.line'].browse(rec)
    print(
        'to_remove: [' 
        if prj_to_remove in rec_rec.analytic_tag_ids.ids 
        else 'to_set   :[',
        rec_rec.id, '] [', 
        rec_rec.move_id.name, '] [', 
        rec_rec.account_id.code, '] [', 
        rec_rec.credit, '] [',
        rec_rec.debit, ']',)
