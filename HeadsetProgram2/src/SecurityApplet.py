#import importlib
import difflib
from Registry import AppletRegistry

class SecurityApplet():

    def __init__(self):
        self.scanner = FileScanner(self) # Create a new file scanner instance, passing the current instance of the Security Applet
        self.validApplets = []

        #Try to open an existing error log to append to it, otherwise create a new errorlog.
        try:
            self.errorlog = open("error.arlog", 'a')
        except Exception:
            self.errorlog = open("error.arlog", 'w')

    def appletMain(self):
        print("ToDo: Security Applet Main Method")
    
    def appletUnload(self):
        print("ToDo: SecurityApplet Unload Method")
    
    def writeError(self, error):
        self.errorlog.write(f"Exception: {error} \n")
    
    def verify(self):
        self.scanner.verifySystemFiles()
    
    def getVerifiedApplets(self):
        return self.validApplets

    

class FileScanner():
    def __init__(self, security):
        self.security = security # Gives the FileScanner class an instance of the security applet
    
    #A file verification class, simply checks if there are any differences between two files.
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
        
        try:
            if(self.fileVerifier("SecurityApplet.py", "saVerify")):
                print("Security Applet Modified!")
        except Exception as e:
            self.security.writeError(e)

        try:
            if(self.fileVerifier("main.py", "mVerify")):
                print("Main System Modified!")
        except Exception as e:
            self.security.writeError(e)

        try:
            if(self.fileVerifier("InputApplet.py", "iaVerify")):
                print("Input Applet Modified!")
        except Exception as e:
            self.security.writeError(e)

        try:
            if(self.fileVerifier("DisplayApplet.py", "daVerify")):
                print("Display Applet Modified!")
        except Exception as e:
            self.security.writeError(e)

        print("Verifying Installed Applets.")
        secureAppletRegistry = AppletRegistry.readSecureRegistry()
        defaultAppletRegistry = AppletRegistry.readDefaultRegistry()
        arregVerify = self.registryVerifier(secureAppletRegistry, defaultAppletRegistry)
        if(not arregVerify[0]):
            print("Applet Registry Modified!")
            print(f"Invalid applets: {arregVerify[1]}")
        
        self.security.validApplets = defaultAppletRegistry
        
        for applet in arregVerify[1]:
            self.security.validApplets.remove(applet)

        