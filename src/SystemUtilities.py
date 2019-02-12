#Import Statements
import time
import datetime

class Format():
    @staticmethod
    def timeTwelveHour():
        hour = datetime.datetime.now().hour
        ampm = "n/a"
        newHour = 0
        if hour > 12:
            newHour = hour - 12
            ampm = "PM"
        else:
            newHour = hour
            ampm = "AM"
        
        return (newHour, ampm)