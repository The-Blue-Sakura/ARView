from multiprocessing import Process
import time
import datetime

class TimeApplet():
    amPM = "N/A"
    now = "%s:%s:%s %s" % (TimeApplet.formatHour(), datetime.datetime.now().minute, datetime.datetime.now().second, amPM)

    def appletLoad(self):
        self.running = True
        self.current_time = self.now
        self.lastTime = "NULL"

    def appletMain(self):
        updateTimeProcess = Process(target=self.updateTime, args=())
        updateTimeProcess.start()

    @classmethod
    def formatHour(cls):
        hour = datetime.datetime.now().hour
        newHour = 0
        if hour > 12:
            newHour = hour - 12
            cls.amPM = "PM"
        else:
            newHour = hour
            cls.amPM = "AM"
        return newHour
        
    def updateTime(self):
        while self.running:
            self.now = "%s:%s:%s %s" % (TimeApplet.formatHour(), datetime.datetime.now().minute, datetime.datetime.now().second, self.amPM)
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

    def __init__(self):
        self.appletLoad()