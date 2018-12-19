#import importlib
import difflib
from Registry import AppletRegistry

class SecurityApplet():

    def appletLoad(self):
        print("ToDo: SecurityApplet")
        print("Importing Difflib")
        #self.difflib = __import__("difflib")

    def appletMain(self):
        print("ToDo: Security Applet Main Method")
    
    def appletUnload(self):
        print("ToDo: SecurityApplet Unload Method")

    def __init__(self):
        self.appletLoad()

    

class FileScanner():
    def __init__(self):
        self.verifySystemFiles()
    
    def fileVerifier(self, file1, file2):
        text1 = open(file1).readlines()
        text2 = open(file2).readlines()

        diff = False
        for line in difflib.unified_diff(text1, text2):
            #print(line)
            if(line != ''):
                diff = True
        return diff

    # Takes in the verified applet registry and the currently installed applet registry.
    def registryVerifier(self, secure, actual):
        different = []
        same = True
        for applet in actual:
            if(applet not in secure):
                different.append(applet)
                same = False
        return (same, different)

    def verifySystemFiles(self):
        print("Verifying System Files.")
        '''
        if(self.fileVerifier("SecurityApplet.py", "saVerify")):
            print("Security Applet Modified!")
        if(self.fileVerifier("main.py", "mVerify")):
            print("Main System Modified!")
        if(self.fileVerifier("InputApplet.py", "iaVerify")):
            print("Input Applet Modified!")
        if(self.fileVerifier("DisplayApplet.py", "daVerify")):
            print("Display Applet Modified!")
        '''
        print("ToDo: Exception Handling")
        print("Verifying Installed Applets.")
        arregVerify = self.registryVerifier(AppletRegistry.readSecureRegistry, AppletRegistry.readDefaultRegistry)
        if(not arregVerify[0]):
            print("Applet Registry Modified!")
            print(f"Invalid applets: {arregVerify[1]}")


        