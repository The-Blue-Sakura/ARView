import RPi.GPIO as GPIO
import time

class InputManager():
    inputType = 1 # Input Types: 0/1 - Vision/Button
    
    def __init__(self):
        print("Input Manager Init")
        if(InputManager.inputType == 0):
            self.stream = None # Camera Stream
            self.mg = MotionGesture()
        else:
            self.bc = ButtonCommand()
    
    def getInput(self):
        print("Get Input")
        if(InputManager.inputType == 0):
            return self.mg.getGesture(self)
        else:
            return self.bc.getButton()

class MotionGesture():
    def __init__(self):
        print("Motion Gesture Init")

    def getGesture(self, inputManager):
        print(inputManager.stream)

class ButtonCommand():
    def __init__(self):
        self.CTRLS =	{
            "Next": 23,
            "Previous": 24,
            "Action": 25,
            "System": 26
        }
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.CTRLS["Next"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.CTRLS["Previous"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.CTRLS["Action"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.CTRLS["System"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    def getButton(self):
        buttons = {}
        inputs = {self.CTRLS["Next"],self.CTRLS["Previous"], self.CTRLS["Action"],self.CTRLS["System"]}
        try:
            for x in inputs:
                if(GPIO.input(x)):
                    buttons.append(GPIO.input(x))
        except:
            GPIO.cleanup()

        return buttons

    def getControl(self, button):
        return(list(self.CTRLS.keys())[list(self.CTRLS.values()).index(16)])

    def getNextButton(self):
        return GPIO.input(self.CTRLS["Next"])

    def getPreviousButton(self):
        return GPIO.input(self.CTRLS["Previous"])

    def getActionButton(self):
        return GPIO.input(self.CTRLS["Action"])

    def getSystemButton(self):
        return GPIO.input(self.CTRLS["System"])
        