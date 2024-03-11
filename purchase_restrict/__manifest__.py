# -*- coding: utf-8 -*-
{
    'name': "Purchase Restrict",
    'summary': """Module to restrict purchase creation for group of users""",
    'author': "Diego Marfil",
    'category': 'Purchase',
    'version': '16.0.1.0.0',
    'depends': ['purchase'],
    'data': [
        'security/groups.xml',
        'views/purchase_order_views.xml',
        'reports/report.xml',
    ],
}


