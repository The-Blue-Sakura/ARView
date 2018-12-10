from multiprocessing import Process

#from DisplayApplet import DisplayApplet
from TestApplet import DisplayApplet
from SecurityApplet import SecurityApplet
from InputApplet import InputApplet
from timeApplet import timeApplet

class Main():
    version = 2

    def main(self):
        print("Version: %c" % str(self.version))
        #self.display = DisplayApplet()
        self.display = DisplayApplet()
        self.security = SecurityApplet()
        self.input = InputApplet()

        self.time = timeApplet()

        #Create class and method to read a system registry file and load all registered applets

        #self.security.appletMain()
        securityProcess = Process(target=self.security.appletMain, args=())
        securityProcess.start()
        displayProcess = Process(target=self.display.appletMain, args=())
        displayProcess.start()
        inputProcess = Process(target=self.input.appletMain, args=())
        inputProcess.start()

        timeProcess = Process(target=self.time.appletMain, args=())
        timeProcess.start()

        print(self.time.getTime())

if __name__ == '__main__':
    main = Main()
    main.main()