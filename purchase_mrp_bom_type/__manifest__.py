{
    'name': 'Purchase MRP Separate BOM Type',
    'author': 'BADEP',
    'version': '17.0.0.1',
    'category': 'Hidden',
    'description': """
Allow to define a bom type for purchases different than that of sales
    """,
    'depends': ['purchase_mrp'],
    'data': [
        'views/bom_views.xml'
    ],
    'installable': False,
}
