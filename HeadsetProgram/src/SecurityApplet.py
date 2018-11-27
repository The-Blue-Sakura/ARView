#import importlib
import difflib

class SecurityApplet():

    def appletLoad(self):
        print("ToDo: SecurityApplet")
        print("Importing Difflib")
        #self.difflib = __import__("difflib")

    def appletMain(self):
        print("ToDo: Security Applet Main Method")
        self.verifySystemFiles()
    
    def appletUnload(self):
        print("ToDo: SecurityApplet Unload Method")

    def __init__(self):
        self.appletLoad()

    def verifier(self, file1, file2):
        text1 = open(file1).readlines()
        text2 = open(file2).readlines()

        diff = False
        for line in difflib.unified_diff(text1, text2):
            #print(line)
            if(line != ''):
                diff = True
        return diff

    def verifySystemFiles(self):
        print("Verifying System Files.")
        if(self.verifier("SecurityApplet.py", "saVerify")):
            print("Security Applet Modified!")
        if(self.verifier("main.py", "mVerify")):
            print("Main System Modified!")
        if(self.verifier("InputApplet.py", "iaVerify")):
            print("Input Applet Modified!")
        if(self.verifier("DisplayApplet.py", "daVerify")):
            print("Display Applet Modified!")
        