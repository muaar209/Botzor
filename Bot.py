import time
import pyautogui
import time

pyautogui.click(950, 575)  # set focus to game

for t in range(0, 10):  # loop, need to change
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
