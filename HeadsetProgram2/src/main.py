from multiprocessing import Process, Queue
import time

from DisplayApplet import DisplayTest
from SecurityApplet import FileScanner

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
        self.displayTest = DisplayTest() # Create an instance of the display test.
        self.fileScanner = FileScanner()

    def main(self):
        print(f"Version: {Main.version}")
        #Establish Multiprocess Communication
        queue = Queue()

        displayTestProcess = Process(target=self.displayTest.main, args=(queue, )) # Create a new process object to run the display test concurrently.
        displayTestProcess.start() # Start running the display test.

        self.fileScanner.verifySystemFiles() # Verify System Files
        
        print("EXITING DISPLAY TEST")
        queue.put(False)

if __name__ == '__main__':
    main = Main()
    main.main()