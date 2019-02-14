import requests

class Updater():
    @classmethod
    def update(cls):
        try:
            packInfo = 'https://raw.githubusercontent.com/The-Blue-Sakura/ARView/master/upd.8'

            r = requests.get(packInfo)
            print('Downloading file upd.8')
            f = open("upd.8", "w")
            f.write(r.text)
            f.close()
            print("File Saved: upd.8")

            f = open("upd.8", "r")
            cverfile = open("currentversion", "r")

            updateVersion = f.readline()
            currentVersion = cverfile.readline()
            cverfile.close()

            if(int(updateVersion) > int(currentVersion)):
                print (f"An update is required. Now updating to version {updateVersion}")
                filename = f.readline().strip("\n")
                while True:
                    print(filename)
                    fileurl = f.readline().strip("\n")
                    print (fileurl)
                    dlBuffer = requests.get(fileurl)
                    dlFile = open(filename, "w")
                    dlFile.write(dlBuffer.text)
                    dlFile.close()
                    filename = f.readline().strip("\n")
                    print (filename == 'EOF')
                    if(filename == 'EOF'):
                        break
                cverfile = open("currentversion", "w")
                cverfile.write(updateVersion)
                cverfile.close()
            else:
                print ("UP TO DATE")
        except:
            print("Error Updating!")
            pass