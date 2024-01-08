# -*- coding: utf-8 -*-
{
    'name': "Product Purchase Min Price",

    'summary': """
        Display min purchase price in product form""",

    'description': """
    """,

    'author': "Captivea, BADEP",
    'website': "https://www.captivea.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Purchase',
    'version': '17.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['purchase'],
    'images': ['static/src/img/banner.png'],
    'license': 'AGPL-3',

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_view.xml',
    ],
    'installable': False,
}