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
epd.init(lut = epd.lut_full_update)

images = os.listdir(path)
images_order = [int(os.path.splitext(img)[0].split("-")[1]) for img in images]
images_ordered = [images[index] for index in images_order]
images_ordered.append(images_ordered[0])
for img in images_ordered[1:]:
    print(img)
    epd.init(lut = epd.lut_full_update)
    time.sleep(1)
    epd.reset()
    time.sleep(1)
    img = Image.open(os.path.join(path, img))
    epd.display(epd.getbuffer(img))
    time.sleep(60)
    
epd.sleep()
    

