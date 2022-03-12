import pyfiglet
from simple_chalk import chalk

# * import makeBackup here , custom module
from makeBackup import *

# onStartUp
# custom clear component for win , mac and for linux for clearing the screen.
clear()

# vars
rawLogo = pyfiglet.figlet_format("Backup")
rawSideLogo = pyfiglet.figlet_format("Files")
colorLogo = chalk.blue.bold(rawLogo)
colorSideLogo = chalk.yellow.bold(rawSideLogo)
logo = colorLogo + colorSideLogo

# Display

# logo
print(logo)

# Checking for any errors in input.
try:
    path = input("Enter your folder path : ")
except KeyboardInterrupt:
    # custom error component and error code.
    error(1)
except:
    # If , any error occurs , it will say something went wrong.
    error(2)

# add backup component here.
backup(path)

# custom copyright component.
copyRight()
