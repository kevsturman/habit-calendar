from PIL import Image, ImageDraw, ImageFont
from dates import getdays
im = Image.open("tracks.png").convert("RGB")

im = im.resize((2480,3508))
d = ImageDraw.Draw(im,"RGBA")
months = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]


d.rectangle([(40,40),(2440,3460)],(255,255,255,180))
fnt = ImageFont.truetype('Harabara.ttf',100)
fntmed = ImageFont.truetype('Harabara.ttf',60)
fntsmg = ImageFont.truetype('Harabara.ttf',40)
d.text((50,50),"Fitness",font=fntmed,fill=(0,0,0,255))
for month in range(0,12):
    dates = getdays(2021,month+1)
    d.text((month*195+100,140),months[month],font=fntmed,fill=(0,0,0,255))
    for y,day in enumerate(dates):
        fill = (0,0,0,255)
        if day['day'] == "Sa" or day['day'] == "Su":
            fill = (100,100,100,255)
        d.text((month*195+210,y*103+275),day['day'][0:1],font=fntsmg,fill=(150,150,150,255))
        d.text((month*195+80,y*103+250),str(day['number']),font=fnt,fill=fill)
        if month == 10:
            if y != 0:
                d.line((40,y*103+250,2440,y*103+250),fill=(0,0,0,100),width=5)

im.save('habit2.png', 'PNG')