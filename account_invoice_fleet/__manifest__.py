# -*- coding: utf-8 -*-
{
    'name': "Account Invoice Fleet",

    'summary': """
        Link Invoices with Fleet""",

    'description': """
        Add vehicles and drivers assignation on Invoices. These Statistics can also be accessed directly from the vehicle view.
    """,

    'author': "Captivea, BADEP",
    'website': "https://www.captivea.com",

    'category': 'Invoicing &amp; Payments',
    'version': '17.0.2.0',

    'depends': ['account', 'fleet'],
    'images': ['static/src/img/banner.png'],
    'license': 'AGPL-3',
    'data': [
        'views/account_view.xml',
        'views/fleet_view.xml',
    ],
    'installable': True,
}