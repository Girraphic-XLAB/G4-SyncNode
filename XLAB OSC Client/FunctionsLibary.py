#Import subprocess for runing console comands
import subprocess
import shutil
import os
import datetime
import time

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
def RunConsoleCommand(int, str):
    if int:
        PrintLog(str)
        subprocess.run(str)

#Print String and log it into the log file
def PrintLog(str):
    print(str)

    #Is Logging enabled
    if ConfigLoader.EnableDebugging == 'True':

            #Get current date and time for the log file
            Now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            #Write to the log file
            with open(os.getcwd() + '\\Logs\\' + datetime.datetime.now().strftime('%Y-%m-%d') + '.log', "a+") as text_file:
                text_file.write(Now + ' > ' + str + '\n')


#Perforce Sync
def PerforceSync(address, int):
    RunConsoleCommand(int, ConfigLoader.PerforceSync)
    print('Sync Sucess.')
  
    
#Perforce force sync command.
def PerforceForceSync(address, int):
    RunConsoleCommand(int, ConfigLoader.PerforceForceSync)
    print('Force Sync Sucess.')


#Perforce revert command
def PerforceRevert(address, int):
    RunConsoleCommand(int, ConfigLoader.PerforceRevert)

#Delete Shader cache.
def DeleteShaderCache(address, int):
    if int:

        #Create a listof the folders to be deleted.
        FolderList = ['\\DerivedDataCache\\', '\\Intermediate\\', '\\Saved\\']

        #loop through each item in the list.
        for i in FolderList:

            #Check if the folder exists before deleting it.
            if os.path.isdir(ConfigLoader.ProjectDir + i):

                #Print to the user and if enabled also the log file.
                PrintLog('Deleting: ' + ConfigLoader.ProjectDir + i)
                shutil.rmtree(ConfigLoader.ProjectDir + i)

            #If the folder doesn't exist simply skip it.
            else:
                PrintLog(ConfigLoader.ProjectDir + i + ' Not Found, Skipping.')


#Launch Unreal
def LaunchUnreal(address, int):
    RunConsoleCommand(int, ConfigLoader.UELaunch)


#Sanatise Directory
def SanatiseDirectory(address, int):
    if int:
        if os.path.isdir(ConfigLoader.ProjectDir + '\\'):

            #Print to the user and if enabled also the log file.
            PrintLog('Deleting: ' + ConfigLoader.ProjectDir + '\\')
            shutil.rmtree(ConfigLoader.ProjectDir + '\\', ignore_errors=True)

        #If the folder doesn't exist simply skip it.
        else:
            PrintLog(ConfigLoader.ProjectDir + '\\' + ' Not Found, Skipping.')
        time.sleep(5)
        PerforceForceSync(address, int)