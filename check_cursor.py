import pyautogui
import time
o = None
while 1:
    c = list(pyautogui.position())
    if c != o:
        print(c)
        o = c
    time.sleep(1)
