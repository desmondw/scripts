import scripter
import pyautogui

i = 1
PAUSE_MS = 1
pyautogui.PAUSE = PAUSE_MS / 1000

def foo():
    # use mana pot
    pyautogui.press('esc')

    global i
    print(i)
    i= i + 1

    # pyautogui.sleep(0.100)


scripter.run(foo)
