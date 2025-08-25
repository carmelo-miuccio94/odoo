{
    'name': 'IT Asset Manager',
    'version': '1.0',
    'summary': 'Manage IT assets, assignments, and accessories',
    'depends': ['base', 'hr'],
    'author': 'Carmelo Miuccio',
    'category': 'Operations/Assets',
    'data': [
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/asset_views.xml',
        'views/assignment_views.xml',
        'views/accessory_views.xml',
    ],
    'installable': True,
}  # type: ignore
