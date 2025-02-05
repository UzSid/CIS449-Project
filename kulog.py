import keyboard
import pyperclip as pc
import string
import random
import os

def on_key_press(event,):
    global word #this is where the actual word is stored

    #if the entered character is alphanumeric or punctuation, add extra random characters
    if (event.name.isalnum() or event.name in string.punctuation) and len(event.name) == 1:
        word += event.name
        keyboard.send(random.choice(string.ascii_letters+string.digits))
    
    #if the user presses backspace, delete the last letter of the actual string
    elif event.name == "backspace":
        word = word[:-1]

    #when the user presses space and the word is not empty:
    elif event.name == "space" and word != "":
        pc.copy(word) #copy the real word to the clipboard
        punctuation_count = 0 #reset punctuation count to 0
        keyboard.press('ctrl')
        #count punctuation except for apostrophes
        for x in word:
            if x in string.punctuation and x != '\'':
                punctuation_count += 1
        #extra backspaces are needed for punctuation marks
        for x in range(punctuation_count):
            keyboard.send('backspace')
        keyboard.send('backspace') #backspace the typed word
        keyboard.send('v') #paste the real word
        keyboard.release('ctrl')
        keyboard.send('space')
        word = "" #clear word

    #display the actual word being typed in the terminal
    os.system('cls')
    print(word)
    
word = ""
keyboard.on_press(on_key_press)

keyboard.wait()