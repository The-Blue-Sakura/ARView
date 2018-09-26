import requests

packInfo = 'https://raw.githubusercontent.com/The-Blue-Sakura/ARView/master/README.md'

r = requests.get(packInfo)
print r.text

f = open("readme.md", "w")
f.write(r.text)
f.close()
print 'File Written and Closed. New File:'

f = open("readme.md", "r")
print f.read()
f.close()