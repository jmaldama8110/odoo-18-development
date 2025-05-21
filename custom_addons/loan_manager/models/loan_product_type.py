from odoo import models,fields

class LoanType(models.Model):
    _name = "loan_manager.loan_product.type"
    _description = "Model to define the type of loan product"

    name = fields.Char(string="Name", required=True)