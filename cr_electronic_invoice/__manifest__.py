# -*- coding: utf-8 -*-

{
    'name': 'Facturación electrónica Costa Rica',
	'version': '0.2',
	'author': 'CRLibre.org',
	'license': 'AGPL-3',
	'website': 'https://crlibre.org/',
	'category': 'Account',
	'description':
		'''
		Facturación electronica Costa Rica.
		''',
	'depends': ['base', 'account', 'product', 'sale_management', 'sales_team', 'account_invoicing', 'l10n_cr_country_codes', 'account_cancel', 'res_currency_cr_adapter', ],
	'data': ['data/data.xml',
             'data/code.type.product.csv',
             'data/identification.type.csv',
             'data/payment.methods.csv',
             'data/reference.code.csv',
             'data/reference.document.csv',
             'data/sale.conditions.csv',
             'data/product.uom.csv',
             'data/mail_template_data.xml',
             'data/aut.ex.csv',
             'data/sequence.xml',
             'views/uom_views.xml',
             'views/account_invoice_views.xml',
             'views/account_journal_views.xml',
             'views/account_payment_views.xml',
             'views/code_type_product_views.xml',
             'views/exoneration_views.xml',
             'views/identification_type_views.xml',
             'views/product_views.xml',
             'views/reference_document_views.xml',
             'views/res_company_views.xml',
             'views/res_config_settings_views.xml',
             'views/res_partner_views.xml',
             'views/resolution_views.xml',
             'views/sale_condition_views.xml',
             'security/ir.model.access.csv',
             'views/menu_views.xml',
             ],
    'installable': True,
}
