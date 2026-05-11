# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)

def post_init_hook(env):
    MRU = env.ref('base.MRU', raise_if_not_found=False)
    if not MRU:
        _logger.warning("Devise MRU introuvable.")
        return
    structure_type = env.ref(
        'l10n_mr_payroll.structure_type_employee_mr',
        raise_if_not_found=False
    )
    contracts = env['hr.contract'].search([
        ('structure_type_id', '=', False),
        ('company_id.currency_id', '=', MRU.id),
    ])
    if contracts:
        contracts.write({'structure_type_id': structure_type.id})
        _logger.info("Structure MR appliquée à %d contrat(s).", len(contracts))
