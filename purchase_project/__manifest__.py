{
    'name': "Purchase Project",

    'summary': """
        Link Purchases with Project""",

    'description': """
    """,

    'author': "Captivea, BADEP",
    'website': "https://www.captivea.com",

    'category': 'Project',
    'version': '17.0.1.0',

    'depends': ['project_purchase_link'],
    'images': ['static/src/img/banner.png'],
    'license': 'AGPL-3',
    'data': [
        'views/project_project_views.xml',
        'views/project_task_views.xml',
        'views/purchase_views.xml',
    ],
    'installable': False,
}