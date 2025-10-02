import epd2in13d
from PIL import Image, ImageDraw, ImageFont

epd = epd2in13d.EPD()
epd.init()
epd.Clear()
image = Image.open("dopet.bmp")
epd.display(epd.getbuffer(image))
