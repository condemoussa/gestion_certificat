# -*-coding: utf-8 -*-
from odoo import models, fields, api , _
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta
import re

class GestionCertificat(models.Model):
    _name = 'gestion.certificat'
    _description = 'Certification des applications'
    _rename='name'

    @api.constrains("expiration_date", "expiration_date_pa")
    def _check_date_range(self):
        for line in self:
            if line.expiration_date and line.expiration_date_pa:
                if line.expiration_date > line.expiration_date_pa:
                    raise models.ValidationError("La date d'expiration ne peut pas etre postérieure à la date expire PA ")

    @api.constrains('numero', 'reference', 'name')
    def _check_unique_record(self):
        if not re.match("^[a-zA-Z0-9\-._]*$", self.name):
            raise ValidationError("Le nom du  Certificat ne peut contenir que des lettres , des chiffres et (-)")

        for record in self:
            # Recherche d'autres enregistrements avec les mêmes valeurs pour les champs
            certificat = self.env['gestion.certificat'].search([('name', '=', record.name), ('id', '!=', record.id)])
            if certificat:
                raise ValidationError("Ce certificat existe déjà !")

    @api.onchange('dat_achat')
    def compute_expiry_dates(self):
        """
        Compute expiration date and expiration date PA based on the date of purchase.
        """
        for record in self:
            if record.dat_achat:
                # Convert the date of purchase to a datetime object
                date_of_purchase =fields.Datetime.from_string(record.dat_achat).date()

                # Calculate expiration date by adding 2 years to the date of purchase
                expiration_date = date_of_purchase + timedelta(days=365 * 2)

                # Calculate expiration date PA by adding 2 years and 1 day to the date of purchase
                expiration_date_pa = date_of_purchase + timedelta(days=365 * 2 + 330)


                # Update the record with the computed dates
                record.update({
                    'expiration_date': expiration_date,
                    'expiration_date_pa': expiration_date_pa,
                })

    @api.model
    def create(self,vals):
        res=super(GestionCertificat,self).create(vals)
        if res:
           res["numero"]="000"+str(res.id)
           record=self.env["gestion.alerty"].create({
                       "numero":res['numero'],
                       "provenance_cert": res['provenance_cert'],
                       "reference": res['reference'],
                       "name": res['name'],
                       "type_cert": res['type_cert'],
                       "expiration_date": res['expiration_date'],
                       "expiration_date_pa":res['expiration_date_pa'],
                       "dat_achat": res['dat_achat'],
                       "state": res['state'],
                       "status": res['status'],
                       "description": res['description'],
                       "application_id": res.application_id.id,
                       "certificat_id" :res.id,
                       "rex_id" :res.rex_cert.id,
                       "commt_certif":res.comment_certif
           })
            
        return res

    def write(self, vals):
        res = super(GestionCertificat, self).write(vals)
        certificat_alert = self.env["gestion.alerty"].search([("certificat_id","=",self.id)])

        if res:
            if "name" in vals and self.name:
                certificat_alert.write({
                    "name": vals["name"]
                })
            if "reference" in vals and self.reference:
                certificat_alert.write({
                    "reference": vals["reference"]
                })
            if "numero" in vals and self.numero:
                certificat_alert.write({
                    "numero": vals["numero"]
                })
            if "provenance_cert" in vals and self.provenance_cert:
                certificat_alert.write({
                    "provenance_cert": vals["provenance_cert"]
                })
            if "type_cert" in vals and self.type_cert:
                certificat_alert.write({
                    "type_cert": vals["type_cert"]
                })
            if "dat_achat" in vals and self.dat_achat:
                certificat_alert.write({
                    "dat_achat": vals["dat_achat"]
                })
            if "expiration_date" in vals and self.expiration_date:
                certificat_alert.write({
                    "expiration_date": vals["expiration_date"]
                })
            if "expiration_date_pa" in vals and self.expiration_date_pa:
                certificat_alert.write({
                    "expiration_date_pa": vals["expiration_date_pa"]
                })
            if "state" in vals and self.state:
                certificat_alert.write({
                    "state": vals["state"]
                })
            if "application_id" in vals and self.application_id:
                certificat_alert.write({
                    "application_id": vals["application_id"]
                })
            if "rex_cert" in vals and self.rex_cert:
                certificat_alert.write({
                    "rex_id": vals["rex_cert"]
                })
            if "comment_certif" in vals and self.comment_certif:
                certificat_alert.write({
                    "commt_certif": vals["comment_certif"]
                })


        return res

    def unlink(self):
        for line in self.filtered('id'):
            certificat_alert = self.env["gestion.alerty"].search(
                [('certificat_id', '=', line.id)])
            certificat_alert.unlink()

        super(GestionCertificat, self).unlink()
        return True

    @staticmethod
    def _truncate_text(text, max_chars=30):
        # Fonction pour tronquer le texte à un nombre maximal de caractères
        if isinstance(text, str) and len(text) > max_chars:
            return text[:max_chars] + '...'
        return text

    @api.depends('dat_achat')
    def _compute_short_description(self):
        for record in self:
            record.comment_certif_short = self._truncate_text(record.comment_certif)


    numero = fields.Char("N°CL :",size=5,readonly=True)
    provenance_cert=fields.Selection([("public","Public"),("local","Local")],string="Public / Local :",default="public")
    reference=fields.Char('Référence :')
    name = fields.Char('Certificat :', required=True)
    type_cert = fields.Selection([("type", "Licence"),("type2", "Certificat"),("type3", "Compte admin") ],string="Type :",default="type")
    expiration_date = fields.Date("Date d'expiration :", required=True)
    expiration_date_pa = fields.Date("Date exp PA :")
    dat_achat=fields.Date("Date achat :")
    state=fields.Selection(
        [('active','Actif'),('desactive','inactif'),('suspendre','Attente')],default="active" , string="Etat :"
    )
    status = fields.Selection([('green', 'Green'),('orange', 'Orange'),('red', 'Red'), ('yellow', 'Yellow'),('noir', 'Noir')
    ], string='Niveau ALT :',  store=True ,default='green')
    description=fields.Text('Traitement :' ,size=40 )
    application_id = fields.Many2one("atm.application" , string="Application :" )
    nbre_jour=fields.Char("Nbre jour ")
    rex_cert=fields.Many2one("res.users" ,string="Rex :")
    comment_certif = fields.Text("Commentaire :")
    comment_certif_short=fields.Text("Commentaire :" ,compute="_compute_short_description")



