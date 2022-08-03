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
        # pyautogui.click(button='left')
        x, y = pyautogui.position()
        pyautogui.click(x, y, button='left')
        # time.sleep(.200)
    # time.sleep(.1)
    # print('end')
