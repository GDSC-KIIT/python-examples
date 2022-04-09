# https://pyautogui.readthedocs.io/en/latest/

import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

print(screenWidth, screenHeight)
print(currentMouseX, currentMouseY)
time.sleep(2)
pyautogui.write('Hello world!', interval=0)

# pyautogui.moveTo(250, 250)  # Move the mouse to XY coordinates.
# pyautogui.click()

# pyautogui.move(600, 400)
# pyautogui.doubleClick()

# pyautogui.press('esc')

# with pyautogui.hold('shift'): 
#     pyautogui.press(['left', 'left', 'left', 'left'])

# pyautogui.hotkey('ctrl', 'c')
