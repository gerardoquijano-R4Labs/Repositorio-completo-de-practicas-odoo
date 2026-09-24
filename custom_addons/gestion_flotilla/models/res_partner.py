from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    es_conductor = fields.Boolean(string='Es Conductor', default=False)