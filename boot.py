import pyautogui, webbrowser 
from time import sleep

webbrowser.open("http://web.whatsapp.com/send?phone+447411308795")
sleep(10)

with open ('messaje_text.txt', 'r') as file:
    for line_messaje in file:
        pyautogui.typewrite(line_messaje)
        pyautogui.press('enter')
