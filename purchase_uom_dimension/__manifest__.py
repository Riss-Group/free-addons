{
    'name': "UoM Dimensions in purchases",

    'summary': """
        Allows the use of UoM dimensions in purchases.""",
    'author': "Captivea, BADEP",
    'website': "https://www.captivea.com",
    'category': 'purchases Management',
    'version': '17.0.1.0.1',
    'images': ['static/src/img/banner.png'],
    'license': 'AGPL-3',
    'depends': ['purchase', 'uom_dimension'],
    'data': [
             'views/purchase_views.xml',
             'report/purchase_report_templates.xml',
             'security/ir.model.access.csv',
             ],
    'auto_install': False,
    'installable': False,
}