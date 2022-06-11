import scripter
import pyautogui

i = 1
PAUSE_MS = 1
pyautogui.PAUSE = PAUSE_MS / 1000

fishingPool = [0,0]

def screencap():
    global i
    pyautogui.screenshot(f'test-{i}.png')
    pyautogui.sleep(.500)

    print(i)
    i= i + 1

def clickPool():
    pyautogui.moveTo(fishingPool.x, fishingPool.y)
    pyautogui.leftClick()

def foo():
    # if fish ready to be caught
    if pyautogui.locateOnScreen('fishing.png'): # TODO
        # click hook icon (reel-in)
        pyautogui.moveTo(0, 0) # TODO
        pyautogui.leftClick()

        # wait for caught animation
        pyautogui.sleep(6) # TODO

        # click confirmation dialogue
        pyautogui.moveTo(0, 0) # TODO
        pyautogui.leftClick()

        # wait for dialogue to leave
        pyautogui.sleep(1) # TODO

        # mark fish caught
        global i
        print(i)
        i = i + 1

        # click fishing pool
        clickPool()


def init():
    global fishingPool
    fishingPool = pyautogui.position()
    clickPool()

# scripter.run(screencap)
scripter.run(foo, init)