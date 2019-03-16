import webbrowser
import keyboard
import time

webbrowser.open('https://mail.google.com/mail/u/0/#inbox', new=2)
keyboard.press_and_release('tab')
keyboard.press_and_release('tab')
time.sleep(3)
keyboard.press_and_release('tab')
keyboard.write('harshavardhan.19.1@protosem.tech')
keyboard.press_and_release('enter')
time.sleep(3)
keyboard.write('Harsrosh@671')
keyboard.press_and_release('enter')