#Now using the Luma.OLED Display Driver.
from multiprocessing import Process
import time


from NotificationManager import NotificationManager
from Registry import AppletRegistry

class DisplayApplet():
    nManager = NotificationManager() # Setup access to a global notification manager.
    currentApplet = None
    displayableApplets = []
    importedApplets = []
    tempAppletEntries = []
    # Notification + Time Center: 128x8
    # Applet Window: 128x24
    def appletLoad(self):
        self.running = True
        DisplayApplet.displayableApplets = AppletRegistry.readDefaultRegistry()
        
        for entry in DisplayApplet.displayableApplets:
            DisplayApplet.importedApplets.append(__import__(entry))
            DisplayApplet.tempAppletEntries.append(entry)
            print(f"NEW APPLET ENTRY: {entry}")

        #module = __import__(displayableApplets[0], globals(), locals(), [displayableApplets[0]], 0)
        #module = __import__(displayableApplets[0])

    @classmethod
    def openApplet(cls, appletName):
        #if(cls.currentApplet)
        pass

    def appletMain(self):
        print("ToDo: DisplayApplet Main Method")
        #print("Notifications: %s" % self.nManager.getNotificationList())
        #print("\n Adding Test Notification \n")
        #self.nManager.addNotification("fl")
        #print("Notifications: %s \n \n" % self.nManager.getNotificationList())
        #print("Notification Size: %s" % self.nManager.getNotificationSize())
        #print("Time Size: %s" % self.nManager.getTimeSize())
        
        #Open the first applet
        DisplayApplet.currentApplet = "time"
        print(f"LIST OF CURRENTLY IMPORTED APPLETS: {DisplayApplet.importedApplets}")
        print(f"APPLETREGISTRY APPLET LIST: {AppletRegistry.AppletNames}")
        print(f"TEMPORARY APPLET ENTRIES: {DisplayApplet.tempAppletEntries}")
        print("\n\n SET CURRENT APPLET TO: %s" % DisplayApplet.currentApplet)


        # = Process(target=self.security.appletMain, args=())
        #securityProcess.start()
        DisplayWindow.displayLoop(1, 1)

    def appletUnload(self):
        print("ToDo: DisplayApplet Unload Method")

    def __init__(self):
        self.appletLoad()

class DisplayObject():
    def setDisplayObjectProperties(self, name, image):
        self.name = name
        self.image = image

class TimeObject():
    #Here is where we allocate space for the time in the notification area
    # Size: Wx8
    @classmethod
    def getTimeObject(cls):
        #return timeApplet.now
        pass

class DisplayWindow():
    loop_running = False

    @staticmethod
    def displayLoop(object, delaySeconds):
        DisplayWindow.loop_running = True
        while DisplayWindow.loop_running:
            print("GETTING IMPORTED APPLETS")
            print(f"{DisplayApplet.importedApplets}")
            #print(getattr(DisplayApplet.importedApplets[object], 'getAppletDisplay')())
            time.sleep(delaySeconds)

    @staticmethod
    def stopDisplayLoop():
        DisplayWindow.loop_running = False