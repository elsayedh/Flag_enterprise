# -*- coding: utf-8 -*-
{
    'name': "Sales Report",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/sales_custom_security.xml',
        'security/sequence.xml',
        'views/sales_custom_report.xml',
        'views/sales_custom_report_ar.xml',
        'views/sales_custom_report_ar2.xml',
        'views/sales_custom_report_en.xml',
        'views/sales_custom_report_en2.xml',
        'views/report_inherit.xml',
        'views/views.xml',
        'views/template.xml',
        'invoice/invoice_report.xml',
        'invoice/invoice_report_en.xml',
        'invoice/invoice_report_en2.xml',
        'invoice/invoice_report_ar.xml',
        'invoice/invoice_report_ar2.xml',
        'invoice/invoice_relations.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
