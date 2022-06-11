import scripter
import pyautogui


i = 1
PAUSE_MS = 1
pyautogui.PAUSE = PAUSE_MS / 1000

def foo():
    # rez
    # print(pyautogui.position())
    pyautogui.moveTo(860, 460)
    pyautogui.leftClick()
    pyautogui.moveTo(2500, 1400)
    pyautogui.leftClick()
    pyautogui.leftClick()

    global i
    print(i)
    i= i + 1

    # pyautogui.sleep(3)
    pyautogui.sleep(.050) # just for ESC interrupt



scripter.run(foo)
