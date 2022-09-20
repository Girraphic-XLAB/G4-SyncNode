#Import Config Reader
import configparser

#Access the config file to get data about OSC, projects and perforce. 
config = configparser.ConfigParser()
config.read('config.ini')


#Variables from the configuration file.
OSCIP = config['OSC']['IncomingIP']
OSCPORT = int(config['OSC']['IncomingPort'])
OSCPull = config['OSC']['PullCommand']

