{
    "name": """Restrict out-of-stock POS Orders""",
    "summary": """Restrict payments for out-of-stock products in POS""",
    "category": "Point Of Sale",
    # "live_test_url": "http://apps.it-projects.info/shop/product/DEMO-URL?version={ODOO_BRANCH}",
    "images": [],
    "version": "12.0.1.0.1",
    "application": False,

    "author": "IT-Projects LLC, Ivan Yelizariev",
    "support": "pos@it-projects.info",
    "website": "https://apps.odoo.com/apps/modules/12.0/pos_product_available_negative/",
    "license": "LGPL-3",
    "price": 50.00,
    "currency": "EUR",

    "depends": [
        "pos_pin",
        "pos_product_available",
    ],
    'data': [
        'data.xml',
        'views.xml',
    ],

    "price": 50.00,
    "currency": "EUR",

    'installable': True,
}
