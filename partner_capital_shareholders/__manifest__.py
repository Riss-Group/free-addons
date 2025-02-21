# -*- coding: utf-8 -*-
{
    'name': "Partner Shareholders",

    'summary': """Add shareholders info in partners and companies
        """,

    'description': """
    """,

    'author': "Captivea, BADEP",
    'website': "https://www.captivea.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Technical Settings',
    'version': '17.0.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'partner_capital',
        'base_partner_company_inherit'
    ],
    'data': [
        'views/res_company_views.xml',
        'views/res_partner_views.xml',
        'security/ir.model.access.csv'
    ],
    'installable': False,
}
