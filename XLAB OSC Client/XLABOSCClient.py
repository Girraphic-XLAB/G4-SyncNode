#Import OSC Server Components
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer

#Import custom functions python file
import XLABFunctions

#Import Config Data
import ConfigLoader


#Ascii art title
XLABFunctions.ASCIITitle()

#Default function for OSC if the value recived does not match any dispatcher maps.
def default_handler(address, *args):
    print(f"DEFAULT {address}: {args}")

#Dispatcher in charge of mapping reciving OSC Commands to python functions.
dispatcher = Dispatcher()

#Dispatcher for pulling in Perforce, simply duplicate this for more OSC commands.
dispatcher.map("/Python" + OSCPull, XLABFunctions.PerforcePull)
dispatcher.set_default_handler(default_handler)


#Start server and wait for OSC comands
server = BlockingOSCUDPServer((ConfigLoader.OSCIP, ConfigLoader.OSCPORT), dispatcher)
server.serve_forever()  # Blocks forever