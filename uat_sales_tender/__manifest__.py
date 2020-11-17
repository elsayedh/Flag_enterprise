# -*- coding: utf-8 -*-
{
    'name': "UAT Sales Tenders",

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
    'depends': ['base', 'sale', 'stock', 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/sales_tender_security.xml',
        'views/sales_tender.xml',
        'views/sales_tender_report.xml',
        'views/tender_document_view.xml',
        'views/product_tender_document_view.xml',
        'views/supplier_tender.xml',
        'views/supplier_documents.xml',
        'data/sequence.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/icon.png'],

}
