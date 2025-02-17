from odoo import models, fields, api,_


class RapportCertificat(models.TransientModel):
    _name = 'rapport.certificat'

    state= fields.Selection(
        [('green', 'Green'), ('orange', 'Orange'), ('red', 'Red'), ('yellow', 'Yellow'), ('noir', 'Noir')
         ], string='Niveau ALT :', store=True, default='green')


    def action_certificat_excel_xlsx(self):
        lines = []
        if self.state:
            data_certificat = self.env['gestion.certificat'].search([('status','=',self.state)])

        else:
            data_certificat = self.env['gestion.certificat'].search([])


        for line in data_certificat:
            vals = {
                'reference':line.numero,
                'numero': line.reference,
                'application_id':line.application_id.name,
                'name':line.name,
                'expiration_date':line.expiration_date,
                "status":line.status,
                "dat_achat":line.dat_achat,
                "provenance_cert":line.provenance_cert,
                "type_cert": line.type_cert,

            }
            lines.append(vals)

        data = {'form_date': self.read()[0],
                'line_data':lines
                }

        return self.env.ref('gestion_certificat.atm_action_rapport_certificat_xlsx').report_action(self, data=data)