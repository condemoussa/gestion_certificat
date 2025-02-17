# -*-coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta

class GestionAlerty(models.Model):
    _name = 'gestion.alerty'
    _description = 'GESTION DES CERTIFICATS DES APPLICATIONS'
    _rename='name'

    #determiner le statut du certificat
    def statut_certificat(self):

        for line in self:
            if line.expiration_date <= line.dat_reference and line.expiration_date_pa > fields.Date.today() :
                line.update({'statute': 'reemission'})

            elif line.expiration_date_pa <= fields.Date.today():
                # Ajoutez votre logique ici, par exemple :
                line.update({'statute': 'renouvellement'})

            else:

                line.update({'statute': 'normal'})

    @api.model
    def _compute_state_color(self):
        today = fields.Date.today()
        self.statut_certificat()
        for certificate in self.search([]):
            delta = (certificate.expiration_date - today)
            if delta < timedelta(days=0):
                certificate.status = 'noir'
            elif delta < timedelta(days=30):
                certificate.status = 'red'
            elif delta < timedelta(days=45):
                certificate.status = 'orange'
            elif delta < timedelta(days=60):
                certificate.status = 'yellow'
            else:
                certificate.status = 'green'

    @staticmethod
    def _truncate_text(text, max_chars=30):
        # Fonction pour tronquer le texte à un nombre maximal de caractères
        if isinstance(text, str) and len(text) > max_chars:
            return text[:max_chars] + '...'
        return text


    def _compute_short_traitement(self):
        for record in self:
            record.traitement_certifi_short = self._truncate_text(record.traitement_certifi)
            record.commt_certif_short = self._truncate_text(record.commt_certif)


    numero = fields.Char("N°CL :",size=4)
    provenance_cert=fields.Selection([("public","Public"),("local","Local")],string="Public / Local :",default="public")
    reference=fields.Char('Référence :')
    name = fields.Char('Certificat :', )
    type_cert = fields.Selection([("type", "Licences"),("type2", "Certificats"),("type3", "Compte admin") ],string="Type :",default="type")
    expiration_date = fields.Date("Date d'expiration :",)
    expiration_date_pa=fields.Date("Date expire PA :")
    dat_achat=fields.Date("Date d'achat :")
    state=fields.Selection(
        [('active','Actif'),('desactive','Inactif'),('suspendre','Attente')],default="active" , string="Etat :"
    )
    status = fields.Selection([('green', 'Vert'),('orange', 'Bleu'),('red', 'Red'), ('yellow', 'Jaune'),('noir', 'Noir')
    ], string='Niveau ALT :', compute='_compute_state', store=True ,default='green')
    description=fields.Text('Traitement :' ,size=40 )
    application_id = fields.Many2one("atm.application" , string="Application :" , )
    nbre_jour=fields.Char("Nbre jour :" ,compute="_compute_state_color")
    traitement_certifi=fields.Text("Traitement :")
    traitement_certifi_short = fields.Text("Traitement :" ,compute="_compute_short_traitement")
    certificat_id=fields.Many2one("gestion.certificat" ,string="Certificat :")
    statute=fields.Selection([
                              ('normal', 'Normal'),
                              ('reemission', 'Réemission'),
                              ('renouvellement', 'Renouvellement')
                             ] ,default="normal" ,string="Statut")
    dat_reference = fields.Date('Réference :', default=lambda self: fields.Datetime.now() + timedelta(days=365),
                                readonly=True)
    rex_id=fields.Many2one("res.users" , string="Rex :")
    commt_certif=fields.Text("Commentaire ")
    commt_certif_short = fields.Text("Commentaire ")




