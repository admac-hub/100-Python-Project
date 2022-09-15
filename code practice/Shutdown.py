import os
import platform

def shutdown():
    if platform.system() == "Windows":
        os.system('shutdown -s')
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("shutdown -h now")
    else:
        print("Os not supported!")

def restart():
    if platform.system() == "Windows":
        os.system("shutdown -t 0 -r -f")
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system('reboot now')
    else:
        print("Os not supported!")



shutdown = input("Do you wish to shutdown your computer ? (yes / no): ")
command = input("Use \'r\' for restart and \'s\' for shutdown: ").lower()
if shutdown == "yes":
    shutdown()
elif command == 'r':
    restart()
elif command == 's':
    shutdown()
else:
    print("Wronng letter")