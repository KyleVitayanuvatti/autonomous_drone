from djitellopy import tello 
import KeyPress as kp
from time import sleep

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

def getKeyboardInput():
    #left right, foward backward, up down, yard velocity
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getKey("a"):
        lr = -speed
    elif kp.getKey("d"):
        lr = speed

    if kp.getKey("UP"):
        ud = speed
    elif kp.getKey("DOWN"):
        ud = -speed

    if kp.getKey("w"):
        fb = speed
    elif kp.getKey("s"):
        fb = -speed

    if kp.getKey("LEFT"):
        yv = -speed
    elif kp.getKey("RIGHT"):
        yv = speed

    if kp.getKey("q"):
        me.land()
    if kp.getKey("e"):
        me.takeoff()

    return [lr, fb, ud, yv]


while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0],vals[1],vals[2],vals[3])
    sleep(0.05)

    