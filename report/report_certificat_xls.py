import base64
import io
from odoo import models

class RapportCertificats(models.AbstractModel):
    _name = 'report.gestion_certificat.wizard_rapport_xlsx_certificat'
    _inherit = 'report.report_xlsx.abstract'


    def generate_xlsx_report(self, workbook, data, partners):
        form_data=data['form_date']
        data_payroll=data['line_data']
        sheet = workbook.add_worksheet('RAPPORT DE CERTIFICATS')

        #styles de livre de paie
        header_format = workbook.add_format(
            {'align': 'center', 'valign': 'vcenter', 'bold': 'TRUE', 'size':15,'color':'orange'})
        header_format_titre = workbook.add_format(
            {'border': 2, 'align': 'center', 'valign': 'vcenter', 'bold': 'TRUE', 'size': 7})
        header_format11 = workbook.add_format(
            {'border': 2,'bg_color':'blue','color':'white', 'align': 'center', 'valign': 'vcenter', 'bold': 'TRUE', 'size': 10})
        header_format12 = workbook.add_format(
            {'border': 1, 'align': 'center', 'valign': 'vcenter', 'size': 8})


        sheet.merge_range('D3:H3', "LA LISTE DES CERTFICATS DE GS2E", header_format)
        sheet.set_column('B:B',20)
        sheet.set_column('C:C', 10)
        sheet.set_column('D:D', 20)
        sheet.set_column('E:E', 20)
        sheet.set_column('F:F', 18)
        sheet.set_column('G:G', 10)
        sheet.set_column('H:H', 15)
        sheet.set_column('I:I', 16)
        sheet.set_column('J:J', 10)
        row=5
        col=1

        sheet.write(row,col,'RÉFERENCE',header_format11)
        sheet.write(row, col + 1, ' NUMÉRO ', header_format11)
        sheet.write(row, col + 2, 'APPLICATION', header_format11)
        sheet.write(row, col + 3, 'CERTIFICAT', header_format11)
        sheet.write(row, col + 4, "DATE D'EXPIRATION",header_format11)
        sheet.write(row, col +5 , 'STATUS',header_format11)
        sheet.write(row, col + 6, "DATE D'ACHAT",header_format11)
        sheet.write(row, col +7, ' PROVENANCE',header_format11)
        sheet.write(row, col + 8, 'TYPE',header_format11)
        row+=1

        for line in range(len(data_payroll)):

            sheet.write(row, col, data_payroll[line]['reference'] , header_format12)
            sheet.write(row, col + 1,data_payroll[line]['numero'], header_format12)
            sheet.write(row, col + 2, data_payroll[line]['application_id'], header_format12)
            sheet.write(row, col + 3, data_payroll[line]['name'], header_format12)
            sheet.write(row, col + 4, data_payroll[line]['expiration_date'], header_format12)
            sheet.write(row, col + 5, data_payroll[line]['status'], header_format12)
            sheet.write(row, col + 6, data_payroll[line]['dat_achat'], header_format12)
            sheet.write(row, col + 7,data_payroll[line]['provenance_cert'], header_format12)
            sheet.write(row, col + 8, data_payroll[line]['type_cert'], header_format12)
            row += 1
        row+=1






