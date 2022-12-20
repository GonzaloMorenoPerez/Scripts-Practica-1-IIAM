from random import *
import win32api, win32con,time
import tkinter as tk
import pyautogui

def click(x,y):

    #click even call
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    
pyautogui.FAILSAFE = False

def move(x,y):
    # cursor move
    pyautogui.move(x,y)

while True:
    #get screen size
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    #pass random value to axis
    x = randint(0,50)
    y = randint(0,50)
    click(x,y)
    move(x,y)
    print('i am moving to x=',x,' and y=',y)
    time.sleep(0.5)#call each 5 seconds