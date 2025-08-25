from odoo import models, fields


class ITAssetAccessory(models.Model):
    _name = 'it.asset.accessory'
    _description = 'Accessory Item'

    name = fields.Char(required=True)
    type = fields.Char()
    asset_id = fields.Many2one('it.asset', string="Main Asset")
