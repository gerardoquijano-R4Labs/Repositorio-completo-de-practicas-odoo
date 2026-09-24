{
    'name': 'Gestión de Flotilla',
    'version': '1.0',
    'summary': 'Módulo para administración de vehículos',
    'category': 'Operations',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/flotilla_vehiculo_views.xml',
        'views/res_partner_views.xml'
    ],
    'installable': True,
    'application': True,
}