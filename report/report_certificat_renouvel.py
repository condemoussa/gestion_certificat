import base64
import io
from odoo import models
from datetime import datetime

class RapportCertificats(models.AbstractModel):
    _name = 'report.gestion_certificat.wizard_rapport_renoul_certificat'
    _inherit = 'report.report_xlsx.abstract'


    def generate_xlsx_report(self, workbook, data, partners):
        # form_data=data['form_date']
        data_payroll=data['line_data']
        sheet = workbook.add_worksheet('RAPPORT DE CERTIFICATS RENOUVEL')

        #styles de livre de paie
        header_format = workbook.add_format(
            {'align': 'center', 'valign': 'vcenter', 'bold': 'TRUE', 'size':15,'color':'orange'})
        header_format_titre = workbook.add_format(
            {'border': 2, 'align': 'center', 'valign': 'vcenter', 'bold': 'TRUE', 'size': 7})
        header_format11 = workbook.add_format(
            {'border': 2,'bg_color':'white','color':'orange', 'align': 'center', 'valign': 'vcenter', 'bold': 'TRUE', 'size': 10})
        header_format12 = workbook.add_format(
            {'border': 1, 'align': 'center', 'valign': 'vcenter', 'size': 8})


        sheet.merge_range('D3:H3', "LA LISTE DES CERTFICATS DE GS2E", header_format)
        sheet.set_column('B:B',50)
        sheet.set_column('C:C', 20)
        sheet.set_column('D:D', 30)
        sheet.set_column('E:E', 20)
        sheet.set_column('F:F', 18)
        sheet.set_column('G:G', 20)
        sheet.set_column('H:H', 20)
        sheet.set_column('I:I', 20)
        sheet.set_column('J:J', 20)
        sheet.set_column('K:K', 28)
        sheet.set_column('L:L', 28)
        sheet.set_column('M:M', 20)
        sheet.set_column('N:N', 20)
        sheet.set_column('O:O', 60)
        sheet.set_column('P:P', 60)
        row=5
        col=1

        sheet.write(row,col,'CERTIFICAT',header_format11)
        sheet.write(row, col + 1, ' NUMÉRO ', header_format11)
        sheet.write(row, col + 2, 'RÉFÉRENCE', header_format11)
        sheet.write(row, col + 3, "DATE D'EXPIRATION", header_format11)
        sheet.write(row, col + 4, "DATE DE CONSTAT",header_format11)
        sheet.write(row, col + 5, 'DATE DE CONFIRMATION',header_format11)
        sheet.write(row, col + 6, "DATE D'EXTRACTION",header_format11)
        sheet.write(row, col + 7, ' DATE DE COTATION',header_format11)
        sheet.write(row, col + 8, "DATE D'ACHAT",header_format11)
        sheet.write(row, col + 9, "DATE DE VERIFICATION ACHAT", header_format11)
        sheet.write(row, col + 10, "NOUVELLE DATE D'EXTRACTION", header_format11)
        sheet.write(row, col + 11, 'DATE DE TRANSFÈRE', header_format11)
        sheet.write(row, col + 12, "DATE D'INSTALLATION", header_format11)
        sheet.write(row, col + 13, "TRAITEMENT", header_format11)
        sheet.write(row, col + 14, "COMMENTAIRE", header_format11)
        row+=1

        for line in range(len(data_payroll)):

            sheet.write(row, col, data_payroll[line]['alert_id'] , header_format12)
            sheet.write(row, col + 1,data_payroll[line]['cert_num'], header_format12)
            sheet.write(row, col + 2, data_payroll[line]['cert_ref'], header_format12)
            date_str = data_payroll[line]['cert_dat_expire']
            date_object = datetime.strptime(date_str, '%Y-%m-%d')
            formatted_date = date_object.strftime('%d/%m/%Y')
            sheet.write(row, col + 3,formatted_date, header_format12)
            date_str = data_payroll[line]['const_dat']
            date_object = datetime.strptime(date_str, '%Y-%m-%d')
            formatted_date = date_object.strftime('%d/%m/%Y')
            sheet.write(row, col + 4,formatted_date, header_format12)
            date_str = data_payroll[line]['confir_dat']
            date_object = datetime.strptime(date_str, '%Y-%m-%d')
            formatted_date = date_object.strftime('%d/%m/%Y')
            sheet.write(row, col + 5,formatted_date, header_format12)
            # date_str = data_payroll[line]['extrat1_dat']
            # date_object = datetime.strptime(date_str, '%Y-%m-%d')
            # formatted_date = date_object.strftime('%d/%m/%Y')
            sheet.write(row, col + 6, data_payroll[line]['extrat1_dat'], header_format12)
            # date_str = data_payroll[line]['cot_dat']
            # date_object = datetime.strptime(date_str, '%Y-%m-%d')
            # formatted_date = date_object.strftime('%d/%m/%Y')
            sheet.write(row, col + 7,data_payroll[line]['cot_dat'], header_format12)
            # date_str = data_payroll[line]['ach_dat']
            # date_object = datetime.strptime(date_str, '%Y-%m-%d')
            # formatted_date = date_object.strftime('%d/%m/%Y')
            sheet.write(row, col + 8, data_payroll[line]['ach_dat'], header_format12)
            # date_str = data_payroll[line]['ver_ach_dat']
            # date_object = datetime.strptime(date_str, '%Y-%m-%d')
            # formatted_date = date_object.strftime('%d/%m/%Y')
            sheet.write(row, col + 9,data_payroll[line]['ver_ach_dat'], header_format12)
            # date_str = data_payroll[line]['nouvel_ext_dat']
            # date_object = datetime.strptime(date_str, '%Y-%m-%d')
            # formatted_date = date_object.strftime('%d/%m/%Y')
            sheet.write(row, col + 10,data_payroll[line]['nouvel_ext_dat'], header_format12)
            # date_str = data_payroll[line]['transf_dat']
            # date_object = datetime.strptime(date_str, '%Y-%m-%d')
            # formatted_date = date_object.strftime('%d/%m/%Y')
            sheet.write(row, col + 11,data_payroll[line]['transf_dat'], header_format12)
            # date_str = data_payroll[line]['instal_dat']
            # date_object = datetime.strptime(date_str, '%Y-%m-%d')
            # formatted_date = date_object.strftime('%d/%m/%Y')
            sheet.write(row, col + 12,data_payroll[line]['transf_dat'], header_format12)
            sheet.write(row, col + 13, data_payroll[line]['traitement'] if data_payroll[line]['traitement'] else "",  header_format12)
            sheet.write(row, col + 14, data_payroll[line]['commentaire'] if data_payroll[line]['commentaire'] else "",header_format12)


            row += 1
        row+=1






