class NotificationManager():
    notifications = [0, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    notificationSize = [8,8]
    timeSize = [16,8]
    def printNotificationList(self):
        for object in self.notifications:
            print(object)

    def addNotification(self, filename):
        notif = Notification(filename, filename)
        
        for i in range(len(self.notifications)):
            if(self.notifications[i] == None):
                self.notifications[i] = notif
                break

    def getNotificationList(self):
        return self.notifications
    
    def getNotificationSize(self):
        return self.notificationSize

    def getTimeSize(self):
        return self.timeSize

class Notification():
    def getNotificationName(self):
        return self.name
    
    def __init__(self, name, image):
        self.name = name
        self.image = image
    
    def str(self):
        return self.name

    def __unicode__(self):
        return self.name