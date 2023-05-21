import keyboard
import pyautogui
import random
import time
import win32api
import win32con
from pyautogui import *

while True:
    if pyautogui.locateOnScreen('stickman.png', grayscale=True, confidence=0.8) is not None:
        print("I can see it")
        time.sleep(0.5)
    else:
        print("I am unable to see it")
        time.sleep(0.5)

