# -*- coding: utf-8 -*-
from odoo import http

# class Dotmatrix(http.Controller):
#     @http.route('/dotmatrix/dotmatrix/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dotmatrix/dotmatrix/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dotmatrix.listing', {
#             'root': '/dotmatrix/dotmatrix',
#             'objects': http.request.env['dotmatrix.dotmatrix'].search([]),
#         })

#     @http.route('/dotmatrix/dotmatrix/objects/<model("dotmatrix.dotmatrix"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dotmatrix.object', {
#             'object': obj
#         })