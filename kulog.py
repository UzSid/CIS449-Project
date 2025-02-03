import keyboard
import pyperclip as pc
import string
import os

def on_key_press(event,):
    global word
    if (event.name.isalnum() or event.name in string.punctuation) and len(event.name) == 1:
        word += event.name
        keyboard.send('b')
    
    elif event.name == "backspace":
        word = word[:-1]

    elif event.name == "space" and word != "":
        pc.copy(word)  
        keyboard.press('ctrl')
        keyboard.send('backspace')
        keyboard.send('v')
        keyboard.release('ctrl')
        keyboard.send('space')
        word = ""

    os.system('cls')
    print(word)
    
word = ""
keyboard.on_press(on_key_press)

keyboard.wait()