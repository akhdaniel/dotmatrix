from odoo import api, fields, models, _
import time
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class invoice(models.Model):
    _name = 'account.invoice'
    _inherit = 'account.invoice'

    printer_data = fields.Text("Printer Data", readonly=True)

    @api.multi
    def action_refresh_printer_data(self):
        tmpl = self.env['mail.template'].search([('name','=','Dot Matrix Invoice')])
        data = tmpl._render_template( tmpl.body_html, 'account.invoice', self.id )
        self.printer_data = data

    @api.multi
    def dummy(self):
        pass


    @api.multi
    def action_invoice_open(self):
        res = super(invoice, self).action_invoice_open()
        self.action_refresh_printer_data()
        return res
