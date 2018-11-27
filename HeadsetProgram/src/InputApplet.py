import time
#import picamera
import numpy as np

class InputApplet():
    #This applet is in charge of obtaining camera input, exposing it to a vision processing chain and then
    #returning the output of that chain to the rest of the system.
    running = False
    
    def appletLoad(self):
        self.running = True
        print("ToDo: Input Applet Load Method")
        #self.startCapture()
    
    def startCapture(self):
        print("ToDo: Input Applet StartCapture")
        #while self.running:
        #    with picamera.PiCamera() as camera:
        #        camera.resolution = (1024, 768)
        #        camera.framerate = 24
        #        time.sleep(2)
        #        self.output = np.empty((768, 1024, 3), dtype=np.uint8)
        #        camera.capture(output, 'rgb')
    
    def appletMain(self):
        print("ToDo: InputApplet Main Method")
        #processVision(self.output)

    def processVision(self, mat):
        print("Do Stuff")

    def appletUnload(self):
        print("ToDo: InputApplet Unload Method")
        self.running = False

    def __init__(self):
        self.appletLoad()
