from PIL import Image, ImageDraw, ImageFont

import epd2in13d

epd = epd2in13d.EPD()
epd.init()
epd.Clear()
image = Image.open("dopet.png")
epd.display(epd.getbuffer(image))
