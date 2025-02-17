# -*-coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta

class CertificatRenouvel(models.Model):
    _name = 'certificat.renouvellement'
    _description = "Renouvellement d'un certificat / d'une license"
    _rename = 'name'

    @api.model
    def create(self, vals):
        certifficat = self.env["gestion.alerty"].browse(self.alert_id.id)
        certifficat.update({"traitement_certifi": vals["observat"]})
        res= super(CertificatRenouvel, self).create(vals)
        if res:
            res["name"] = "/000" + str(res.id)
        return res

    def write(self, vals):
        res=super(CertificatRenouvel, self).write(vals)
        if res:
            certifficat=self.env["gestion.alerty"].browse(self.alert_id.id)
            certifficat.update({"traitement_certifi":self.observat})
        return res

    def imprimer_certificat_renouvel(self):

        selected_rows = self.env['certificat.renouvellement'].browse(self.env.context.get('active_ids', []))
        for row in selected_rows:
            certificat = self.env['certificat.renouvellement'].search_read([("cert_ref", "=", row.cert_ref)])

            data = {"line_data": certificat }


            return self.env.ref('gestion_certificat.atm_action_rapport_certificat_renouvel_xlsx').report_action(self, data=data)

    name = fields.Char("Index :")
    # certificat_id=fields.Many2one("gestion.certificat" , string="Certificat" ,domain="[('status', '=', 'yellow')]")
    alert_id = fields.Many2one("gestion.alerty", string="Certificat :" , required=True)
    cert_num= fields.Char( related='alert_id.numero',string="Numéro :",store=True)
    cert_ref= fields.Char( related='alert_id.reference',string="Référence :",store=True)
    applicate=fields.Many2one("atm.application" , related="alert_id.application_id" ,string="Application" , store=True)
    cert_status=fields.Selection( related='alert_id.status', readonly=True ,string="Référence :",store=True)
    cert_dat_expire = fields.Date( related='alert_id.expiration_date',string="Date d'Expiration :", readonly=True ,store=True)
    #partir renouvellement
    observat=fields.Text("Observation :" ,size=30)
    const_dat=fields.Date('Constate :' ,default=lambda self: fields.Datetime.now())
    confir_dat = fields.Date('Confirmation :' ,default=lambda self: fields.Datetime.now())
    extrat1_dat = fields.Date('Extraction :' ,default=lambda self: fields.Datetime.now())
    cot_dat = fields.Date('Cotation :' ,default=lambda self: fields.Datetime.now())
    ach_dat = fields.Date('Achat :' ,default=lambda self: fields.Datetime.now())
    ver_ach_dat = fields.Date('Verif Achat :',default=lambda self: fields.Datetime.now())
    nouvel_ext_dat = fields.Date('Nouvelle Extraction :' ,default=lambda self: fields.Datetime.now())
    transf_dat = fields.Date('Transfere Admin :' ,default=lambda self: fields.Datetime.now())
    instal_dat = fields.Date('Installation :' ,default=lambda self: fields.Datetime.now())
    ver_instal_dat = fields.Date('Verif Installation :' ,default=lambda self: fields.Datetime.now())
    dat_reference = fields.Date('Réference :', default=lambda self: fields.Datetime.now() + timedelta(days=365) ,readonly=True)







