#Import subprocess for runing console comands
import subprocess

#Import config loader to acess variables
import ConfigLoader


#Ascii Title Art
def ASCIITitle():
    print('   _____ _____ _____  _____            _____  _    _ _____ _____           __   ___               ____  ')
    print('  / ____|_   _|  __ \|  __ \     /\   |  __ \| |  | |_   _/ ____|          \ \ / / |        /\   |  _ \ ')
    print(' | |  __  | | | |__) | |__) |   /  \  | |__) | |__| | | || |       ______   \ V /| |       /  \  | |_) |')
    print(' | | |_ | | | |  _  /|  _  /   / /\ \ |  ___/|  __  | | || |      |______|   > < | |      / /\ \ |  _ < ')
    print(' | |__| |_| |_| | \ \| | \ \  / ____ \| |    | |  | |_| || |____            / . \| |____ / ____ \| |_) |')
    print('  \_____|_____|_|  \_\_|  \_\/_/    \_\_|    |_|  |_|_____\_____|          /_/ \_\______/_/    \_\____/ ')
    print(' ')


#Generic console command function
def RunConsoleCommand (int, str):
    if int:
        PrintLog(str)
        subprocess.run(str)

#PrintString and log it into the log file
def PrintLog(str):
    print(str)
    if ConfigLoader.EnableDebugging:
            print('Logged')


#Perforce Sync
def PerforceSync(address, int):
    RunConsoleCommand(int, ConfigLoader.PerforceSync)
    print('Sync Sucess.')
        
#Perforce force sync comand
def PerforceForceSync (address, int):
    RunConsoleCommand(int, ConfigLoader.PerforceForceSync)
    print('Force Sync Sucess.')

#Delete Shader cache
def DeleteShaderCache(address, int):
    if int:
        #FolderList = ['\DerivedDataCache\', '\Intermediate\', '\Saved\']
        #for i in FolderList:
               #Command = 'RMDIR ' + ConfigLoader.ProjectDir + i + ' /s /q'
               #RunConsoleCommand(int, Command)

