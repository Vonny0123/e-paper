import os
import time
import random
from PIL import Image
from waveshare_epd import epd2in9

epd = epd2in9.EPD()
epd.init(epd.lut_full_update)
epd.Clear(0xFF)
path = "/share/Ewan/ProcessedImages/"
images = os.listdir(path)
img = random.choice(images)
img = Image.open(os.path.join(path, img))

epd.display(epd.getbuffer(img))
