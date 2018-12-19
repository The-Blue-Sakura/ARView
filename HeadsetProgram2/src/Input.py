class InputManager():
    def __init__(self):
        print("Input Manager Init")
        self.stream = None # Camera Stream
        self.mg = MotionGesture()
    
    def getInput(self):
        print("Get Input")
        return self.mg.getGesture(self)

class MotionGesture():
    def __init__(self):
        print("Motion Gesture Init")

    def getGesture(self, inputManager):
        print(inputManager.stream)
        