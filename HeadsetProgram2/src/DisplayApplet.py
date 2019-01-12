from multiprocessing import Queue
import time

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

class SystemDisplay():
    def __init__(self):
        self.serial = i2c(port=1, address=0x3c)
        self.device = ssd1306(self.serial, width=128, height=32)
        self.running = True
    
    def startAnimation(self, queue):
        while self.running:
            self.display("HELLO")
            time.sleep(0.5)
            if(not queue.empty()):
                self.running = queue.get()
        while True:
            self.display("Ending Anim")
            time.sleep(5)
            break

    def display(self, toDisplay):
        with canvas(self.device) as draw:
            draw.rectangle(self.device.bounding_box, outline="white", fill="black")
            draw.text((30, 40), str(toDisplay), fill="white")
        
        print(toDisplay)
        
