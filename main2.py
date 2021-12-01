from PIL import Image, ImageDraw, ImageFont
from dates import getdays
im = Image.open("dec-back.jpg").convert("RGB")

im = im.resize((2480,3508))
d = ImageDraw.Draw(im,"RGBA")
dates = getdays(2021,12)
d.rectangle([(40,40),(1800,3460)],(255,255,255,140))
d.rectangle([(1800+25,40),(2450,3460)],(255,255,255,140))
fnt = ImageFont.truetype('Harabara.ttf',100)
for y,day in enumerate(dates):
    fill = (0,0,0,255)
    if day['day'] == "Sa" or day['day'] == "Su":
        fill = (100,100,100,255)
    d.text((770,y*103+250),day['day'],font=fnt,fill=fill)
    d.text((940,y*103+250),str(day['number']),font=fnt,fill=fill)
    if y != 0:
        d.line((40,y*103+250,1800,y*103+250),fill=(0,0,0,100),width=5)
        d.line((1800+25,y*103+250,2450,y*103+250),fill=(0,0,0,100),width=5)
fntbig = ImageFont.truetype('Harabara.ttf',160)
d.text((60,60),"December",font=fntbig,fill=(0,0,0,255))
# d.text((1850,60),"Tasks",font=fntbig,fill=(0,0,0,255))
im.save('dec.png', 'PNG')
