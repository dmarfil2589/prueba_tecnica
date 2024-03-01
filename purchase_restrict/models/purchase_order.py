# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
     _inherit = 'purchase.order'

     random_product_id = fields.Many2one("product.product")

     @api.model_create_multi
     def create(self, vals):
         allow_to_create_users = self.env.user.has_group('purchase_restrict.restrict_user_purchase_creation')
         if not allow_to_create_users:
             raise UserError(_("User is not allowed to create purchase orders."))
         return super(PurchaseOrder, self).create(vals)


