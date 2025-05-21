from odoo import models,fields

class LoanManagerProductCycle(models.Model):
    _name = 'loan_manager.product_cycle'
    _description = 'Cycle number where loan limit is defined'

    name = fields.Char(string='Level name', required=True)
    cycle_number = fields.Integer(string='Cycle number', required=True)
    amount_limit = fields.Float(string='Amount limit', required=True)
