import os
import time
import random
from PIL import Image

dir = '/home/pi/code/e-paper'

import sys
sys.path.append(dir)

from waveshare_epd import epd4in2

epd = epd4in2.EPD()
epd.init()
epd.Clear()
path = "/share/Ewan/ProcessedImages/"
images = os.listdir(path)
img = random.choice(images)
img = Image.open(os.path.join(path, img))

epd.display(epd.getbuffer(img))
