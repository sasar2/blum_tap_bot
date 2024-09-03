import pyautogui
import time
import keyboard
import win32api, win32con
import cv2
import numpy as np
import pygetwindow as gw

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

time.sleep(1)
while keyboard.is_pressed('q') == False:

    windows = gw.getAllTitles()
    # Find the Telegram window (you may need to adjust the window title)
    telegram_window = gw.getWindowsWithTitle('Telegram')[0]

    # Get window properties
    tg_x, tg_y = telegram_window.left +10, telegram_window.top +120
    tg_width, tg_height = telegram_window.width -20, telegram_window.height -200

    pic1 = pyautogui.screenshot(region=(tg_x, tg_y, tg_width , tg_height))
    
    hsvFrame = cv2.cvtColor(np.array(pic1), cv2.COLOR_BGR2HSV)
    
    # Create a mask for the green color
    lower_limit = np.array([75, 200, 220], dtype=np.uint8)
    upper_limit = np.array([88, 255, 255], dtype=np.uint8)
    green_mask = cv2.inRange(hsvFrame, lower_limit, upper_limit)

    green_contours, _ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in green_contours:
            area = cv2.contourArea(contour)
            if area > 30:
                x, y, w, h = cv2.boundingRect(contour)
                click(x +1 + tg_x, y+1 + tg_y)
                
