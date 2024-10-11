import util_error as error_handler
import random

cameras = 6
camera_room = [
    'Living Room',
    'Bathroom',
    'Bedroom',
    'Office',
    'Kitchen',
    'Garage'
]
monster_camid = 6
monster_agressive = 2
monster_canmove = True

def monster_randomchance():
    chance = random.randint(1, 20)

    if chance == monster_agressive:
        monster_camCheck('Living Room', 0, monster_camid)
        monster_camCheck('Bathroom', 3, monster_camid)
        monster_camCheck('Bedroom', 2, monster_camid)
        monster_camCheck('Kitchen', 1, monster_camid)
        monster_camCheck('Garage', 5, monster_camid)
        monster_camCheck('Office', 6, monster_camid)
        monster_canmove = True

def returnCamRoom(camid):
    return camera_room[camid]

def checkCameraStuff():
    error = ''

    if len(camera_room) != cameras:
        error += f"There are not enough entries in the camera_room list (expected: {cameras}, got: {len(camera_room)})\n"

    if error != '':
        error_handler.throw(error, __name__)

def monster_camCheck(room, newid, monster_camid):
    try:
        if returnCamRoom(monster_camid) == room and monster_canmove:
            monster_camid = newid
            monster_canmove = False
            print('The monster has moved')
    except:
        error_handler.passE(f'Unknown Cam ID: {monster_camid}', __name__)

def monster_lure(roomid, monster_camid):
    if returnCamRoom(monster_camid) != 'Living Room' or random.randint(1, 2) == 1:
        monster_camid = roomid
        print('The Monster has been lured')
    else:
        print('The Monster has not been lured')