#We are going to write code descriptions until we can get our libraries and other stuff open
''' TIME
We need to keep the time on the screen at almost all times.
It needs to be large when an 'applet' is not running
When an applet is running it needs to be small and in the corner.
We will use if statememts and multithreading to determine
if an applet is running.
'''

''' INTERNET APPLET
The internet applet is in charge of determining whether or not
the HMD is connected to the internet. If it is, then it will show
the user's IP address.
'''

''' WEATHER APPLET
The weather applet is in charge of getting the weather in the
user's area, based on the entered zip code. It will show the
current temperature and the current weather
(rain, snow, sunny, cloudy).
'''

''' HAND TRACKING APPLET DEBUG
The hand tracking applet is going to show where your hand is, 
relative to the edges of the camera's view. The debug version
of the hand tracking applet will stop the TIME applet and will
use the entire screen to show a single lit pixel for where the
detected hand is.
'''

''' HAND TRACKING APPLET USER
The hand tracking applet in user mode (instead of debug mode)
will show the appropriate section that the user's hand is in
by way of location code (think E2). Through the applet 
configuration, a more exact grid system can be used
(instead of dividing the camera into fourths, if could be
divided into eights or into every pixel, though
higher divisions are not advised.)
'''

'''Program Flow
BOOT-UP
    As soon as the RPI boots up, this program should be run, displaying an image on the screen
    for roughly 3 seconds. During these three seconds, the camera module should be warmed up and 
    all other required functions and data manipulation, including updates, should be completed.
    Self tests should also be run, with the output shown on the screen in some manner.
    The rest of the application should then run. For debugging, there should be some form of indicator
    on the display that will tell us how far along the start-up process is.

HOME
    Once the required actions are performed, the program should start hand tracking and run the TIME applet
    in the main view. There should be nothing else open in the notification area unless some system 
    notification framework is in place. From here, once the necessary gestures are performed, the time 
    and system notifications should be placed in the notification area while the appropriate applet is open
    in the main window.

HOW SWITCHING APPLETS IS HANDLED
    When the gesture to open a different applet is performed, the previous applet, if it provides
    notifications, should be put into the notification area and the main view should be filled with the new
    applet. If the previous applet is one without notification functionality, then it should be suspended
    with the appropriate data saved in a way that is handled by the applet itself. The main view should
    then be filled with the new applet.

A NOTE ON APPLETS
    Each applet should be constructed in a way that is controllable directly by the system. This would
    necessitate a requirement for a set of standard methods across all applets to help facilitate this.
    The standard is as follows:
        CLASS: 
            AppletName
        PUBLIC VARIABLES:
            Dependencies[]
                A variable used to ensure continued compatibility with other applets and modules
                currently installed on the system.
            Permissions[]
                A variable with a list of permissions needed for the applet, so that there may be some
                security within the software and so that any features required and allowed for the applet
                are exposed to the applet.
        METHOD:
            appletLoad
                Used to perform any setup required by the applet, such as checking for and retrieving
                saved data from a previous instance. This should also check for any required dependencies.
            appletMain
                This is where the applet itself is ran. In order to retrieve input from the user, it must
                ask for it from the VisionProcessing class, and in order to output anything to the display,
                it must put in a request with the DisplayManager class. Other hardware functionality that
                is provided by the headset and is required for the applet should be brokered with the 
                appropriate class.
            appletUnload
                Used to finalize any running aspect of the applet, as well as save data required for the
                next instance of the applet.
'''