import os
import time
import random
from PIL import Image

dir = '/home/pi/code/e-paper'

import sys
sys.path.append(dir)


from waveshare_epd import epd2in9
path = '/home/pi/code/e-paper/calendar/bmps'

epd = epd2in9.EPD()

img = Image.open(os.path.join(path, "dalendar-0.bmp"))

while True:
    epd.init(lut = epd.lut_full_update)
    time.sleep(0.1)
    epd.reset()
    time.sleep(0.1)
    epd.display(epd.getbuffer(img))
    epd.sleep()
    time.sleep(10)
