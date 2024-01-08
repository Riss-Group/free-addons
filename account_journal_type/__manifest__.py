# -*- coding: utf-8 -*-
{
    'name': "Account Journal User type",

    'summary': """
        Add user-defined types to journals to help group journal by their nature (Payroll, etc.)""",

    'description': """
        
    """,

    'author': "Captivea, BADEP",
    'website': "https://www.captivea.com",

    'category': 'Invoicing &amp; Payments',
    'version': '17.0.1.0',

    'depends': ['account'],
    'images': ['static/src/img/banner.png'],
    'license': 'AGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/account_journal_views.xml',
        'views/account_journal_type_views.xml',
    ],
    'installable': False,
}