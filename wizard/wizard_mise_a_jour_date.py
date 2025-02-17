# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import datetime, timedelta

class MiseDate(models.TransientModel):
    _name = 'mise.date'
    _description = "Mise a jour de la date d'expiration"



    mse_date=fields.Date("Nvlle date d'expire :",default=lambda self: fields.Datetime.now() + timedelta(days=365 * 2))
    mse_dat_pa=fields.Date("Nouvelle date PA :" ,default=lambda self: fields.Datetime.now() + timedelta(days=365 * 2 + 335))


    def test(self):
        active_id = self.env.context.get('active_id')
        active_model = self.env[self.env.context.get('active_model')]
        active_record = active_model.browse(active_id)
        if active_record.ver_instal_dat:
            active_record.alert_id.update({'expiration_date': self.mse_date,
                                           'expiration_date_pa': self.mse_dat_pa,
                                           'status': 'green'})
            active_record.alert_id.certificat_id.update({'expiration_date': self.mse_date,
                                           'expiration_date_pa': self.mse_dat_pa,
                                           'status': 'green'})
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'type': 'success',
                    'message': _("La nouvelle date d'expiration a été ajoutée avec succès par %s", self.env.user.name),
                    'next': {'type': 'ir.actions.act_window_close'},
                }
            }
        else:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'type': 'danger',
                    'message': _("Veuillez vérifier l'installation du nouveau serveur avant la mise à jour des dates"),
                    'next': {'type': 'ir.actions.act_window_close'},
                }
            }



