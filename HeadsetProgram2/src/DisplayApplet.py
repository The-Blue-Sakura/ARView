from multiprocessing import Queue
import time

class DisplayTest():
    def __init__(self):
        self.running = True
    def startAnimation(self, queue):
        while self.running:
            print("HELLO")
            time.sleep(0.5)
            if(not queue.empty()):
                self.running = queue.get()

    def display(self, toDisplay):
        print(toDisplay)
