import pyautogui
import time
import keyboard
import webbrowser


webbrowser.open("https://youtube.com")

pozitie_initiala_x = 520
pozitie_initiala_y = 924

def cautare_yt():
    time.sleep(5)
    if pyautogui.locateOnScreen(r'D:\Bot Youtube\yt_search.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'D:\Bot Youtube\yt_search.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
        pyautogui.write('Valydex')
        pyautogui.press('enter')
    else:
        print("Imagine nu este pe ecran")

cautare_yt()

def cautare_canal():
    time.sleep(5)
    if pyautogui.locateOnScreen(r'D:\Bot Youtube\Valydex.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'D:\Bot Youtube\Valydex.png', confidence=0.7)
        pyautogui.click(camp_google)
    else:
        print("Imagine nu este pe ecran")

cautare_canal()

def subscribe():
    time.sleep(4)
    if pyautogui.locateOnScreen(r'D:\Bot Youtube\Subscribe.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'D:\Bot Youtube\Subscribe.png', confidence=0.7)
        pyautogui.click(camp_google)
    else:
        print("Esti abonat.")

subscribe()

def video():
    time.sleep(1)
    if pyautogui.locateOnScreen(r'D:\Bot Youtube\Video.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r'D:\Bot Youtube\Video.png', confidence=0.7)
        pyautogui.click(camp_google)
    else:
        print("Imagine nu este pe ecran")

video()

def coordonate():
    print(pyautogui.position()) #scrie pozitia cursorului pe ecran

i = 0
while ((i <= 3) and not keyboard.is_pressed('esc')):
    time.sleep(1)
    pyautogui.click(pozitie_initiala_x, pozitie_initiala_y)
    time.sleep(5)
    pyautogui.click(20,50)
    time.sleep(1)
    pozitie_initiala_x += 300
    i = i + 1

