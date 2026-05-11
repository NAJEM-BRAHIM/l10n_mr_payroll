# -*- coding: utf-8 -*-
from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    l10n_mr_smig = fields.Float(string='SMIG (MRU)', default=30000.0, config_parameter='l10n_mr_payroll.smig')
    l10n_mr_cnss_employer_rate = fields.Float(string='CNSS Employeur (%)', default=15.0, config_parameter='l10n_mr_payroll.cnss_employer_rate')
    l10n_mr_cnss_employee_rate = fields.Float(string='CNSS Salarié (%)', default=1.0, config_parameter='l10n_mr_payroll.cnss_employee_rate')
    l10n_mr_cnam_rate = fields.Float(string='CNAM Salarié (%)', default=4.0, config_parameter='l10n_mr_payroll.cnam_rate')
