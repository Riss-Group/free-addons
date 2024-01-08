# -*- coding: utf-8 -*-
{
    'name': "MRP Routing",

    'summary': """Restore routing fuctionality in Odoo v14
        """,

    'description': """
    """,

    'author': "Captivea, BADEP",
    'website': "https://www.captivea.com",
    'category': 'Manufacturing',
    'version': '17.0.1',

    'depends': [
        'mrp'
    ],

    'data': [
        'data/mrp_data.xml',
        'security/ir.model.access.csv',
        'views/mrp_bom_views.xml',
        'views/mrp_production_views.xml',
        'views/mrp_routing_views.xml'
    ],

    'installable': False,
    'auto_install': True,
}
