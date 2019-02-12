from PIL import Image, ImageDraw, ImageFont
from picamera import PiCamera

class CameraApplet():
    def __init__(self):
        self.mode = 0 #Camera Mode: 0 for Still Image, 1 for Video
        self.nextFile = int(open("nextfile", "r").readline())
        self.messageDefault = ("IMG - WAITING", "VID - WAITING", "VID - RECORDING")
        self.message = "IMG - WAITING"
        self.videoResolution = (1920, 1080, 30) # 1920x1080px 30fps
        self.experimentalVideoResolution = (3280, 2464) # 3280x2464px 30fps - EXPERIMENTAL, DATA FROM SONY WEBSITE
        self.cameraResolution = (1920, 1080) # 3280x2464px
        self.camera = PiCamera(resolution=self.cameraResolution)
        pass

    def fileName(self):
        x = f"img/AR_{self.nextFile}"
        self.nextFile += 1
        open("nextfile", "w").write(self.nextFile)
        return x

    def step(self, appInput):
        self.message = messageDefault[self.mode]

        if(appInput.getActionButton()):
            if(self.mode == 0):
                self.camera.capture(self.fileName, format="yuv")
                self.message = "Captured Image"
            if(self.mode == 1):
                self.camera.start_recording(self.fileName, format="yuv")
                self.mode = 2
            if(self.mode == 2):
                self.camera.stop_recording()
        
        if(appInput.getSystemButton()):
            try:
                self.camera.stop_recording()
                self.camera.close()
            except:
                pass
    
    def getDisplay(self):
        #Old V2 Code
        #image = Image.new('1', (128,64))
        #draw = ImageDraw.Draw(image)
        #fnt = ImageFont.truetype('fonts/Hanken-Book.ttf', 10)
        #draw.text((10,60), self.message, font=fnt, fill=(255))
        #del draw
        #return (image)

        #New V1 Code
        return (self.message)