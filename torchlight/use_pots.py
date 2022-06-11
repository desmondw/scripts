import scripter
import pyautogui


i = 1
PAUSE_MS = 1
pyautogui.PAUSE = PAUSE_MS / 1000

def foo():
    # use spell
    pyautogui.rightClick()
    pyautogui.sleep(.250)

    # use mana pot
    pyautogui.press('9')

    global i
    print(i)
    i= i + 1

    # wait for pot use to come available
    pyautogui.sleep(3.700)


scripter.run(foo)
