#Now using the Luma.OLED Display Driver.

from NotificationManager import NotificationManager

class DisplayApplet():
    #Notification Center: 128x8
    #Applet Window: 128x24
    def appletLoad(self):
        print("ToDo: DisplayApplet")
        self.nManager = NotificationManager()

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