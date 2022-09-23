# G4 Sync Node
## Introducing G4 Sync
Girraphics homebrewed answer to waiting for Erizos to cache, it's a Python application to receives commands from OSC and interacts with Perforce, This way we can automate perforce actions on many many machines at once without individual interactions. This way we get all the benefits of Perforce (Only downloading whats changed)

## What it can do:
- Pull a project from perforce at the latest revision (At thus only Pull the changed files)
- Force pull a project from Perforce (This will pull all files from the depo even if the already exist) (For Debugging)
- Perforce Revert (This will revert any changed files back to there state in the depo)
- Delete Shader Cache (Deletes the Intermediate, DerivedDataCahce and Saved folders and Content form the project causing the shaders to recompile) (For Debugging)
- Sanitise (This will delete everything and repull from the depo for a fresh start)
- Launch the uproject with command line arguments (These are not dynamic, yet.)

## What still needs to be done:
- Better ini file handling, hardcoded default values to fall back to and specific error message if there is a problem with the config
- 2 way communication, at the moment G4 doesn't send any information back to OSC, some useful information might be if an action was a sucsess
- use the -n mode on P4 sync to show mb/number of files to bring current up to date with master (Would be good for debugging)
- Because G4 launches Unreal it has ownership over it and should be able to also kill it, will be useful if Unreal stops responding

## Where can i get it?
The brand new Girraphic-Xlab Github: https://github.com/Girraphic-XLAB/G4-SyncNode


## How to configure?
To configure G4 use the included Configuration.ini file, the file is layed out as follows:
```
[OSC]
This is the local ip address of the network adapter you want to use for OSC (This will be your locl IP unless you have multiple nics)
IncomingIP = 127.0.0.1

#The port OSC should use for reciving
IncomingPort = 1337

#These are the button address for your OSC program
#All buttons need to start with /python/ so an example would be /python/Button1
SyncAddress = /Button1
ForceSyncAddress = /Button2
QueryDepo = /Button3
RevertDir = /Button4
DeleteShaders = /Button5
SanatiseDir = /Button6
LaunchUnreal = /Button7


[GENERAL]
#This is the path to your UE4 editor, change this if you are using a nonstandard install path or differnt version of the editor.
UnrealDirectory = C:\Program Files\Epic Games\UE_4.27\Engine\Binaries\Win64\UE4Editor.exe

#The directory of your project, this is used for perforce syncing as well as the delete and sanatise commands
ProjectRootDir = F:\P4V\AR_blueprint_dev

#the Uproject file name, this is used for launching the project
Uproject = BroadcastBlueprints.uproject

#Enable debugging, this will create log files in the Logs folder containing all the actions you have submitted and any errors.
DebugLogging = True
```
