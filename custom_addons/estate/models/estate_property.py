from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Propiedad Inmobiliaria"

    name = fields.Char(string="Título", required=True)
    description = fields.Text(string="Descripción")
    postcode = fields.Char(string="Código Postal")
    date_availability = fields.Date(string="Fecha de Disponibilidad")
    expected_price = fields.Float(string="Precio Esperado", required=True)
    selling_price = fields.Float(string="Precio de Venta")
    bedrooms = fields.Integer(string="Habitaciones", default=2)
    living_area = fields.Integer(string="Área Habitable (m²)")
    facades = fields.Integer(string="Fachadas")
    garage = fields.Boolean(string="Cochera")
    garden = fields.Boolean(string="Jardín")
    garden_area = fields.Integer(string="Área del Jardín (m²)")
    garden_orientation = fields.Selection(
        selection=[
            ('north', 'Norte'),
            ('south', 'Sur'),
            ('east', 'Este'),
            ('west', 'Oeste'),
        ],
        string="Orientación del Jardín"
    )

    # Nuevos campos de relación
    property_type_id = fields.Many2one("estate.property.type", string="Tipo de Propiedad")
    tag_ids = fields.Many2many("estate.property.tag", string="Etiquetas")


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Tipo de Propiedad Inmobiliaria"

    name = fields.Char(string="Tipo", required=True)


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Etiqueta de Propiedad Inmobiliaria"

    name = fields.Char(string="Etiqueta", required=True)