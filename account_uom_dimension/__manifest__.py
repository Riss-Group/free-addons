{
    'name': "UoM Dimensions in Invoices",

    'summary': """
        Allows the use of UoM dimensions in invoices.""",
    'author': "Captivea, BADEP",
    'website': "https://www.captivea.com",
    'category': 'Invoicing Management',
    'version': '17.0.1.0.1',
    'images': ['static/src/img/banner.png'],
    'license': 'AGPL-3',
    'depends': ['account', 'uom_dimension'],
    'data': [
        'report/invoice_report_templates.xml',
        'views/invoice_views.xml',
        'security/ir.model.access.csv',
    ],
    'auto_install': True,
    'installable': False,
}
