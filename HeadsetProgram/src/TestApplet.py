#Now using the Luma.OLED Display Driver.
from multiprocessing import Process
import time


from NotificationManager import NotificationManager
from Registry import AppletRegistry
from AppletManager import AppletManager

class DisplayApplet():
    nManager = NotificationManager() # Setup access to a global notification manager.
    currentApplet = None
    # Notification + Time Center: 128x8
    # Applet Window: 128x24
    def appletLoad(self):
        self.running = True

        self.AppletManager = AppletManager()

        self.applets = AppletRegistry.readDefaultRegistry()

        #module = __import__(displayableApplets[0], globals(), locals(), [displayableApplets[0]], 0)
        #module = __import__(displayableApplets[0])

    @classmethod
    def openApplet(cls, appletName):
        #if(cls.currentApplet)
        pass

    def appletMain(self):
        print("DIAGNOSTICS:")
        print(f"applets: {self.applets}")
        self.currentApplet = self.applets[0]
        print(f"Time Applet Test Method: {self.AppletManager.get(self.currentApplet, 'Display')}")
        pass

    def appletUnload(self):
        print("ToDo: DisplayApplet Unload Method")

    def __init__(self):
        self.appletLoad()

class DisplayObject():
    def setDisplayObjectProperties(self, name, image):
        self.name = name
        self.image = image

class DisplayWindow():
    loop_running = False

    @staticmethod
    def displayLoop(object, delaySeconds):
        DisplayWindow.loop_running = True
        while DisplayWindow.loop_running:
            #print(getattr(DisplayApplet.importedApplets[object], 'getAppletDisplay')())
            pass

    @staticmethod
    def stopDisplayLoop():
        DisplayWindow.loop_running = False