from fpdf import FPDF
from dates import getdays

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)

days = getdays(2021,1)
pdf.image('background.png',0,0,230,400)
pdf.set_text_color(255,255,255)
for y, day in enumerate(days):
    pdf.set_xy(95,y*7+55)
    pdf.cell(40,10,day['day'])
    pdf.set_xy(105,y*7+55)
    pdf.cell(40,10,str(day['number']))
    pdf.set_draw_color(100,100,100)
    #pdf.line(10,y*7+56,200,y*7+56)
    #if y == len(days):
    #    pdf.line(10,y+2*7+56,200,y+2*7+56)

pdf.output('January.pdf', 'F')