# G4 Sync Node
## Introducing G4 Sync
Girraphics homebrewed answer to waiting for Erizos to cache, it's a Python application to receives commands from OSC and interacts with Perforce, This way we can automate perforce actions on many many machines at once without individual interactions. This way we get all the benefits of Perforce (Only downloading whats changed)

## What it can do:
Pull a project from perforce at the latest revision (At thus only Pull the changed files)
Force pull a project from Perforce (This will pull all files from the depo even if the already exist) (For Debugging)
Perforce Revert (This will revert any changed files back to there state in the depo)
Delete Shader Cache (Deletes the Intermediate, DerivedDataCahce and Saved folders and Content form the project causing the shaders to recompile) (For Debugging)
Sanatise (This will delete everything and repull from the depo for a fresh start)
Launch the uproject with command line arguments (These are not dynamic, yet.)

## What still needs to be done:
Better ini file handling, hardcoded default values to fall back to and specific error message if there is a problem with the config
2 way communication, at the moment G4 doesn't send any information back to OSC, some useful information might be if an action was a sucsess
use the -n mode on P4 sync to show mb/number of files to bring current up to date with master (Would be good for debugging)
Because G4 launches Unreal it has ownership over it and should be able to also kill it, will be useful if Unreal stops responding

## Where can i get it?
The brand new Girraphic-Xlab Github: https://github.com/Girraphic-XLAB/G4-SyncNode
