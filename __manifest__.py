# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2011 CCI Connect asbl (http://www.cciconnect.be) All Rights Reserved.
#                       Philmer <philmer@cciconnect.be>

{
    'name': 'CERTIFICATS SI',
    'version': '1.0',
    'category': 'Accounting/Accounting',
    'description': """
     un module permettant de gerer les certificats des application
     et le stats de la date d expiration
    """,
    'depends': ['base','web','mail','report_xlsx'],
    'data': [
        'security/ir.model.access.csv',
        #"security/security_gestion_certificat.xml",
        'views/certificat.xml',
        'wizard/wizard_mise_a_jour_date.xml',
        'views/renouvellement.xml',
        'views/alerty.xml',
        "automatisation/automatique.xml",
        "wizard/wizard_rapport_certificat_renouvel.xml",
        "wizard/wizard_rapport_certificat_alerte.xml",
        "wizard/wizard_rapport_certificat.xml",
        "wizard/liste_certificat_actif.xml",
        "views/menu_generale.xml",


    ],
    'assets': {
        'web.assets_backend': [
            "/gestion_certificat/static/src/css/ivoire_status.css",

        ]
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}
