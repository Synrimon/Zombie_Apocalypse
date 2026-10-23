"""
Welcome to Zombie Apocaclips -- A text-based Python story game!
    A game by @Synrimon (github & hackclub)
YOU are a promosing photographer caught up in mankind's greatest
biological blunder: Zombies. Traverse a decaying world full of
stories. 

GUIDE:
------- Set Up -------
How can you play this? Here's how!
Should also work on mobile, it's just going to be really squished.
Some places might not support the color coding & cleared screen,
but this shouldn't detract from the main game.

    * Code HS:
        1. Go to https://codehs.com/sandbox/maroonarmadillo5402/zombie-apocaclips
        2. Hit the green "Run" button
    
    * Online Python Interpreter:
        BEWARE -- > ANSI Escape stuff might not work. (colored txt, cleared screen, etc.)
        1. Copy ALL of this code
        2. Search "Online Python Interpreter"
        3. Choose one of the first two (not sponsored) links
        4. Click the left side and paste the code
        5. Press the "run" (or play) button 
        
    * VS Code:
        1. Copy ALL of this code
        2. Go to https://vscode.dev/ (VS Code website)
        3. Create a file in .py
        4. Select Python as the language
        5. paste code in
            install the Python API in extensions if needed
------- Play -------
* Scrolling:
    Depending on where you're running this, you might have to
    constantly scroll down to view all the dialogue!

* Inputs:
    Answers you can type are encapsulated in parenthesis
    ex: Waffles or pancakes ( waffles/pancakes )
    Type exactly what u see bc it's case sensitive

* Saving:
    Currently, NOT a feature yet, but I'm planning on making it

    How it WOULD work v
    1. Type save in any input box
    2. String is produced with your progress and choices
    3. Copy, save it somewhere like a google doc or note
    4. Come back, enter load into the first input
    5. Paste string in 

* Dev Mischief:
    I may or may not have put small tidbits that are hidden:
    they're not hinted at in the game; they're in the code
    I usually make them for me bc :3 silly
    Feel free to find them if u wanna

------- Have fun -------
"""
# ------ Imports -------

import random
    # Usage: 
            # from 1 to 10 -- > (1, 10)
            # use random.randint(num,num) function
import time
    # Usage: 
            # defaults to seconds.
            # use time.sleep(seconds) function

# ------ Imports -------

# ------ Add-on ------

    # --- ANSI Colors ---
red = "ESC[38;5;31m"
orange = "ESC[38;5;208m"
yellow = "ESC[38;5;33m"
green = "ESC[38;5;32m"
blue = "ESC[38;5;34m"
purple = "ESC[38;5;93m"
    # --- ANSI Colors ---

def clear():
    print("clearing...")
    time.sleep(3)
    print("\033[H\033[2J")
    return "cleared"

def dialog_spacing(dialog_here):
    i = 0
    for i in range(len(dialog_here)):
        print(dialog_here[i])
        time.sleep(4)
        i += 1

# ------ Add-on ------

# ----- Save -----
def saving():
    #global (any & all inputs)
    #save_code = f"100.200.300.400.500"
    #save guide:
        # . are seperators
    pass

# ----- Start -----

print("""
Welcome to Zombie Apocaclips -- A text-based Python story game!
    A game by @Synrimon (github & hackclub)
YOU are a promosing photographer caught up in mankind's greatest
biological blunder: Zombies. Traverse a decaying world full of
stories. 

More parts of this game will be added on later C:

""")

for i in range(2):
    print(" ")
time.sleep(5)
# ----- Start -----

# ----- Story -----
    # --- The Day Everything went Wrong
clear()
print("""-------The Day Everything went Wrong-------""")
time.sleep(2)
dialog1 = ["""

It was late, the sun was setting. You were tinkering with your camera as
everything turned to a dark purple in your room an emergency broadcast 
drowned out all your passing thoughts. It lost you at 'diesease'.
Not soon after you could hear commotion down the street.""", 
""" 
You get an unsettling chill as you approach your bedroom window, camera
in hand. Peeking out through your closed blinds you see what everyone was
screaming about: zombies. Something you'd never believe unless you saw it
yourself.""",
"""
All you could think about was how crazy a photo of this would be. How you
felt the urge to remember this day forever.
""",
"""
So... you took a picture

"""]
dialog2 = ["Dialog here"]
dialog_spacing(dialog1)

print("      _______       _____      _____        _______        _____     ______ ")
print("    /         \\    |     |    |     |     /         \\     |     |   /     / ")
print("   |    ---    \\   |     |    |_____|    |    ---    \\    |     |  /     / ")
print("   |   |   \\ ___\\  |     |     _____     |   |   \\ ___\\   |      V      / ")
print("   |   |           |     |    |     |    |   |            |            / ")
print("   |   |     ____  |     |    |     |    |   |     ____   |      ^     \\ ")
print("   |    ____/   /  |     |    |     |    |    ____/   /   |     | \\     \\ ")
print("   \\           /   |     |    |     |    \\           /    |     |  \\     \\ ")
print("    -----------     -----     -------     -----------      -----    ------- ")