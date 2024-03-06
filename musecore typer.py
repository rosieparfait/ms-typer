from pynput.keyboard import Controller
import keyboard
import time
import re

anyphrase = input("Custom phrase? ")

sequence = ""

if anyphrase:
    original_sequence = input("Please type your phrase: ")
    sequence = re.sub("[^cdefgab]", "", original_sequence)
else:
    print("Defaulting to Bee Movie Script.")
    sequence = "accdgaafaaeeaaabeedbeabefgaeagefaebdffegdebeefcefeaabecaebeedcaeaabeebacebacebacebacbacadeeaeaeaebabeafaeadcgagaecdbaadacabeeeaegcacgabaeeafaeadgdefeaecedabgdaeegadaeeeedfaefececadabedagagggeeegefcaeaeebeededadegeeadbadfgdeee"

keyboardController = Controller()

print(sequence)

stuck = True
heldctrl = False

def on_key_release(key):
    global stuck
    print('Released Key %s' % key)

print("Waiting on '*' key press for confirmation. Press q to quit.")

while stuck:
    if keyboard.read_key() == "q" and not heldctrl:
        break

    if keyboard.read_key() == "*":
        heldctrl = True
        print("Press any other key to begin.")
    elif heldctrl:
        stuck = False

if not heldctrl:
    print("Quitting.")
    quit()

print("Typing!")

for note in sequence:
    keyboardController.press(note)
    time.sleep(0.01)
    keyboardController.release(note)

print("Done! Quitting...")