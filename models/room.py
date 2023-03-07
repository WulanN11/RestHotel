from unicodedata import name
from odoo import api, fields, models

class RoomHotel(models.Model):
    _name = 'hotel.rooms'
    _description = 'Room Hotel'

    name = fields.Selection(string='Nama Kamar', selection=[('ClasicStandar', 'ClasicS'), ('ClasicVip', 'ClasicV'),('ClasicVvip', 'ClasicVv'),('MonoStandar','MonoS'), ('MonoVip','MonoV'),('MonoVvip','MonoVv'),('BasicStandar','BasicS'),('BasicVip','BacicV'),('BacisVvip','BasicVv')])
    tipe = fields.Selection([
        ('standar', 'Standar'),
        ('vip', 'VIP'),
        ('vvip', 'VVIP')
    ], string='Tipe Kamar', required=True)
    harga = fields.Integer(string='Harga/hari', required=True)
    descrips = fields.Text(string='Deskripsi')
    img = fields.Binary(string='Image')
    
    
    