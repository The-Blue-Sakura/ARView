from multiprocessing import Process
from SystemUtilities import Format
import time
import datetime

class timeApplet():
    APPDISPLAYMODE = 1
    NOTIFICATIONDISPLAYMODE = 1

    amPM = "N/A"
    now = "%s:%s:%s %s" % (Format.timeTwelveHour()[0], datetime.datetime.now().minute, datetime.datetime.now().second, Format.timeTwelveHour()[1])

    def appletLoad(self):
        self.running = True
        self.current_time = timeApplet.now
        self.lastTime = "NULL"

    def appletMain(self):
        updateTimeProcess = Process(target=self.updateTime, args=())
        updateTimeProcess.start()

    def updateTime(self):
        while self.running:
            self.now = "%s:%s:%s %s" % (Format.timeTwelveHour()[0], datetime.datetime.now().minute, datetime.datetime.now().second, Format.timeTwelveHour()[1])
            if self.current_time != self.lastTime:
                self.lastTime = self.current_time
            self.current_time = self.now
            self.QUEUE.put(self.current_time)
            time.sleep(0.1)

    def getTime(self):
        return self.current_time

    def appletUnload(self):
        self.running = False
    
    @classmethod
    def getAppletDisplay(cls):
        return (1, 2, cls.now)

    @classmethod
    def getAppletNotification(cls):
        return cls.now

    def __init__(self, queue, a):
        self.QUEUE = queue
        self.appletLoad()