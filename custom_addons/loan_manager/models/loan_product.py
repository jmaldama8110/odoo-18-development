from odoo import api,models,fields
from datetime import date,timedelta

class LoanProduct(models.Model):
    _name="loan_manager.loan_product"
    _description = "Credit products where behavioural of loans are defined"

    name = fields.Char("Name",required=True)
    short_name= fields.Char("Short name",required=True)
    min_amount = fields.Float("Min Amount",required=True, default=5000)
    max_amount = fields.Float("Max Amount",required=True, default=500000)
    default_amount = fields.Float("Default amount",required=True,default=1000)
    step_amount = fields.Float(required=True, default=1000)

    interest_rate = fields.Float("Interest Rate",required=True,default=12)

    date_start = fields.Date("From",default=fields.Datetime.now)
    def _date_plus_one_month(self):
            today = fields.Date.today()
            return today + timedelta(days=365)
    date_end = fields.Date("To", default=_date_plus_one_month)

    state = fields.Selection([ ('d','Draft'),('a','Approved')],default='d',string='Status',required=True)
    product_type_id = fields.Many2one("loan_manager.loan_product.type", required=True)

    product_destination_ids = fields.Many2many("loan_manager.loan_product.dest", required=True)

    cycle_ids = fields.One2many("loan_manager.product_cycle","product_id")


    # loan calculator
    calc_loan_amount = fields.Float("Loan amount", required=True, default=1000)
    calc_frequency = fields.Selection([ ('w','Weekly'),('f','Fortnightly'),('m','Monthly')],default='m',string='Status')
    calc_term = fields.Integer("Term", default=6)
    calc_tax = fields.Float('Tax', default=0.16)

    calc_repay_amount = fields.Float(string="Repay amount")
    AQUI NOS QUEDAMOS

