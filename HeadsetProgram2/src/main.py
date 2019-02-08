from multiprocessing import Process, Queue
import time

from DisplayApplet import SystemDisplay as Display
from DisplayApplet import DisplayAnimations, DisplayHelpers
from luma.core.render import canvas
import Input
import SecurityApplet

class Main():
    '''
        NEW PROGRAM FLOW:
        The program will now work similarly to some game engines, having initialization code and then a single run loop.
        It will start off by checking for updates (update.py)
        then it will move to running a display test (in this case an animated splash screen) while the security program checks all of the files.
        [display test and security programs run in separate threads. The security program remains in the main thread while the display test is external.]
        When the security program is finished checking all of the files, all of the external applets will be loaded and prepared for use.
        At this point, the time applet will be loaded and the main program loop will start.
    '''
    version = 3 # Current version of the project. Used for Debug Purposes

    def __init__(self):
        self.disp = Display() # Create an instance of the display test.
        self.security = SecurityApplet.SecurityApplet() # Create an instance of the security applet
        self.inputManager = Input.InputManager() # Create an instance of the Input Manager
        self.running = False
        self.applets = []
        self.appletObjects = []
        self.currentApplet = 0

    def main(self):
        print(f"Version: {Main.version}")
        #Establish Multiprocess Communication
        queue = Queue()

        displayTestProcess = Process(target=DisplayAnimations.bootAnimation, args=(self.disp, queue)) # Create a new process object to run the display test concurrently.
        displayTestProcess.start() # Start running the display test.

        self.security.verify() # Verify System Files

        self.applets = self.security.getVerifiedApplets() # Get a list of verified, installed applets

        for entry in self.applets:
            self.appletObjects.append(getattr(__import__(entry), entry)()) # Import all valid applets
            print(f"Imported: {entry}")

        self.currentApplet = self.applets.index("timeApplet") # Set the current applet to the time applet
        print(self.applets.index("timeApplet"))
        
        print("SENDING ANIMATION EXIT COMMAND")
        queue.put(False)
        displayTestProcess.join()

        print("MAIN LOOP")
        input("PAUSE - PreLoop")
        with canvas(self.disp.device) as draw:
            while self.running:
                appInput = self.inputManager.getInput()
                self.appletObjects[self.currentApplet].step(appInput)
                appDisplay = self.appletObjects[self.currentApplet].getDisplay()
                input("PREDISPLAY")
                self.disp.display(appDisplay, draw)
            

if __name__ == '__main__':
    main = Main()
    main.running = True
    main.main()