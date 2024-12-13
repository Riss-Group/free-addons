from odoo import models, fields, api
from odoo.exceptions import UserError


class IrModelFields(models.Model):
    _inherit = 'ir.model.fields'

    company_dependent = fields.Boolean(default=False)

    @api.onchange('company_dependent')
    def onchange_company_dependent(self):
        for rec in self:
            if rec.company_dependent:
                rec.copied = rec.stored = False

    @api.constrains('company_dependent')
    def _check_company_dependent(self):
        for rec in self:
            if rec.company_dependent and (rec.copied or rec.stored):
                raise UserError('A company dependent field cannot be set to copied or stored')

    def _instanciate_attrs(self, field_data):
        attrs = super()._instanciate_attrs(field_data)
        attrs['company_dependent'] = field_data['company_dependent']
        return attrs
