{
    'name': "Android Support",

    'summary': """Add Android app support""",

    'author': "Captivea, BADEP",
    'website': "https://www.captivea.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Discuss',
    'version': '17.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail_notify'],
    'images': ['static/src/img/banner.png'],
    'license': 'AGPL-3',
    # always loaded
    'data': [
        'views/assets.xml',
    ],
    'installable': False,
}