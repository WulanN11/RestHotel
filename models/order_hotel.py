import code
from re import search
from odoo import api, fields, models
import datetime
import random
from odoo.exceptions import ValidationError

class OrderHotel(models.Model):
    _name = 'hotel.orderhotel'
    _descripton = "For Order Hotel"

    name = fields.Many2one(comodel_name='res.partner', string='Nama Pemesan',  required=True, domain="[('is_custommer','=',True)]")
    tgl_check_in = fields.Date(string='Tanggal Check In', default=fields.Datetime.now, required=True)
    tgl_check_out = fields.Date(string='Tanggal Check Out', required=True)
    detailorder_ids = fields.One2many('hotel.detailorder', 'order_id', string='DETAIL ORDER')
    jml_hari = fields.Integer(compute="_compute_jml_hari", string='Total Hari', readonly=True, store=True)
    jml_harga = fields.Integer(compute='_compute_jml_harga', string='Total Harga')
    tagihan = fields.Integer(compute='_compute_tagihan', string='Total Tagihan')
    no_confirm = fields.Char(string='Kode Konfirmasi', readonly=True, store=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Konfirmasi'),
        ('pay', 'Menunggu Konfirmasi Pembayaran....'),
        ('done', 'Terkonfirmasi'),
        ('not_confirm', 'Ditolak'),
        ('cancel', 'Batal'),
    ], string='States', default='draft', tracking=True)

    def action_draft(self):
        self.state = 'draft'

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'
        code = True
        while code:
            rand_code = random.sample(range(1000,1999),1)
            mycode = "HIT" + str(rand_code[0])
            search_code = self.env['hotel.orderhotel'].search([('no_confirm','=',mycode)])
            if len(search_code) < 1:
                self.no_confirm = mycode
                break

    def action_cancel(self):
        self.state = 'cancel'

    def action_pay(self):
        self.state = 'pay'

    def action_not_confirm(self):
        self.state = 'not_confirm'

    
    
    
    @api.model
    def _compute_jml_harga(self):
        for record in self:
            total = sum(self.env['hotel.detailorder'].search([('order_id','=',record.id)]).mapped('total_harga'))
            record.jml_harga = total

    
    
    @api.depends('tgl_check_in','tgl_check_out')
    def _compute_jml_hari(self):
        for record in self:
            if record.tgl_check_out and record.tgl_check_in:
                to_date = fields.Datetime.to_datetime(record.tgl_check_out)
                from_date = fields.Datetime.to_datetime(record.tgl_check_in)
                record.jml_hari = int(((to_date - from_date)).days)
    
    @api.depends('jml_harga','jml_hari')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.jml_hari*record.jml_harga
    
class OrderHotel(models.Model):
    _name = 'hotel.detailorder' 
    _descripton = "Detail Order Room"


    name = fields.Char(string='Kode Order')
    order_id = fields.Many2one('hotel.orderhotel', string='Order Hotel')
    models_id = fields.Many2one('hotel.rooms', string='Tipe Kamar')
    jml_kamar = fields.Integer(string='Jumlah Kamar', default=1)
    harga = fields.Integer(compute='_compute_no_kamar', string='Harga/hari')
    total_harga = fields.Integer(compute='_compute_total_harga', string='Total Harga')
    
    @api.depends('harga','jml_kamar')
    def _compute_total_harga(self):
        for record in self:
            record.total_harga = record.jml_kamar * record.harga
    
    @api.depends('models_id')
    def _compute_no_kamar(self):
        for record in self:
            record.harga = record.models_id.harga
            