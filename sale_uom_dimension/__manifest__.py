{
    'name': "UoM Dimensions in Sales",

    'summary': """
        Allows the use of UoM dimensions in sales.""",
    'author': "Captivea, BADEP",
    'website': "https://www.captivea.com",
    'category': 'Sales Management',
    'version': '17.0.1.0.1',
    'images': ['static/src/img/banner.png'],
    'license': 'AGPL-3',
    'depends': ['sale', 'uom_dimension'],
    'data': [
             'views/sale_views.xml',
             'report/sale_report_templates.xml',
             'security/ir.model.access.csv',
             ],
    'auto_install': True,
    'installable': False,
}