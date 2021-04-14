from PIL import Image, ImageDraw, ImageFont
import os
import datetime
from dateutil.relativedelta import relativedelta
from math import ceil

path = '/home/pi/code/e-paper/calendar'

class Calendar:
    def __init__(self):
        self.font = ImageFont.truetype(font="/usr/share/fonts/truetype/msttcorefonts/Arial.ttf", size=15, index=0, encoding='')
        self.font_bold = ImageFont.truetype(font="/usr/share/fonts/truetype/msttcorefonts/Arial_Bold_Italic.ttf", size=15, index=0, encoding='')
        
        birthday_cake = Image.open(path + "/icons/birthday_cake.png").resize((14,14), Image.ANTIALIAS)
        
        events_per_page = 6
        
        with open(os.path.join(path, "data/eventsFull.txt"), "r") as file:
            upcoming_events = [line.rstrip("\n") for line in file.readlines() if self.strptime_wrapper(line) < (datetime.datetime.now() + relativedelta(months=12)).date()]
        
        pages = ceil(len(upcoming_events)/events_per_page)         
        
        for page in range(pages):
            self.image = Image.new('1', (296, 128), 255)
            self.draw = ImageDraw.Draw(self.image)
            self.draw_underlined_text((20, 5), "Upcoming Events...")
            self.draw.text((250, 5), f"{page+1}/{pages}", font=self.font)
            if (page+1) * events_per_page <= len(upcoming_events):
                number_lines = events_per_page
            else:
                number_lines = len(upcoming_events) % events_per_page
                
            for line in range(number_lines):
                event_number = page * events_per_page + line
                event_string = upcoming_events[event_number]
                
                position = (20, 25 + (15 * line))
                
                if "birthday" in event_string.lower():
                    self.image.paste(birthday_cake, (5,position[1]))
                
                self.draw.text(position, event_string, font=self.font, fill = 0)
                
            self.image.save(path + f"/bmps/calendar-{page}.bmp")
                
        
    def strptime_wrapper(self, string):
        return datetime.datetime.strptime(string[:6], "%d %b").date()

    def draw_underlined_text(self, pos, text, **options):    
        twidth, theight = self.draw.textsize(text, font=self.font_bold)
        lx, ly = pos[0], pos[1] + theight + 1
        self.draw.text(pos, text, font=self.font_bold, **options)
        self.draw.line((lx, ly, lx + twidth, ly), **options)
                
if __name__ == "__main__":
    calendar = Calendar()
    
    birthday_cake = Image.open(path + "/icons/birthday_cake.png").resize((14,14), Image.ANTIALIAS)
    

#birthday_cake = Image.open(path + "/icons/birthday_cake.png").resize((14,14), Image.ANTIALIAS)

#image = Image.new('1', (296, 128), 255)  # 255: clear the frame
#draw = ImageDraw.Draw(image)
#draw_underlined_text(draw, (20, 5), "Events this week...", font=font)
#draw.text((20, 5), 'Events this week...', font=font, fill = 0, )

#image.paste(birthday_cake, (5,20))
#draw.text((20, 20), "Someone's birthday", font=font, fill = 0)



#image.save(path + "/bmps/image.bmp")