import pyautogui
import time
import numpy as np
from PIL import ImageGrab
import cv2

last_time = time.time()

pyautogui.click(950, 575)  # set focus to game
pyautogui.keyDown('tab')  # find target
pyautogui.keyUp('tab')  # find target
time.sleep(1)
pyautogui.keyDown('1')  # auto attack
pyautogui.keyUp('1')
time.sleep(1)
pyautogui.keyDown('3')  # bow
pyautogui.keyUp('3')
time.sleep(1)
pyautogui.keyDown('1')  # auto attack
pyautogui.keyUp('1')
time.sleep(22)  # time it takes to kill a mob

pyautogui.keyDown('shift')  # auto loot
pyautogui.rightClick(950, 752)
time.sleep(1)
pyautogui.keyUp('shift')


# while(True):
#     screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
#     # printscreen_numpy = np.array(printscreen_pil.getdata(),dtype='uint8')
#
#     print('Loop took {} seconds' .format(time.time()-last_time))
#     last_time = time.time()
#     cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break
