import keyboard
import sys
import os

def on_key_press(event):
    print(event.name, end=" ")
    sys.stdout.flush()

os.system('cls')

keyboard.on_press(on_key_press)

keyboard.wait()