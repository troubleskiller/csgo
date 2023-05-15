import time

import cv2
import pynput

import grabscreen

t0 = time.time()
mouse = pynput.mouse.Controller()
for i in range(10):
    mouse.move(50, 0)
print(time.time() - t0)

a = grabscreen.grab_screen(region=(0, 0, 3024, 1964))
cv2.imshow('1', a)
cv2.waitKey(0)
