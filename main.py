# module imports
import random

# file imports
from constants import *
from namekeywords import *

# thinger for url
# ?vscode-coi=

# game data
data = {
    "fname":"N/A",
    "lname":"N/A"
}

# basic functions
def randomKeyword():
    return keywords[random.randint(0, len(keywords))]

def randomName():
    new_name = randomKeyword() or 'N/A'
    return new_name

# print game version

# name input
data.__setitem__('fname', input(fname_input) or randomName())
data.__setitem__('lname', input(lname_input) or randomName())
print(f"It's nice to meet you, {data.get('fname')} {data.get('lname')}.")

# command stuff

commands = [
    'help',
    'check_basement'
]

commands_info = [
    'gives info on commands',
    'check the basement camera'
]


def command(com):
    if com == 'help':
        print(f"Python Insider v{str(version)}")
        i = 0
        for command in commands:
            command_info = commands_info[i]
            print(f"{command} - {command_info}")
            i = i + 1
        print('')

    if com == 'check_basement':
        print(f"")

# camera stuff
def changeCamStat(cam):
    return

# loop
user_input = 'help'

while True:
    print('')
    if commands.__contains__(user_input):
        command(user_input)
    else:
        print(f'Unknown Command: {user_input}/n')

    user_input = input('> ')