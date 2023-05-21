import keyboard
import pyautogui
import random
import time
import win32api
import win32con
from pyautogui import *

# Gets the color of the pixel at the mouse's current position
# pyautogui.displayMousePosition()

# Tile 1 Position: X:  1300 Y:  400 RGB: (  0,   0,   0)
# Tile 2 Position: X:  1415 Y:  400 RGB: (  0,   0,   0)
# Tile 3 Position: X:  1520 Y:  400 RGB: (  0,   0,   0)
# Tile 4 Position: X:  1615 Y:  400 RGB: (  0,   0,   0)
tiles = {
    "tile1": (1300, 400),
    "tile2": (1415, 400),
    "tile3": (1520, 400),
    "tile4": (1615, 400)
}


# Instead of using PyAutoGUI (too slow) to click the tiles, we can use the win32api to click the tiles.
def click(coords):
    win32api.SetCursorPos(coords)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)  # This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def main():
    while not keyboard.is_pressed("q"):
        # We get the color of the pixel for every tile
        for tile in tiles:
            # The star is here to destructure the tuple
            if pyautogui.pixel(*tiles[tile])[0] == 0:
                click(tiles[tile])
