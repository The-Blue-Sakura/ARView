from multiprocessing import Process
from SystemUtilities import Format
import time
import datetime

class timeApplet():
    def __init__(self):
        self.now = "%s:%s:%s %s" % (Format.timeTwelveHour()[0], datetime.datetime.now().minute, datetime.datetime.now().second, Format.timeTwelveHour()[1])
        self.amPM = "N/A"

    def step(self, appInput):
        self.now = "%s:%s:%s %s" % (Format.timeTwelveHour()[0], datetime.datetime.now().minute, datetime.datetime.now().second, Format.timeTwelveHour()[1])
    
    def getDisplay(self):
        return (1, 2, self.now)