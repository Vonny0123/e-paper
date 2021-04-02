from PIL import Image, ImageDraw, ImageFont

dir = '/home/pi/code/e-paper/calendar'

font = ImageFont.truetype(font="/usr/share/fonts/truetype/freefont/FreeMono.ttf", size=14, index=0, encoding='')
font_bold = ImageFont.truetype(font="/usr/share/fonts/truetype/freefont/FreeMono.ttf", size=14, index=0, encoding='')

birthday_cake = Image.open(dir + "/icons/birthday_cake.png").resize((14,14), Image.ANTIALIAS)

image = Image.new('1', (296, 128), 255)  # 255: clear the frame
draw = ImageDraw.Draw(image)

draw.text((20, 5), 'Events this week...', font=font_bold, fill = 0)

image.paste(birthday_cake, (5,20))
draw.text((20, 20), "Someone's birthday", font=font, fill = 0)



image.save(dir + "/bmps/image.bmp")