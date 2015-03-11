# -*- coding: utf-8 -*-
import os

from base import Report, DetailBand
from widgets import ObjectValue
from generators.pdf import PDFGenerator

here = os.path.dirname(__file__)

class reporte (Report):
    title = 'LIBRO IVA VENTAS - RESOLUCION GENERAL AFIP 3419'
    #page_size = landscape(A4)
    #first_page_number=7
    
    """def __init__(self, queryset=None, fpn=0):
        print "INIT DE REPORTE"
        Report.__init__(self, queryset=queryset)
        self.first_page_number=fpn
    
    class band_page_header(ReportBand):    
        height = 4*cm
        elements = [SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH, 
                                style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),
                    Label(text="RAZON SOCIAL: %s" %RAZON_SOCIAL_EMPRESA, top=0.8*cm, width=BAND_WIDTH, 
                          style={'fontName':'Helvetica','fontSize':10}),
                    Label(text="CUIT: %s" %CUIT, top=1.2*cm, width=BAND_WIDTH, 
                          style={'fontName':'Helvetica','fontSize':10}),
                    Label(text="DOMICILIO COMERCIAL: %s" %DOMICILIO_COMERCIAL, top=1.5*cm, width=BAND_WIDTH, 
                          style={'fontName':'Helvetica','fontSize':10}),
                    SystemField(expression='Periodo: %(var:periodo)s', top=1.5*cm, left=23*cm, 
                          style={'fontName':'Helvetica','fontSize':10}), 
                    SystemField(expression='Fecha emisión: %(now:%d/%m/%Y)s', top=2*cm, width=8*cm),
                    SystemField(expression='Folio N°: %(page_number)s', top=2*cm, left=23*cm, 
                          style={'fontName':'Helvetica','fontSize':10}),
                    Line(left=0, top=2.7*cm, right = 29.7*cm, bottom = 2.7*cm),
                    #Encabezado de tabla
                    Label(text="Fecha", top=2.9*cm, left=0, width=2*cm, style={'fontName':'Helvetica-Bold','fontSize':10,'alignment':TA_CENTER}),
                    Label(text="Comprobante", top=2.9*cm, left=2.1*cm, width=3.5*cm, style={'fontName':'Helvetica-Bold','fontSize':10,'alignment':TA_CENTER}),
                    Label(text="Razón Social", top=2.9*cm, left=5.7*cm, width=7*cm, style={'fontName':'Helvetica-Bold','fontSize':10,'alignment':TA_CENTER}),
                    Label(text="CUIT", top=2.9*cm, left=13.7*cm, width=2.5*cm, style={'fontName':'Helvetica-Bold','fontSize':10,'alignment':TA_CENTER}),
                    Label(text="Imp. Neto", top=2.9*cm, left=17.2*cm, width=2*cm, style={'fontName':'Helvetica-Bold','fontSize':10,'alignment':TA_CENTER}),
                    Label(text="IVA(10.5%)", top=2.9*cm, left=20.2*cm, width=2*cm, style={'fontName':'Helvetica-Bold','fontSize':10,'alignment':TA_CENTER}),
                    Label(text="IVA(21%)", top=2.9*cm, left=22.2*cm, width=2*cm, style={'fontName':'Helvetica-Bold','fontSize':10,'alignment':TA_CENTER}),
                    Label(text="Exento", top=2.9*cm, left=23.7*cm,width=2*cm, style={'fontName':'Helvetica-Bold','fontSize':10,'alignment':TA_CENTER}),
                    Label(text="Imp. Total", top=2.9*cm, left=26*cm, width=2*cm, style={'fontName':'Helvetica-Bold','fontSize':10,'alignment':TA_CENTER}),
                    Line(left=0, top=3.5*cm, right = 29.7*cm, bottom = 3.5*cm),]
    
    class band_page_footer(ReportBand):
        height = 1*cm
        elements=[SystemField(expression='Pagina N°: %(page_number)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                              style={'fontName':'Helvetica','fontSize':10, 'alignment':TA_CENTER}),]
    
    """    
    class band_detail(DetailBand):
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
    print "PYTHONPATH:"
    print os.environ['PYTHONPATH'].split(os.pathsep)
    nombres = ["Jorge","Daiana"]
    repo = reporte(queryset=nombres)
    repo.generate_by(PDFGenerator, filename=os.path.join(here, 'reporte.pdf'))