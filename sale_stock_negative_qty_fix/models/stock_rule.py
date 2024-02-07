from odoo import models, fields, api

class StockRule(models.Model):
    _inherit = 'stock.rule'

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values):
        vals = super()._get_stock_move_values(product_id, product_qty, product_uom, location_id, name, origin, company_id, values)
        if not 'to_refund' in vals:
            vals.update({
                'to_refund': self._context.get('force_to_refund', False) and (product_qty < 0)
            })
        return vals