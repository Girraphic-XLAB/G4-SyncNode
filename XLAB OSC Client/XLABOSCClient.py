#Import OSC Server Components
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer

#Import custom functions python file
import XLABFunctions

#Import Config Reader
import configparser


#Access the config file to get data about OSC, projects and perforce. 
config = configparser.ConfigParser()
config.read('config.ini')


#Variables from the configuration file.
OSCIP = config['OSC']['IncomingIP']
OSCPORT = int(config['OSC']['IncomingPort'])
OSCPull = config['OSC']['PullCommand']



#Ascii art title
XLABFunctions.ASCIITitle()

#Default function for OSC if the value recived does not match any requierments.
def default_handler(address, *args):
    print(f"DEFAULT {address}: {args}")

#Test python event taking any input starting with /Python
def testevent(address, int):
    if int:
        print(int)

dispatcher = Dispatcher()
dispatcher.map("/Python" + OSCPull, testevent)
dispatcher.set_default_handler(default_handler)

ip = OSCIP
port = OSCPORT

server = BlockingOSCUDPServer((ip, port), dispatcher)
server.serve_forever()  # Blocks forever