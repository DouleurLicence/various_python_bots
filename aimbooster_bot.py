import keyboard
import screeninfo
import pyautogui
import random
import time
import win32api
import win32con
from pyautogui import *


# Get the primary screen information
screen = screeninfo.get_monitors()[0]


# Instead of using PyAutoGUI (too slow) to click the tiles, we can use the win32api to click the tiles.
def click(coords):
    win32api.SetCursorPos(coords)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)  # This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def take_screenshot_from_region(region):
    """
        Takes a screenshot of the screen and saves it in the images folder
    """
    return pyautogui.screenshot(region=region)
    # iml.save(r"C:\Users\maxna\Exos Codage\Python\piano_tiles_bot\images\stickman.png")


def main():
    print("Program starting...")
    # Takes 2 seconds to launch the AimBooster game
    time.sleep(2)

    print("Press q to quit")
    while not keyboard.is_pressed("q"):
        region = (screen.width//2 + 100, 430, 742, 524)
        image = take_screenshot_from_region(region)

        width, height = image.size

        target = (255, 219, 195)

        prev = (0, 0)
        # We check every pixel of the image
        for i in range(0, width, 5):
            for j in range(0, height, 5):
                # If the pixel is the same color as the target, we click it
                if image.getpixel((i, j)) == target:
                    # We add the padding to the coordinates to click in the correct region
                    click((region[0] + i, region[1] + j))
                    time.sleep(0.04)
                    break


if __name__ == "__main__":
    main()
