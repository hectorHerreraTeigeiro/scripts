import os
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

database = 'mtnmx100'
username = 'Soporte Jarsa'
password = '1'

odoo = odoorpc.ODOO(url, protocol, port)
odoo.login(database, username, password)

path = './'
files = os.listdir(path)

for file in files:
    if '.xml' in file:
        # This assumes that the file will be renamed id_invoice|name_of_xml.xml
        invoice_id = file.split('|')[0]
        invoice = odoo.env['account.invoice'].browse(int(invoice_id))
        xml_str = open(file).read()
        xml = objectify.fromstring(xml_str)
        attribute = 'tfd:TimbreFiscalDigital[1]'
        namespace = {'tfd': 'http://www.sat.gob.mx/TimbreFiscalDigital'}
        xml.Complemento.xpath(attribute, namespaces=namespace)
        uuid = xml.Complemento.xpath(
            attribute, namespaces=namespace)[0].get('UUID')
        fname = "%s_%s" % (
            invoice.company_id.partner_id.vat or '', invoice.move_name or '')
        count = odoo.env['ir.attachment'].search_count(
            [('name', 'like', fname),
             ('res_model', '=', 'account.invoice'),
             ('res_id', '=', invoice.id),
             ('mimetype', '=', 'application/xml'),
             ])
        if count > 0:
            fname += '_%s' % (count + 1)

        invoice.write({
            'cfdi_uuid': uuid,
            'xml_signed': xml_str,
            'l10n_mx_report_name': fname.replace('/', ''),
        })
        try:
            invoice.generate_xml_attachment()
        except RPCError:
            continue
