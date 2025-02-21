{
    'name': "Website Sale Stock Warehouse",

    'summary': """
        Choose proper warehouse when sale order is generated from website""",
    'author': "Captivea, BADEP",
    'website': "https://www.captivea.com",
    'category': 'Sales Management',
    'version': '17.0.1.0.1',
    'images': ['static/src/img/banner.png'],
    'license': 'AGPL-3',
    'depends': ['website_sale_stock'],
    'data': [
             'views/res_config_settings_views.xml',
             ],
    'auto_install': True,
    'installable': False,
}