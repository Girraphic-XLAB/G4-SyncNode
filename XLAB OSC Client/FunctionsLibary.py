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



#Perforce Sync
def PerforceSync(address, int):
    if int:
        print(ConfigLoader.PerforceSync)
        subprocess.run(ConfigLoader.PerforceSync)
        print('Sync Sucess.')
        
#Perforce force sync comand
def PerforceForceSync (address, int):
    if int:
        print(ConfigLoader.PerforceForceSync)
        subprocess.run(ConfigLoader.PerforceForceSync)
        print('Force Sync Sucess.')