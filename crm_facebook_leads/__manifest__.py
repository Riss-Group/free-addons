{
    'name': "CRM Facebook Lead Ads",
    'summary': """
        Sync Facebook Leads with Odoo CRM""",

    'description': """
    """,
    'author': "Captivea, BADEP, Vauxoo",
    'website': "https://www.captivea.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Lead Automation',
    'version': '17.0.2.0.1',

    'depends': ['crm'],
    'images': ['static/src/img/banner.png'],
    'license': 'AGPL-3',

    'data': [
        'data/ir_cron.xml',
        'data/crm.facebook.form.mapping.csv',
        'security/ir.model.access.csv',
        'views/crm_view.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': False,
}
