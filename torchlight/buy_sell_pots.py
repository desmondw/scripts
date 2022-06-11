import scripter
import pyautogui

SLEEP_MS = 0
PAUSE_MS = 1

i = 1
sleep = SLEEP_MS / 1000
pyautogui.PAUSE = PAUSE_MS / 1000

def foo():
    # move to purchase pot
    pyautogui.moveTo(100, 225)
    pyautogui.sleep(sleep)

    # buy pot
    pyautogui.keyDown('shift')
    pyautogui.click()
    pyautogui.keyUp('shift')

    # move to sell pot
    pyautogui.moveTo(2020, 1000)
    pyautogui.sleep(sleep)

    # sell pot
    pyautogui.keyDown('shift')
    pyautogui.click()
    pyautogui.keyUp('shift')

    global i
    print(i)
    i= i + 1

scripter.run(foo)