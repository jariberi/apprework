# -*- coding: utf-8 -*-
import os

from base import Report, DetailBand, ReportBand
from widgets import ObjectValue, SystemField
from generators.pdf import PDFGenerator
from utils import cm, BAND_WIDTH
from reportlab.lib.enums import TA_CENTER

here = os.path.dirname(__file__)

class reporte (Report):
    title = 'LIBRO IVA VENTAS - RESOLUCION GENERAL AFIP 3419'
    #page_size = landscape(A4)
    #first_page_number=7
    
    def __init__(self, queryset=None, fpn=1):
        print "INIT DE REPORTE"
        Report.__init__(self, queryset=queryset)
        self.first_page_number=fpn
        print self.first_page_number
    
    class band_page_header(ReportBand):    
        height = 4*cm
        elements = [SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH, 
                                style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),
                    SystemField(expression='Fecha emisión: %(now:%d/%m/%Y)s', top=2*cm, width=8*cm),
                    SystemField(expression='Folio N°: %(page_number)s', top=2*cm, left=15*cm, 
                          style={'fontName':'Helvetica','fontSize':10}),]
                    
    
    class band_page_footer(ReportBand):
        height = 1*cm
        elements=[SystemField(expression='Pagina N°: %(page_number_1)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                              style={'fontName':'Helvetica','fontSize':10, 'alignment':TA_CENTER}),]
        
    class band_detail(DetailBand):
        height = 2*cm
        elements = [ObjectValue(attribute_name='capitalize'),
                    ]
        
    """
    class band_summary(ReportBand):
        margin_top = 3*cm
        height = 0.5*cm
        elements = [
            ObjectValue(attribute_name='neto', top=0.1*cm, left=16.9*cm, width=2*cm,\
                action=FIELD_ACTION_SUM, get_value=lambda instance: float("%.2f" %(instance.neto*-1) if instance.tipo.startswith("NC") else "%.2f" %instance.neto), style={'alignment':TA_RIGHT}),
            ObjectValue(attribute_name='iva21', top=0.1*cm, left=21.4*cm,width=2*cm,\
                action=FIELD_ACTION_SUM, get_value=lambda instance: float("%.2f" %(instance.iva21*-1) if instance.tipo.startswith("NC") else "%.2f" %instance.iva21), style={'alignment':TA_RIGHT}),
            ObjectValue(attribute_name='total', top=0.1*cm, left=26*cm, width=2*cm,\
                action=FIELD_ACTION_SUM, get_value=lambda instance: float("%.2f" %(instance.total*-1) if instance.tipo.startswith("NC") else "%.2f" %instance.total), style={'alignment':TA_RIGHT}),]
        borders = {'all': RoundRect(radius=5, fill_color=grey, fill=True)}
    """   

if __name__ == '__main__':
    print "COMIENZO MINI TEST"
    #print "PYTHONPATH:"
    #print os.environ['PYTHONPATH'].split(os.pathsep)
    nombres = ["Jorge",
               "Daiana",
               "Appline",
               "Jorge",
               "Daiana",
               "Appline",
               "Jorge",
               "Daiana",
               "Appline",
               "Jorge",
               "Daiana",
               "Appline",
               "Jorge",
               "Daiana",
               "Appline",
               "Jorge",
               "Daiana",
               "Appline",
               "Jorge",
               "Daiana",
               "Appline",
               "Jorge",
               "Daiana",
               "Appline",
               "Jorge",
               "Daiana",
               "Appline",
               "Jorge",
               "Daiana",
               "Appline",
               "Jorge",
               "Daiana",
               "Appline",
               "Jorge",
               "Daiana",
               "Appline",
               "Jorge",
               "Daiana",
               "Appline",
               "Jorge",
               "Daiana",
               "Appline"]
    print "COMIENZO A ARMAR EL REPORTE"
    repo = reporte(queryset=nombres, fpn=5)
    repo.generate_by(PDFGenerator, filename=os.path.join(here, 'reporte.pdf'))