from odoo import models, fields, api,_


class RapportCertificatAlert(models.TransientModel):
    _name = 'rapport.certificat.alert'

    state = fields.Selection(
        [ ('orange', 'Orange'), ('red', 'Red'), ('yellow', 'Yellow'), ('noir', 'Noir')
         ], string='Rapport :', store=True, default='')


    def action_certificat_alert_excel_xlsx(self, line=None):
        lines = []
        if self.state:
            alert_certificat = self.env['gestion.alerty'].search([('status','=',self.state),('state','!=','desactive')],order="expiration_date asc")

        else:
            alert_certificat = self.env['gestion.alerty'].search([('status','!=','green'),('state','!=','desactive')],order="expiration_date asc")



        for line in alert_certificat:
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
                'comment':line.commt_certif
            }
            lines.append(vals)

        data = {'form_date': self.read()[0],
                'line_data':lines
                }


        return self.env.ref('gestion_certificat.atm_action_rapport_certificat_alert_xlsx').report_action(self, data=data)