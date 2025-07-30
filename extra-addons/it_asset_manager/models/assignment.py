from odoo import models, fields


class ITAssetAssignment(models.Model):
    _name = 'it.asset.assignment'
    _description = 'IT Asset Assignment'

    employee_id = fields.Many2one('hr.employee', required=True)
    asset_id = fields.Many2one('it.asset', required=True)
    date_assigned = fields.Date(default=fields.Date.today)
    due_date = fields.Date()
    date_returned = fields.Date()
    note = fields.Text()
