from odoo import api, fields, models, _
import time
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class sale(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'

    printer_data = fields.Text("Printer Data", readonly=True)

    @api.multi
    def action_refresh_printer_data(self):
        tmpl = self.env['mail.template'].search([('name','=','Dot Matrix SO')])
        data = tmpl._render_template( tmpl.body_html, 'sale.order', self.id )
        self.printer_data = data

    @api.multi
    def dummy(self):
        pass

    @api.multi
    def action_confirm(self):
        res = super(sale, self).action_confirm()
        self.action_refresh_printer_data()
        return res
