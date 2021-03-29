from PIL import Image, ImageDraw, ImageFont
import waveshare_epd

font = ImageFont.truetype(font="times", size=14, index=0, encoding='')
font_bold = ImageFont.truetype(font="timesbd", size=14, index=0, encoding='')

birthday_cake = Image.open("birthday_cake.png").resize((14,14), Image.ANTIALIAS)

Himage = Image.new('1', (296, 128), 255)  # 255: clear the frame
draw = ImageDraw.Draw(Himage)
draw.text((20, 5), 'Events this week...', font=font_bold, fill = 0)
draw.text((20, 20), "Someone's birthday", font=font, fill = 0)
draw.line((20, 50, 70, 100), fill = 0)
draw.line((70, 50, 20, 100), fill = 0)
draw.rectangle((20, 50, 70, 100), outline = 0)
draw.line((165, 50, 165, 100), fill = 0)
draw.line((140, 75, 190, 75), fill = 0)
draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
draw.rectangle((80, 50, 130, 100), fill = 0)
draw.chord((200, 50, 250, 100), 0, 360, fill = 0)

Himage.paste(birthday_cake, (5,20))

Himage.save("image.bmp")