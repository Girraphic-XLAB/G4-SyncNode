#Import Config Reader
import configparser

#Access the config file to get data about OSC, projects and perforce. 
config = configparser.ConfigParser()
config.read('config.ini')


#Variables from the configuration file.
#Osc server variables
OSCIP = config['OSC']['IncomingIP']
OSCPORT = int(config['OSC']['IncomingPort'])

#OSC button addresses.
OSCSync = config['OSC']['SyncAddress']
OSCForceSync = config['OSC']['ForceSyncAddress']
OSCQuery = config['OSC']['QueryDepo']
OSCRevert = config['OSC']['RevertDir']
OSCShaderDelete = config['OSC']['DeleteShaders']
OSCSanatise = config['OSC']['SanatiseDir']

#Enable debugging variable
EnableDebugging = config['GENERAL']['DebugLogging']

#Project directory for P4 Commands.
ProjectDir = config['GENERAL']['ProjectRootDir']

#Assembled P4 comands to run sync and others.
PerforceSync = 'p4 sync -q ' + ProjectDir + '\...#head'
PerforceForceSync = 'p4 sync -f -q ' + ProjectDir + '\...#head'
PerforceQuery = 'p4 sync -n -q ' + ProjectDir + '\...#head'
PerforceRevert = 'p4 revert ' + ProjectDir + '\...'
