from odoo import api, fields, models, _
import time
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class po(models.Model):
    _name = 'purchase.order'
    _inherit = 'purchase.order'

    printer_data = fields.Text("Printer Data", readonly=True)

    @api.multi
    def action_refresh_printer_data(self):
        tmpl = self.env['mail.template'].search([('name','=','Dot Matrix PO')])
        data = tmpl._render_template( tmpl.body_html, 'purchase.order', self.id )
        self.printer_data = data

    @api.multi
    def dummy(self):
        pass


    @api.multi
    def button_confirm(self):
        res = super(po, self).button_confirm()
        self.action_refresh_printer_data()
        return res
