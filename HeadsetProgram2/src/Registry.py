class RegistryReader():
    #There will be multiple registry files.
    #One will contain a list of installed applets
    #Another will contain a list of system settings
    def __init__(self):
        pass
    def readAppRegistry(self):
        pass
    def readSystemRegistry(self):
        pass
    def readCustomRegistry(self, file):
        pass


class RegistryWriter():
    def __init__(self):
        pass
    def writeAppRegistry(self):
        pass
    def writeSystemRegistry(self):
        pass
    def writeCustomRegistry(self, file):
        pass

class AppletRegistry():
    default_file = "appregistry.arreg"
    system_file = "secureapps.arreg"

    @staticmethod
    def readDefaultRegistry():
        appletNames = []
        regFile = open(AppletRegistry.default_file, "r")
        while True:
            tempName = regFile.readline().strip("\n")
            if(tempName == ""):
                break
            appletNames.append(tempName)
        regFile.close()
        # Applet Registry Debug Code
        # print(f"Applets: {appletNames}")
        return appletNames
    
    @staticmethod
    def readSecureRegistry():
        appletNames = []
        regFile = open(AppletRegistry.system_file, "r")
        while True:
            tempName = regFile.readline().strip("\n")
            if(tempName == ""):
                break
            appletNames.append(tempName)
        regFile.close()
        # Applet Registry Debug Code
        #print(f"Applets: {appletNames}")
        return appletNames

    @staticmethod
    def test():
        #module = __import__('Registry')
        func = getattr(AppletRegistry, 'readDefaultRegistry')
        func()