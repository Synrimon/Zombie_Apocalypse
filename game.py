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
        3. Select Python as the language
        4. paste code in
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
    
# ------ Add-on ------

