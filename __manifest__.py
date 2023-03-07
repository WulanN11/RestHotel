# -*- coding: utf-8 -*-
{
    'name': "RestHotel",
    'category': 'Services',
    'summary': 'Module for managing the Hotel',
    'sequence': '10',

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        "base",
    ],

    # always loaded
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu_views.xml',
        'views/room_views.xml',
        'views/canceled_views.xml',
        'views/confirmation_views.xml',
        'views/custemers_views.xml',
        'views/not_confirm_views.xml',
        'views/order_hotel_views.xml',
        'views/ordered_views.xml',
        #'views/akunting_views.xml',
        'report/invoicereport.xml',
        'report/report.xml',
        
       

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
