import scripter
import pyautogui

i = 1
PAUSE_MS = 1
pyautogui.PAUSE = PAUSE_MS / 1000

def foo():
    # buy pot
    # print(pyautogui.position())
    pyautogui.moveTo(330, 230)
    pyautogui.keyDown('shift')
    pyautogui.click()

    global i
    print(i)
    i= i + 1

scripter.run(foo)