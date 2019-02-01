from multiprocessing import Queue
import time

from PIL import Image, ImageDraw, ImageFont
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from luma.core.render import canvas

class DisplayTest():
    def __init__(self):
        self.running = True
    def startAnimation(self, queue):
        while self.running:
            print("HELLO")
            time.sleep(0.5)
            if(not queue.empty()):
                self.running = queue.get()
        while True:
            print("FINALIZING THE START ANIMATION BEFORE RUNNING MAIN LOOP")
            time.sleep(5)
            break

    def display(self, toDisplay):
        print(toDisplay)

class TestDisplay():
    def __init__(self):
        self.running = True
    def startAnimation(self, queue):
        while self.running:
            print("HELLO")
            time.sleep(0.5)
            if(not queue.empty()):
                self.running = queue.get()
        while True:
            print("FINALIZING THE START ANIMATION BEFORE RUNNING MAIN LOOP")
            time.sleep(5)
            break

    def display(self, toDisplay):
        #toDisplay Works, but it tries to open the image file in an external viewer, such as ms paint or similar.
        #So it works, but not in a self-contained way that was the goal.
        #toDisplay.show()
        pass

class DisplayHelpers():
    @classmethod
    def imgFromText(cls, text, xPos, yPos, font='fonts/Hanken-Book.ttf', fontSize=10):
        image = Image.new('1', (128,64))
        draw = ImageDraw.Draw(image)
        fnt = ImageFont.truetype(font, fontSize)
        draw.text((xPos,yPos), text, font=fnt, fill=(255))
        del draw
        return (image)

class DisplayAnimations():
    @staticmethod
    def bootAnimation(disp, queue):
        loopable = True
        while loopable:
            disp.display(DisplayHelpers.imgFromText("Welcome", 4, 4))
            time.sleep(0.05)
            if(not queue.empty()):
                loopable = queue.get()
        while True:
            disp.display(DisplayHelpers.imgFromText("Let's Do This!", 4, 4))
            break

class SystemDisplay():
    def __init__(self):
        self.serial = i2c(port=1, address=0x3c)
        self.device = ssd1306(self.serial, width=128, height=32)
        self.running = True

    def display(self, toDisplay):
        self.device.display(toDisplay) # This should take the 128x64 image and display it on the OLED.
        