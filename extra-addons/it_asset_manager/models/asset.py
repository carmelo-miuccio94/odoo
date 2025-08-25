from odoo import models, fields


class ITAsset(models.Model):
    _name = "it.asset"
    _description = "IT Asset"

    name = fields.Char(string="Asset Tag", require=True)
    serial_number = fields.Char()
    category = fields.Selection([
        ('laptop', 'Laptop'),
        ('monitor', 'Monitor'),
        ('phone', 'Phone'),
        ('accessory', 'Accessory'),
        ('other', 'Other')
    ])  # type: ignore | the selection argument in fields.Selection(...) isn’t fully typed in Odoo’s stubs.
    brand = fields.Char()
    model = fields.Char()
    purchase_date = fields.Date()
    warranty_expiration = fields.Date()
    status = fields.Selection([
        ('available', 'Available'),
        ('assigned', 'Assigned'),
        ('maintenance', 'In Maintenance'),
        ('retired', 'Retired')
    ], default="available")  # type: ignore
    assigned_to = fields.Many2one('hr.employee')
    accessories_ids = fields.One2many('it.asset.accessory', 'asset_id')
