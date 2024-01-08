# -*- coding: utf-8 -*-
{
    'name': 'Fleet Maps',
    'version': '17.0.1.0.2',
    'author': 'Yopi Angi, BADEP',
    'license': 'AGPL-3',
    'website': 'https://badep.ma',
    'maintainer': 'Yopi Angi <yopiangi@gmail.com>, Khalid Hazam <k.hazam@badep.ma>',
    'category': 'Fleet',
    'description': """
Fleet Maps
==========

Show your fleet on map view
""",
    'depends': [
        'fleet',
        'web_google_maps'
    ],
    'data': [
        'views/fleet_vehicle.xml'
    ],
    'demo': [],
    'installable': False,
    'uninstall_hook': 'uninstall_hook',
}
