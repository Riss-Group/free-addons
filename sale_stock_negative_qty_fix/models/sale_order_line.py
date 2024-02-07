from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _action_launch_stock_rule(self, previous_product_uom_qty=False):
        super(SaleOrderLine, self.with_context(force_to_refund=True))._action_launch_stock_rule(previous_product_uom_qty)