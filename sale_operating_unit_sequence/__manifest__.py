# -*- coding: utf-8 -*-
{
    'name': "Sale operating Unit Sequence",

    'summary': """
        Add OU specific sequence for sale orders""",

    'author': "Captivea, BADEP",
    'website': "https://www.captivea.com",

    'category': 'Sales',
    'version': '17.0.1.0',

    'depends': ['sale_operating_unit'],
    'images': ['static/src/img/banner.png'],
    'license': 'AGPL-3',
    'data': [
        'views/sequence_view.xml',
    ],
    'installable': False,
}