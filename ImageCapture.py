from djitellopy import tello
import cv2

me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamon()

while True:
    image = me.get_frame_read().frame
    #Resizes the frame to make it smaller which makes it faster
    image = cv2.resize(image,(360, 240))
    #Creats a window to display the resalt
    cv2.imshow("Image", image)
    cv2.waitKey(1)