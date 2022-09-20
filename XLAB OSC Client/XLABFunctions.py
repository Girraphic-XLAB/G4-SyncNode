#Import subprocess for runing console comands
import subprocess

#Ascii Title Art
def ASCIITitle():
    print("   _____ _____ _____  _____            _____  _    _ _____ _____           __   ___               ____  ")
    print("  / ____|_   _|  __ \|  __ \     /\   |  __ \| |  | |_   _/ ____|          \ \ / / |        /\   |  _ \ ")
    print(" | |  __  | | | |__) | |__) |   /  \  | |__) | |__| | | || |       ______   \ V /| |       /  \  | |_) |")
    print(" | | |_ | | | |  _  /|  _  /   / /\ \ |  ___/|  __  | | || |      |______|   > < | |      / /\ \ |  _ < ")
    print(" | |__| |_| |_| | \ \| | \ \  / ____ \| |    | |  | |_| || |____            / . \| |____ / ____ \| |_) |")
    print("  \_____|_____|_|  \_\_|  \_\/_/    \_\_|    |_|  |_|_____\_____|          /_/ \_\______/_/    \_\____/ ")



#Current test command
def PerforcePull(address, int):
    if int:
        print(int)
