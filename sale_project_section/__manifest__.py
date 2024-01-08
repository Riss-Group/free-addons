# -*- coding: utf-8 -*-
{
    'name': "Sale Project Section",

    'summary': """
        Generate parent tasks for project sections
    """,

    'description': """
        This module will automatically generate parent tasks for sections in sale orders. each task will have the corresponding sale order lines within that section as subtasks.
    """,

    'author': "Captivea, BADEP",
    'website': "https://www.captivea.com",

    'category': 'Hidden',
    'version': '17.0.2.0',

    'depends': ['sale_project'],
    'images': ['static/src/img/banner.png'],
    'license': 'AGPL-3',
    'data': [
    ],
    'installable': False,
}