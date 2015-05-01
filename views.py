from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import KeepTogether
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.colors import black, purple, white, yellow
from django.http import HttpResponse, response
import csv

# Set up response
response = HttpResponse(mimetype='application/pdf')
pdf_name = "Postal-address-list"
response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
styles = getSampleStyleSheet()
buff = StringIO()

pdf = SimpleDocTemplate(buff, rightMargin=72, leftMargin=30, topMargin=20, bottomMargin=1)

# container for pdf elements
Story = []

style = ParagraphStyle(
    'default',
    fontName='Times-Roman',
    fontSize=15,
    leading=20,
    leftIndent=0,
    rightIndent=0,
    firstLineIndent=0,
    alignment=TA_LEFT,
    spaceBefore=20,
    spaceAfter=0,
    bulletFontName='Times-Roman',
    bulletFontSize=10,
    bulletIndent=0,
    textColor= black,
    backColor=None,
    wordWrap=None,
    borderWidth= 1,
    borderPadding= 0,
    borderColor= black,
    borderRadius= None,
    allowWidows= 1,
    allowOrphans= 0,
    textTransform='None',  # 'uppercase' | 'lowercase' | None
    endDots=None,         
    splitLongWords=1,
)

with open('pathtopdffile') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for a in spamreader:
        for row in a:
            p = Preformatted(row.upper(), style)
            Story.append(KeepTogether(p))
            Story.append(Spacer(1,0.2*inch))

# Add the content as before then...
pdf.build(Story)
response.write(buff.getvalue())
buff.close()
return response
