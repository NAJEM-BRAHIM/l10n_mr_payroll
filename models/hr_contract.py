# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class HrContract(models.Model):
    _inherit = 'hr.contract'

    l10n_mr_is_resident = fields.Boolean(string='Résident mauritanien', default=True)
    l10n_mr_transport_allowance = fields.Monetary(string='Indemnité de transport (MRU)', default=0.0)
    l10n_mr_housing_allowance = fields.Monetary(string='Indemnité de logement (MRU)', default=0.0)
    l10n_mr_meal_allowance = fields.Monetary(string='Indemnité de repas (MRU)', default=0.0)
    l10n_mr_seniority_years = fields.Integer(string="Ancienneté (années)", compute='_compute_seniority_years', store=True)
    l10n_mr_annual_leave_days = fields.Integer(string="Jours de congés annuels", compute='_compute_annual_leave_days', store=True)
    l10n_mr_overtime_hours = fields.Float(string="H. supp. jour (x1,15)", default=0.0)
    l10n_mr_overtime_night_hours = fields.Float(string="H. supp. nuit (x1,40)", default=0.0)
    l10n_mr_overtime_rest_hours = fields.Float(string="H. supp. repos (x1,50)", default=0.0)

    @api.depends('date_start')
    def _compute_seniority_years(self):
        from datetime import date
        today = date.today()
        for contract in self:
            if contract.date_start:
                contract.l10n_mr_seniority_years = (today - contract.date_start).days // 365
            else:
                contract.l10n_mr_seniority_years = 0

    @api.depends('l10n_mr_seniority_years', 'l10n_mr_is_resident')
    def _compute_annual_leave_days(self):
        for contract in self:
            y = contract.l10n_mr_seniority_years
            base = 36 if not contract.l10n_mr_is_resident else 18
            bonus = 3 if y >= 20 else 2 if y >= 15 else 1 if y >= 10 else 0
            contract.l10n_mr_annual_leave_days = min(base + bonus, 30)

    @api.constrains('wage')
    def _check_smig(self):
        SMIG = 30000.0
        for c in self:
            if c.company_id.currency_id.name == 'MRU' and c.wage < SMIG:
                raise ValidationError(
                    _("Salaire %.2f MRU < SMIG légal (30 000 MRU)") % c.wage)
