# ██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗
# ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║
# ██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║
# ██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║
# ██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║
# ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
#                                                      
# ██╗███╗   ██╗███████╗██╗██████╗ ███████╗██████╗      
# ██║████╗  ██║██╔════╝██║██╔══██╗██╔════╝██╔══██╗     
# ██║██╔██╗ ██║███████╗██║██║  ██║█████╗  ██████╔╝     
# ██║██║╚██╗██║╚════██║██║██║  ██║██╔══╝  ██╔══██╗     
# ██║██║ ╚████║███████║██║██████╔╝███████╗██║  ██║     
# ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

# module imports
import random
import time

# file imports
import util_constants as constant
import util_keywords as keywordfile
import util_asciiart as ascii
import util_camera as camera

# thinger for url
# ?vscode-coi=

# you have started the program

camera.checkCameraStuff()
print(ascii.logo)
print('Out of Development')

# game data
data = {
    "name":"",
    "hour": 0,
    "night": 1
}
minute = 0
mainmenu = True

# basic functions

def randomName():
    new_name = keywordfile.randomKeyword() or 'N/A'
    return new_name

def incorrectForm():
    data.__setitem__('hour', 0)
    data.__setitem__('night', 1)

    print('Incorrect Format')

# name input
data.__setitem__('name', input(constant.name_input) or randomName())
print(f"It's nice to meet you, {data.get('name')}.")

save_data = input(f'input any save data > ')
if len(save_data) == 2:
    # expected format example: 62
    try:
        data.__setitem__('hour', int(save_data[0]))
        data.__setitem__('night', int(save_data[1]))

        if data.get('hour') < 0:
            data.__setitem__('hour', 0)
        if data.get('hour') > 5:
            data.__setitem__('hour', 5)

        if data.get('night') < 1:
            data.__setitem__('night', 1)
        if data.get('night') > 6:
            data.__setitem__('night', 6)
    except:
        incorrectForm()
else:
    incorrectForm()
   
print('Running...')

# command stuff

commands = [
    'help',
    'save_data',
    'check_camera',
    'audio_lure',
    'check_time',
    'time'
]

commands_info = [
    'gives info on commands',
    'returns current save data',
    'check the cameras',
    'lure the monster to one of the other cameras',
    'tells you the time',
    'tells you the time'
]


def command(com):
    inpit = com
    cancheck = commands.__contains__(inpit)
    # print(com)

    if inpit.__contains__(' '):
        print(f'Commands cannot contain a Space character.')
        cancheck = False

    if cancheck:
        if com == 'help':
            print(f"Python Insider v{str(constant.version)}")
            i = 0
            for command in commands:
                command_info = commands_info[i]
                print(f"{command} - {command_info}")
                i = i + 1
        
        if com == 'check_camera':
            camcheck()

        if com == "check_time" or com == 'time':
            hour = data.get('hour')
            curmin = round(minute * (60/constant.time_change_int))

            extraChar = ''
            if len(str(round(curmin))) == 1:
                extraChar = '0'

            print(f"Night {data.get('night')}, {hour}:{extraChar}{curmin}am")
        
        if com == 'save_data':
            print(data)
        
        if com == 'audio_lure':
            camcheck()
            
            print(f'What camera (1 - {camera.cameras})')
            cam = input("\n> ")
            cams = camera.cameras + 1

            try:
                if int(cam) < cams:
                    curcam = int(cam) - 1
                    # print(f"{camera.returnCamRoom(curcam)}, the monster has heard something")
                    camera.monster_lure(curcam, camera.monster_camid)
            except:
                pass

    else:
        if inpit != "":
            print(f'Unknown Command: {inpit}')

def camcheck():
    index = 0
    msterI = 1
    for cam in camera.camera_room:
        msg = "Nothing"

        if camera.monster_camid == msterI:
            msg = "Monster"
                
        print(f"{camera.camera_room[index]} - {msg}")
        index = index + 1
        msterI = msterI + 1

# loop
user_input = 'help'
# print(time.time())

while True:
    print('')

    if mainmenu:
        print('Commands')
        print("start - starts a new game")
        print("continue - continues a game")
        print("challenge - plays a challenge match")
        # print("achievements - list of awards you've earned")
        # print("options - change any settings you might have")
        print('')

        user_input = input("> ")

        if user_input.lower() == "start" or user_input.lower() == "continue" or user_input.lower() == "challenge":
            constant.change_timeChangeInt(40)
            
            if user_input.lower() == "start":
                data.__setitem__('night', 1)
                data.__setitem__('hour', 0)

            if user_input.lower() == "challenge":
                constant.change_timeChangeInt(60)

            user_input = "help"
            mainmenu = False
            print('')
            command('time')
        else:
            print('unknown')
    else:
        command(user_input.lower())
        print('')

        lasttime = time.clock_gettime(0)
        user_input = input('> ')
        curtime = time.clock_gettime(0)
        dif = curtime - lasttime
        camera.monster_randomchance()

        if constant.devmode:
            print(f'minute: {round(minute)}\ntime since command was run: {round(dif)}')
        
        minute = minute + dif

        if constant.devmode:
            print(f"minute now: {round(minute)}")

        if minute > constant.time_change_int:
            hour_change = round(minute/constant.time_change_int)    
            minute = minute - constant.time_change_int * hour_change
            
            camera.monster_agressive = camera.monster_agressive + hour_change * 2
            
            if camera.monster_agressive > 20:
                camera.monster_agressive = 20
            
            if minute < 0:
                minute = 0

            data.__setitem__('hour', int(int(data.get('hour')) + int(hour_change)))
            if constant.devmode:
                print(f"minutes were over {constant.time_change_int}")
                print(f"New Hour: {data.get('hour')} New minute: {round(minute)}")

            if data.get('hour') > 5:
                if constant.devmode:
                    print('end of night!!!')
                
                print(ascii.night_end)
                data.__setitem__('night', data.get('night') + 1)
                data.__setitem__('hour', 0)
                
                if data.get('night') < 6 and constant.time_change_int == constant.time_change_int_DEFAULT:
                    print(f'Night: {data.get("night")}')
                else:
                    mainmenu = True