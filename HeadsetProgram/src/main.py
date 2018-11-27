from multiprocessing import Process

from DisplayApplet import DisplayApplet
from SecurityApplet import SecurityApplet
from InputApplet import InputApplet

class Main():
    version = 1

    def main(self):
        print("Version: %c" % str(self.version))
        self.display = DisplayApplet()
        self.security = SecurityApplet()
        self.input = InputApplet()
        #self.security.appletMain()
        securityProcess = Process(target=self.security.appletMain, args=())
        securityProcess.start()
        displayProcess = Process(target=self.display.appletMain, args=())
        displayProcess.start()
        inputProcess = Process(target=self.input.appletMain, args=())
        inputProcess.start()

if __name__ == '__main__':
    main = Main()
    main.main()