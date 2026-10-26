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
import re
    # Usage:
        # Meta Charas
            # [] character set (ex: [a-c])
            # * zero+ occurances
            # + one+ occurances
        # findall() ex: ("word", text)

# ------ Imports -------

# ------ Add-ons ------

    # --- ANSI Colors ---
red = "\033[31m"
orange = "208"
yellow = "33"
green = "32"
blue = "\033[34m"
purple = "93"
    # --- ANSI Colors ---

def clear():
    time.sleep(3)
    print("\033[H\033[2J")
    return "cleared"

def day_titling(title):
    print(f"-------{title}-------")

def dialogue_spacing(dialogue_here):
    # takes a list/tuple
    i = 0
    for i in range(len(dialogue_here)):
        print(dialogue_here[i])
        time.sleep(4)
        i += 1

# ------ Add-ons ------

# ----- Save -----
def saving(save_code):
    saved = list(save_code)
    #global (any & all inputs)
    #save_code = f"words:words, words:words"
    #save guide:
        # . are seperators
    # maybe be a keyboard interrupt
    pass
# ----- Save -----

# ----- Inventory -----

player_inv = {
    "Item Slot 1" : "Empty",
    "Item Slot 2" : "Empty",
    "Item Slot 3" : "Empty",
    "Item Slot 4" : "Empty",
    "Item Slot 5" : "Empty",
    "Item Slot 6" : "Empty",
    "Item Slot 7" : "Empty"}

# ----- Inventory -----

# ----- Start -----
try:
    print(f"""
    Welcome to Zombie Apocaclips -- A text-based Python story game!
        A game by @Synrimon (github & hackclub)
    YOU are a promosing photographer caught up in mankind's greatest
    biological blunder: Zombies. Traverse a decaying world full of
    stories. 

    More parts of this game will be added on later C:

    {blue}If you have a save code please interrupt this message.{blue}
    """)

    time.sleep(5)
except KeyboardInterrupt:
    pass
# ----- Start -----

# ----- Story Parts -----
    # --- The Day Everything went Wrong ---
def episode_1(skip_value):
    completion_values = ("Event", "Event", "Item") # < -- Pair with completion
    completion = ["Event 1", "Event 2", ] # < -- Use a match case to match the values. I'm TIRED of coding if-elses bro.
    global red
    clear()
    # ^--- Readying
    day_titling("The Day Everything went Wrong")
    time.sleep(2)
    dialogue1 = (f"""

    It was late, the sun was setting. You were tinkering with your camera as
    everything turned to a dark purple in your room an emergency broadcast 
    drowned out all your passing thoughts. It lost you at {red}'disease'{red}.
    Not soon after you could hear commotion down the street.""", 
    f""" 
    You get an unsettling chill as you approach your bedroom window, camera
    in hand. Peeking out through your closed blinds you see what everyone was
    screaming about: {red}zombies{red}. Something you'd never believe unless you saw it
    yourself.""",
    """
    All you could think about was how crazy a photo of this would be. How you
    felt the urge to remember this day forever.
    """,
    """

    So... you took a picture
    """,
    """
        _______       _____      _____        _______        _____     ______ 
        /         \\    |     |    |     |     /         \\     |     |   /     / 
    |    ---    \\   |     |    |_____|    |    ---    \\    |     |  /     / 
    |   |   \\ ___\\  |     |     _____     |   |   \\ ___\\   |      V      / 
    |   |           |     |    |     |    |   |            |            / 
    |   |     ____  |     |    |     |    |   |     ____   |      ^     \\ 
    |    ____/   /  |     |    |     |    |    ____/   /   |     | \\     \\ 
    \\           /   |     |    |     |    \\           /    |     |  \\     \\ 
        -----------     -----     -------     -----------      -----    ------- 
    """,
    """
    As you slide your camera down from your face you hear something from your front door.
    It was faint, but still audbile from where you were.
    """)
    dialogue_spacing(dialogue1)
    time.sleep(1.5)
    for i in range(4):
        print(f"{red} Thud.{red}")
        time.sleep(1)
    print(" ")

# ----- Gameplay Order -----
    # Episode list planner:
        # Episode 1 : Entry into the apocalypse
        # Episode 2 : Shutting in
        # Episode 3 : Venturing out
        # Episode 4 : Memories... maybe
        # Episode 5
        # Episode 6
        # Episode 7