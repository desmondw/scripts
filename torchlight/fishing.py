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

def getPos():
    pos = pyautogui.position()
    print(pos)
    print(pyautogui.pixel(pos.x, pos.y))
    pyautogui.sleep(.500)

def clickPool():
    print(f'clicking fishing pool')
    pyautogui.moveTo(fishingPool.x, fishingPool.y)
    pyautogui.leftClick()

def foo():
    # check if fish ready to be caught
    # if pyautogui.locateOnScreen('fishing.png'):
    pixel = pyautogui.pixel(1204, 959)
    if pixel[2] >= 200:
        print(f'ready to catch identified')
        pyautogui.sleep(.150)

        # click hook icon (reel-in)
        print(f'reeling in')
        pyautogui.moveTo(1275, 930)
        pyautogui.leftClick()

        # wait for caught animation
        print(f'waiting for animation')
        pyautogui.sleep(3.0) # TODO

        # click confirmation dialogue
        print(f'clicking confirm dialogue')
        pyautogui.moveTo(1275, 875)
        pyautogui.leftClick()

        # wait for dialogue to leave
        print(f'waiting for confirm dialogue to leave')
        pyautogui.sleep(0.2) # TODO

        # mark fish caught
        global i
        print(i)
        i = i + 1

        # click fishing pool
        clickPool()


def init():
    global fishingPool
    fishingPool = pyautogui.position()
    print(f'fishingPool position; x:{fishingPool.x} y:{fishingPool.y}')
    clickPool()

def printPixelColor():
    pixel = pyautogui.pixel(1204, 959)
    print(pixel)

# scripter.run(screencap)
# scripter.run(getPos)
scripter.run(foo, init)
# scripter.run(printPixelColor)
# scripter.run(getPos, init)