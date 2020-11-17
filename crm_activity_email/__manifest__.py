# -*- coding: utf-8 -*-
{
    'name': "Daily Activity Notification",

    'summary': """
        Everyday This module will send  their daily Activity Summary email notification to all users""",

    'description': """
         Everyday This module will send  their daily Activity Summary email notification to all users.
    """,

    'author': "Hunain AK",
    'website': "https:www.HAKSolutions",
    'maintainer': 'hunainfast@gmail.com',
    'license': 'AGPL-3',
    'category': 'crm',
    'version': '13.0',

    # any module necessary for this one to work correctly
    'depends': ['base','crm','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'images': ['static/description/icon.png'],
    'installable': True,
}
