class AppletManager():
    def __init__(self):
        self.currentApplet = None

    def get(self, AppletName, Request):
        self.currentApplet = AppletName
        #if not self.currentApplet == AppletName:
        self.applet = getattr(__import__(AppletName), AppletName)
        
        if Request == 'Display':
            return self.applet.getAppletDisplay()