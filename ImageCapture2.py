from djitellopy import tello 
import KeyPress as kp
import time
import cv2

kp.init()
me = tello.Tello()
me.connect()
global image
me.streamon()

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

    if kp.getKey("z"):
        cv2.imwrite(f'Drone/Images/{time.time()}.jpg', image)
        time.sleep(0.05)

    return [lr, fb, ud, yv]


while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0],vals[1],vals[2],vals[3])
    image = me.get_frame_read().frame
    #Resizes the frame to make it smaller which makes it faster
    image = cv2.resize(image,(360, 240))
    #Creats a window to display the result
    cv2.imshow("Image", image)
    cv2.waitKey(1)
    



    