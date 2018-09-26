import requests

packInfo = 'https://raw.githubusercontent.com/The-Blue-Sakura/ARView/master/upd.8'

r = requests.get(packInfo)
print 'Downloading file upd.8'

f = open("upd.8", "w")
f.write(r.text)
f.close()
print "File Saved: upd.8"

f = open("upd.8", "r")
cverfile = open("currentversion", "r")

updateVersion = f.readline()
currentVersion = cverfile.readline()
cverfile.close()
print "UPDATE VERSION: "
print updateVersion
print "CURRENT VERSION: "
print currentVersion

if(int(updateVersion) > int(currentVersion)):
    print "UPDATE REQUIRED. UPDATING!"
    while True:
        filename = f.readline()
        if(filename == 'EOF'):
            break
        fileurl = f.readline()
        dlBuffer = requests.get(fileurl)
        dlFile = open("filename", w)
        dlFile.write(dlBuffer.text)
        dlFile.close()
    cverfile = open("currentversion", "w")
    cverfile.write(updateVersion)
    cverfile.close()
else:
    print "UP TO DATE"