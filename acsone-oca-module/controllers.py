{%- set mod = name|snake -%}
{%- set model = "%s.%s"|format(mod, mod) -%}
{%- set root = "/%s/%s"|format(mod, mod) -%}
# -*- coding: utf-8 -*-
##############################################################################
#
#     This file is part of {{ name }}, an Odoo module.
#
#     Copyright (c) 2015 ACSONE SA/NV (<http://acsone.eu>)
#
#     {{ name }} is free software: you can redistribute it and/or
#     modify it under the terms of the GNU Affero General Public License
#     as published by the Free Software Foundation, either version 3 of
#     the License, or (at your option) any later version.
#
#     {{ name }} is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.
#
#     You should have received a copy of the
#     GNU Affero General Public License
#     along with {{ name }}.
#     If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import http

# class {{ mod|pascal }}(http.Controller):
#     @http.route('{{ root }}/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('{{ root }}/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('{{ mod }}.listing', {
#             'root': '{{ root }}',
#             'objects': http.request.env['{{ model }}'].search([]),
#         })

#     @http.route('{{ root }}/objects/<model("{{ model }}"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('{{ mod }}.object', {
#             'object': obj
#         })
