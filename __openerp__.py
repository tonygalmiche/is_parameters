# -*- coding: utf-8 -*-

{
    'name': u'Paramétrage des modules',
    'version': '1.0',
    'category': 'InfoSaone',
    'description': """
Parametrage des modules
    """,
    'author': 'Tony GALMICHE / Asma BOUSSELMI',
    'maintainer': 'InfoSaone',
    'website': 'http://www.infosaone.com',
    'depends': ['base', 'mail'
                , 'sale', 'crm', 'sale_stock', 'delivery', 'sale_journal'
                , 'stock', 'purchase', 'purchase_analytic_plans'
                , 'mrp', 'mrp_byproduct', 'mrp_operations'
                , 'account_voucher', 'account_accountant'],
    'data': ['is_config_view.xml'],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: