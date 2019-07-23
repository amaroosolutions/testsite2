# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2018-today Ascetic Business Solution <www.asceticbs.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

## Inherit class sale.order.line for validate amount of product
class HolidaysAllocation(models.Model):
    _inherit = "hr.leave.allocation"

    @api.multi
    @api.constrains('holiday_status_id')
    def _check_leave_type_validity(self):
        for allocation in self:
            if allocation.holiday_status_id.validity_stop:
                
                vstop = allocation.holiday_status_id.validity_stop
                today = fields.Date.today()

                if vstop < today:
                    raise UserError(_('You can only allocate %s upto %s') % (allocation.holiday_status_id.display_name, allocation.holiday_status_id.validity_stop))

