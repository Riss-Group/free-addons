{
    'name': "Dimensions in Product UoM",

    'summary': """
        Eeach Unit of Measure has its dimensions. This is a technical module, functional behavior can be found in corresponding modules (stock_uom_dimension, sale_uom_dimension, purchase_uom_dimension).""",
    'author': "Captivea, BADEP",
    'website': "https://www.captivea.com",
    'category': 'Inventory',
    'version': '17.0.1.0.2',
    'depends': ['uom', 'product'],
    'images': ['static/src/img/banner.png'],
    'license': 'AGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/uom_view.xml',
    ],
    'installable': False,
}