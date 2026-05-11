# -*- coding: utf-8 -*-
from odoo import api, fields, models

class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    l10n_mr_its_amount = fields.Monetary(
        string='ITS calculé', compute='_compute_l10n_mr_its', store=True)

    @api.depends('line_ids', 'line_ids.total')
    def _compute_l10n_mr_its(self):
        for slip in self:
            gross_line = slip.line_ids.filtered(lambda l: l.code == 'GROSS')
            gross = gross_line[0].total if gross_line else 0.0
            slip.l10n_mr_its_amount = self._calc_its(gross)

    @staticmethod
    def _calc_its(ri):
        tranches = [(6000,0.0),(9000,0.15),(21000,0.25),(45000,0.35),(float('inf'),0.40)]
        its, prev = 0.0, 0.0
        for p, t in tranches:
            if ri <= prev: break
            its += (min(ri, p) - prev) * t
            prev = p
        return round(its, 2)
