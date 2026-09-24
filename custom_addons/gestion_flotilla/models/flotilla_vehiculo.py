from odoo import models, fields

class FlotillaVehiculo(models.Model):
    _name = 'flotilla.vehiculo'
    _description = 'Vehículo de la Flotilla'

    placa = fields.Char(string='Placa', required=True)
    modelo = fields.Char(string='Modelo', required=True)
    conductor_id = fields.Many2one('res.partner', string='Conductor')