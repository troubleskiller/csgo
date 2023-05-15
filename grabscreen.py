# _*_ coding : utf-8 _*_
# @Time : 2022/6/29 18:53
# @Author : Lucid1ty
# @File : grabscreen
# @Project : Yolov5ForCSGO

import cv2
import numpy as np
from PIL import ImageGrab


def grab_screen(region=None):
    if region:
        left, top, x2, y2 = region
        width = x2 - left
        height = y2 - top
    # else:
    # width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    # height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    # left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    # top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    while True:
        rgb = ImageGrab.grab(bbox=(0, 0, width, height))
        rgb = np.array(rgb)

        return cv2.cvtColor(rgb, cv2.COLOR_BGRA2BGR)

