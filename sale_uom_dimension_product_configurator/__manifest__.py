{
    'name': "UoM Dimensions in Sales - Product Configurator",

    'summary': """
        Allows the use of UoM dimensions in sales with product configurator.""",
    'author': "Captivea, BADEP",
    'website': "https://www.captivea.com",
    'category': 'Sales Management',
    'version': '17.0.1.0.1',
    'images': ['static/src/img/banner.png'],
    'license': 'AGPL-3',
    'depends': ['sale_product_configurator', 'sale_uom_dimension'],
    'data': [
             'views/templates.xml',
             'views/sale_views.xml',
             'views/assets.xml',
             ],
    'auto_install': True,
    'installable': False,
}