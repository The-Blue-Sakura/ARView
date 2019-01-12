from pyowm import OWM

class weatherApplet():
    def __init__(self):
        self.API_key = "e94264bdd9b4d1453de166db0c3ded6d"
        self.owm = OWM(self.API_key)
        self.location = self.owm.weather_at_place('Aurora,CO')
        #self.location = self.weather.lookup_by_location('aurora')
        #self.location = self.weather.lookup(12792871)


    def step(self, appInput):
        weather = self.location.get_weather()
        self.condition = (weather.get_temperature('fahrenheit'), weather.get_status())
    
    def getDisplay(self):
        return (0, 0, self.condition)