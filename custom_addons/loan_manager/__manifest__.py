{
    'name': "Loan Manager Module",
    'version': '1.0',
    'author': "Josman Gmz",
    'description': """
        Loan Application manager to manage loan portfolio
    """,
    'depends': ['base'],
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/loan_manager_loan_product_views.xml',
        'views/loan_manager_menus.xml',
        'views/loan_manager_product_view_list.xml',
        'views/loan_manager_product_view_form.xml',
        'views/loan_manager_product_view_search.xml'

    ]

}