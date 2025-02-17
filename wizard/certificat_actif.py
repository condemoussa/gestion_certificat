from odoo import models, fields, api,_


class CertificatActif(models.TransientModel):
    _name = 'certificat.actif'

    state = fields.Selection(
        [('actif', 'Actif')
         ], string='Actif :', store=True, default='actif' ,required=True)


    def action_certificat_actif_excel_xlsx(self, line=None):
        lines = []
        if self.state:
            actif_certificat = self.env['gestion.alerty'].search([('state','=',"active")])

        for line in actif_certificat:
            vals={
                'numero':line.numero,
                'provenance_cert':line.provenance_cert,
                'reference':line.reference,
                'name':line.name,
                'type_cert':line.type_cert,
                'expiration_date':line.expiration_date,
                'dat_achat':line.dat_achat,
                'state':line.state,
                'status':line.status,
                'description':line.traitement_certifi,
                'application_id':line.application_id.name,
                'date_pa':line.expiration_date_pa,
                'rex' :line.rex_id.name,
                'commtaire':line.commt_certif
            }
            lines.append(vals)

        data = {'form_date': self.read()[0],
                'line_data':lines
                }


        return self.env.ref('gestion_certificat.atm_action_rapport_certificat_actif_xlsx').report_action(self, data=data)