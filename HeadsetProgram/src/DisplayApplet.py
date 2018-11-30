#Now using the Luma.OLED Display Driver.

from NotificationManager import NotificationManager
from timeApplet import TimeApplet

class DisplayApplet():
    nManager = NotificationManager() # Setup access to a global notification manager.
    currentApplet = None
    # Notification + Time Center: 128x8
    # Applet Window: 128x24
    def appletLoad(self):
        self.running = True
        
    @classmethod
    def openApplet(cls, appletName):
        #if(cls.currentApplet)
        pass

    def appletMain(self):
        print("ToDo: DisplayApplet Main Method")
        print("Notifications: %s" % self.nManager.getNotificationList())
        print("\n Adding Test Notification \n")
        self.nManager.addNotification("fl")
        print("Notifications: %s \n \n" % self.nManager.getNotificationList())
        print("Notification Size: %s" % self.nManager.getNotificationSize())
        print("Time Size: %s" % self.nManager.getTimeSize())
    
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
        return TimeApplet.now