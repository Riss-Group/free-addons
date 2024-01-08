# -*- coding: utf-8 -*-
{
    'name': "Document Folder",

    'summary': """Structure attachments in folders. Compatible with Odoo Enterprise
        """,

    'description': """
    """,

    'author': "Captivea, BADEP",
    'website': "https://www.captivea.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Technical Settings',
    'version': '17.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'attachment_indexation'
    ],

    'data': [
        'views/attachment_views.xml',
        'security/attachment_security.xml',
        'security/ir.model.access.csv'
             ],

    'installable': False,
    'auto_install': True,
}
