import os
import time
import random
from PIL import Image

dir = '/home/pi/code/e-paper'

import sys
sys.path.append(dir)

from waveshare_epd import epd2in9

path = "/home/pi/code/e-paper/calendar"
epd = epd2in9.EPD()
epd.init(epd.lut_full_update)
epd.Clear(0xFF)

images = os.listdir(path)
img = "bmps/image.bmp"
img = Image.open(os.path.join(path, img))

epd.display(epd.getbuffer(img))
