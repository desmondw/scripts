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
    # if mouse.is_pressed('x') or mouse.is_pressed('x2'):
    if keyboard.is_pressed('e'):
        # x, y = pyautogui.position()
        # pyautogui.dragTo(x, y, button='left')
        # print('hitting right 1')
        # mouse.click('right')
        pyautogui.click(button='left')
        # print('hitting right 2')
        # time.sleep(.200)
        # print('hitting right 3')
    # time.sleep(.1)
    # print('end')
