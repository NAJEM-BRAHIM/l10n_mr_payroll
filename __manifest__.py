# -*- coding: utf-8 -*-
{
    'name': 'Mauritanie - Règles Salariales (Payroll)',
    'version': '19.0.1.0.0',
    'category': 'Payroll/Localizations',
    'summary': 'Règles salariales pour la République Islamique de Mauritanie',
    'author': 'Localisation Mauritanie',
    'license': 'LGPL-3',
    'depends': ['hr_payroll'],
    'data': [
        'security/ir.model.access.csv',
        'data/hr_salary_rule_category_data.xml',
        'data/hr_payroll_structure_type_data.xml',
        'data/hr_payroll_structure_data.xml',
        'data/hr_salary_rule_data.xml',
        'views/hr_contract_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'post_init_hook': 'post_init_hook',
}
