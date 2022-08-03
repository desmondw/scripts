import keyboard
import mouse
import time
import pyautogui

# print(mouse.record(button='right', target_types=('down',)))

# closer side mouse = x
# further side mouse= x2

while True:
    if keyboard.is_pressed('`'):
        exit(0)
    if mouse.is_pressed('x'):
        x, y = pyautogui.position()
        pyautogui.dragTo(x, y - 200, .15, button='left')
        pyautogui.moveTo(x, y)
        # time.sleep(.200)
    elif mouse.is_pressed('x2'):
        x, y = pyautogui.position()
        pyautogui.dragTo(x, y - 20, .15, button='left')
        pyautogui.moveTo(x, y)
        # time.sleep(.200)

