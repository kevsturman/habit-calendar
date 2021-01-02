from PIL import Image, ImageDraw, ImageFont
from dates import getdays
im = Image.open("febback.jpg").convert("RGB")

im = im.resize((2480,3508))
d = ImageDraw.Draw(im,"RGBA")
dates = getdays(2021,2)
d.rectangle([(40,40),(1800,3460)],(255,255,255,180))
fnt = ImageFont.truetype('Harabara.ttf',100)
for y,day in enumerate(dates):
    fill = (0,0,0,255)
    if day['day'] == "Sa" or day['day'] == "Su":
        fill = (100,100,100,255)
    d.text((770,y*103+250),day['day'],font=fnt,fill=fill)
    d.text((940,y*103+250),str(day['number']),font=fnt,fill=fill)
    if y != 0:
        d.line((40,y*103+250,1800,y*103+250),fill=(0,0,0,100),width=5)
fntbig = ImageFont.truetype('Harabara.ttf',160)
d.text((60,60),"Febuary",font=fntbig,fill=(0,0,0,255))
im.save('feb.png', 'PNG')
