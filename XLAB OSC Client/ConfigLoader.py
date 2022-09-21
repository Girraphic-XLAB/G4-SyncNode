#Import Config Reader
import configparser

#Access the config file to get data about OSC, projects and perforce. 
config = configparser.ConfigParser()
config.read('config.ini')


#Variables from the configuration file.
OSCIP = config['OSC']['IncomingIP']
OSCPORT = int(config['OSC']['IncomingPort'])
OSCSync = config['OSC']['SyncAddress']
OSCForceSync = config['OSC']['ForceSyncAddress']
ProjectDir = config['GENERAL']['ProjectRootDir']
P4Stream = config['GENERAL']['P4StreamDir']


PerforceSync = 'p4 sync -q ' + ProjectDir + '\...#head'
PerforceForceSync = 'p4 sync -f -q ' + ProjectDir + '\...#head'