# -*- coding: utf-8 -*-
{
    'name': "Company dependent custom fields",

    'summary': """
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
        'base_import',
    ],
    'data': ['views/ir_model_fields_views.xml'],

    'installable': True,
    'auto_install': False,
    'application': False
}
