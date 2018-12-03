from multiprocessing import Process
from SystemUtilities import Format
import time
import datetime

class TimeApplet():
    APPDISPLAYMODE = 0
    NOTIFICATIONDISPLAYMODE = 0

    amPM = "N/A"
    now = "%s:%s:%s %s" % (Format.timeTwelveHour()[0], datetime.datetime.now().minute, datetime.datetime.now().second, Format.timeTwelveHour()[1])

    def appletLoad(self):
        self.running = True
        self.current_time = TimeApplet.now
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
            time.sleep(0.1)

    def getTime(self):
        return self.current_time

    def appletUnload(self):
        self.running = False
    
    @classmethod
    def getAppletDisplay(cls):
        return cls.now
    @classmethod
    def getAppletNotification(cls):
        return cls.now

    def __init__(self):
        self.appletLoad()