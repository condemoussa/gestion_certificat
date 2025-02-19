import base64
import io
from odoo import models
from datetime import datetime

class RapportCertificatsActif(models.AbstractModel):
    _name = 'report.gestion_certificat.wizard_rapport_actif_certificat'
    _inherit = 'report.report_xlsx.abstract'


    def generate_xlsx_report(self, workbook, data, partners):
        form_data=data['form_date']
        data_payroll=data['line_data']
        sheet = workbook.add_worksheet('RAPPORT DES CERTIFICATS ACTIFS')

        #styles de livre de paie
        header_format = workbook.add_format(
            {'align': 'center', 'valign': 'vcenter', 'bold': 'TRUE', 'size':15,'color':'orange'})
        header_format_titre = workbook.add_format(
            {'border': 2, 'align': 'center', 'valign': 'vcenter', 'bold': 'TRUE', 'size': 7})
        header_format11 = workbook.add_format(
            {'border': 1,'bg_color':'white','color':'orange', 'align': 'center', 'valign': 'vcenter', 'bold': 'TRUE', 'size': 10})
        header_format12 = workbook.add_format(
            {'border': 1, 'align': 'center', 'valign': 'vcenter', 'size': 8})


        sheet.merge_range('D3:H3', "LA LISTE DES CERTFICATS ACTIF", header_format)
        sheet.set_column('B:B', 14)
        sheet.set_column('C:C', 15)
        sheet.set_column('D:D', 30)
        sheet.set_column('E:E', 40)
        sheet.set_column('F:F', 20)
        sheet.set_column('G:G', 30)
        sheet.set_column('H:H', 15)
        sheet.set_column('I:I', 16)
        sheet.set_column('J:J', 20)
        sheet.set_column('K:K', 20)
        sheet.set_column('L:L', 10)
        sheet.set_column('M:M', 15)
        sheet.set_column('N:N', 60)
        sheet.set_column('O:O', 60)
        row=5
        col=1

        sheet.write(row, col, 'NUMÉRO', header_format11)
        sheet.write(row, col + 1, ' PROVENANCE ', header_format11)
        sheet.write(row, col + 2, 'RÉFÉRENCE', header_format11)
        sheet.write(row, col + 3, 'CERTIFICAT', header_format11)
        sheet.write(row, col + 4, 'REX', header_format11)
        sheet.write(row, col + 5, 'APPLICATION', header_format11)
        sheet.write(row, col + 6, "TYPE", header_format11)
        sheet.write(row, col + 7, "DATE D'ACHAT", header_format11)
        sheet.write(row, col + 8, "DATE D'EXPIRATON", header_format11)
        sheet.write(row, col + 9, "DATE EXPIRE PA", header_format11)
        sheet.write(row, col + 10, 'ETAT', header_format11)
        sheet.write(row, col + 11, 'NIVEAU ALT', header_format11)
        sheet.write(row, col + 12, 'TRAITEMENT', header_format11)
        sheet.write(row, col + 13, 'COMMENTAIRES', header_format11)
        row+=1

        for line in range(len(data_payroll)):
            if data_payroll[line]['status'] =='red':
                background = workbook.add_format({'bg_color': 'red', 'align': 'center',
                                                  'valign': 'vcenter', 'size': 8,'color':'white',
                                                  'bold': 'TRUE'
                                                  })
            elif data_payroll[line]['status'] =='green':
                background = workbook.add_format(
                    {'bg_color': 'green', 'align': 'center', 'valign': 'vcenter', 'size': 8,
                     'color': 'white','bold': 'TRUE'})
            elif data_payroll[line]['status'] =='yellow':
                background = workbook.add_format(
                    {'bg_color': 'yellow', 'align': 'center', 'valign': 'vcenter', 'size': 8,
                     'color': 'white','bold': 'TRUE'})
            elif data_payroll[line]['status'] == 'noir':
                background = workbook.add_format(
                    {'bg_color': 'black', 'align': 'center', 'valign': 'vcenter', 'size': 8,
                     'color': 'white','bold': 'TRUE'})
            else:
                background = workbook.add_format(
                    {'bg_color': 'orange', 'align': 'center', 'valign': 'vcenter', 'size': 8,
                     'color': 'white','bold': 'TRUE'})

            sheet.write(row, col, data_payroll[line]['numero'], background)
            sheet.write(row, col + 1, 'Public' if data_payroll[line]['provenance_cert'] == 'public' else 'Local',   background)
            sheet.write(row, col + 2, data_payroll[line]['reference'] if data_payroll[line]['reference'] else "", background)
            sheet.write(row, col + 3, data_payroll[line]['name'], background)
            sheet.write(row, col + 4, data_payroll[line]['rex'] if data_payroll[line]['rex'] else "", background)
            sheet.write(row, col + 5, data_payroll[line]['application_id'] if data_payroll[line]['application_id'] else "", background)
            sheet.write(row, col + 6,'Licence' if data_payroll[line]['type_cert'] == 'type' else 'Certificat' if data_payroll[line][ 'type_cert'] == 'type2' else 'CompteAdmin', background)

            sheet.write(row, col + 7,data_payroll[line]['dat_achat'], background)

            sheet.write(row, col + 8,data_payroll[line]['expiration_date'], background)

            sheet.write(row, col + 9,data_payroll[line]['date_pa'], background)
            sheet.write(row, col + 10,'Actif' if data_payroll[line]['state'] == 'active' else 'Inactif' if data_payroll[line][ 'state'] == 'desactive' else 'Attente', background)
            sheet.write(row, col + 11, data_payroll[line]['status'] if data_payroll[line]['status'] else "",  background)
            sheet.write(row, col + 12, data_payroll[line]['description'] if data_payroll[line]['description'] else "",background)
            sheet.write(row, col + 13, data_payroll[line]['commtaire'] if data_payroll[line]['commtaire'] else "", background)


            row += 1
        row+=1






