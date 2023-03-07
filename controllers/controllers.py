# -*- coding: utf-8 -*-
# from odoo import http


# class RestHotel(http.Controller):
#     @http.route('/rest_hotel/rest_hotel/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rest_hotel/rest_hotel/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rest_hotel.listing', {
#             'root': '/rest_hotel/rest_hotel',
#             'objects': http.request.env['rest_hotel.rest_hotel'].search([]),
#         })

#     @http.route('/rest_hotel/rest_hotel/objects/<model("rest_hotel.rest_hotel"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rest_hotel.object', {
#             'object': obj
#         })
