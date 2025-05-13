from odoo import models,fields

class LoanProduct(models.Model):
    _name="loan_manager.loan_product"
    _description = "Credit products where behavioural of loans are defined"

    name = fields.Char()
    short_name= fields.Char(required=True)
    min_amount = fields.Float(required=True, default=1000)
    max_amount = fields.Float(required=True, default=5000)

    interest_rate = fields.Float(required=True,default=12)