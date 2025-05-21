from odoo import models, fields

class LoanProductDestination(models.Model):
    _name = 'loan_manager.loan_product.dest'
    _description = 'Define for example personal loans is used for consumption, repay debts, etc'

    name = fields.Char(string="Loan destination", required=True);
