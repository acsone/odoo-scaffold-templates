# -*- coding: utf-8 -*-
##############################################################################
#
#     This file is part of {{ name }},
#     an Odoo module.
#
#     Copyright (c) 2015 ACSONE SA/NV (<http://acsone.eu>)
#
#     {{ name }} is free software:
#     you can redistribute it and/or modify it under the terms of the GNU
#     Affero General Public License as published by the Free Software
#     Foundation,either version 3 of the License, or (at your option) any
#     later version.
#
#     {{ name }} is distributed
#     in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
#     even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#     PURPOSE.  See the GNU Affero General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with {{ name }}.
#     If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "{{ name }}",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    # 'description': put the module description in README.rst

    'author': 'ACSONE SA/NV,'
              'Odoo Community Association (OCA)',
    'website': "http://acsone.eu",

    # Categories can be used to filter modules in modules listing
    # Check http://goo.gl/0TfwzD for the full list
    'category': 'Uncategorized',
    'version': '8.0.1.0.0',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}

