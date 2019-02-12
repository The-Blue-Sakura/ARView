from SystemUtilities import Format
from PIL import Image, ImageDraw, ImageFont
import datetime

class timeApplet():
    def __init__(self):
        self.appletName = "Time Applet"
        self.now = "%s:%s:%s %s" % (Format.timeTwelveHour()[0], datetime.datetime.now().minute, datetime.datetime.now().second, Format.timeTwelveHour()[1])
        self.amPM = "N/A"

    def step(self, appInput):
        self.now = "%s:%s:%s %s" % (Format.timeTwelveHour()[0], datetime.datetime.now().minute, datetime.datetime.now().second, Format.timeTwelveHour()[1])
    
    def getDisplay(self):
        return self.now

    def getDisplayV2(self):
        image = Image.new('1', (128,64))
        draw = ImageDraw.Draw(image)
        fnt = ImageFont.truetype('fonts/Hanken-Book.ttf', 10)
        draw.text((10,60), self.now, font=fnt, fill=(255))
        del draw
        return (image)