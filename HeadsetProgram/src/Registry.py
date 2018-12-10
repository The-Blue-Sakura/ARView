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
    AppletNames = []
    default_file = "appregistry.arreg"

    @staticmethod
    def readDefaultRegistry():
        regFile = open(AppletRegistry.default_file, "r")
        while True:
            tempName = regFile.readline().strip("\n")
            if(tempName == ""):
                break
            AppletRegistry.AppletNames.append(tempName)
        regFile.close()
        print(f"Applets: {AppletRegistry.AppletNames}")
        return AppletRegistry.AppletNames

    @staticmethod
    def test():
        #module = __import__('Registry')
        func = getattr(AppletRegistry, 'readDefaultRegistry')
        func()