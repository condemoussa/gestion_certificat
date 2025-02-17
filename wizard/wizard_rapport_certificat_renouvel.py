from odoo import models, fields, api,_


class RapportCertificatRenouvel(models.TransientModel):
    _name = 'rapport.certificat.renouvel'

    reference=fields.Char('Réference Certificat :')


    def action_certificat_renouvel_excel_xlsx(self, line=None):
        lines = []
        if self.reference:
            renouvel_certificat = self.env['certificat.renouvellement'].search([('cert_ref','=',self.reference)],order="cert_dat_expire asc")

        else:
            renouvel_certificat = self.env['certificat.renouvellement'].search([],order="cert_dat_expire asc")



        for line in renouvel_certificat:
            vals={
                'alert_id':line.alert_id.name,
                'cert_num':line.cert_num,
                'cert_ref':line.cert_ref,
                'cert_dat_expire':line.cert_dat_expire,
                'const_dat':line.const_dat,
                'confir_dat':line.confir_dat,
                'extrat1_dat':line.extrat1_dat,
                'cot_dat':line.cot_dat,
                'ach_dat':line.ach_dat,
                'ver_ach_dat':line.ver_ach_dat,
                'nouvel_ext_dat':line.nouvel_ext_dat,
                'transf_dat':line.transf_dat,
                'instal_dat':line.instal_dat,
                'ver_instal_dat':line.ver_instal_dat,
                'traitement':line.observat,
                'commentaire':line.alert_id.commt_certif
            }
            lines.append(vals)

        data = {'form_date': self.read()[0],
                'line_data':lines
                }


        return self.env.ref('gestion_certificat.atm_action_rapport_certificat_renouvel_xlsx').report_action(self, data=data)