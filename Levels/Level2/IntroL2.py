import os
import sys
from functions.functions import *
from Levels.Level2.LevelN import *
from Levels.Level2.LevelW import *

current_health = health
current_inventory = inventory

got_friend = False

def IntroL2():
    global current_health
    global current_inventory
    global got_friend
    enable_back = True
    
    print("You find yourself on a chair... You feel like your head is going to explode.")
    print("The room around you is dark with only one light bulb at the center of it.")
    print("On your right there is a table with your backpack on it...")
    print("And on your left is darkness... In front of you is a big metal door.")
    print("Suddenly a sound comes from the left corner in front of you...")
    print("- Hello? - you say scared...\n- Hello, my little pig... - says a voice. - You do realize it was a trap, don't you?")
    print("You spot a slender and tall figure with an apron who has a very similar voice to the one that talked to you on the phone.")
    print("- Fuck you... - you answer...")
    print("He slaps you in the face...")
    current_health = damage(current_health, 2)
    print("- YOU ARE THE ONE WHO'S GONNA BE FUCKED, LITTLE PIG!!! - he says angrily...")
    print("- I have to throw out the trash... They start rotting, you know... - he says and then laughs histerically.")
    print("He opens the door behind him and leaves. You are on your own...")
    choices = choose(("left", "right"),
        inventory_enabled = False,
        Up = "You can't go up. You are restrained.",
        Back = "You can't move back. You are restrained...",
        Interact = "You try to loosen the ropes but it does not work...",
        Punch = "You can't punch. You are restrained...")
    for choice in choices:
        if choice == "left":
            print("You lean with the chair to the left...")
            choice = input("What do you do?: ")
            if choice == "right":
                print("You then lean to the right. The chair falls and the ropes are now loose...")
                break
            else:
                print("The chair gets back to it's previous position...")
        if choice == "right":
            print("You lean with the chair to the right...")
            choice = input("What do you do?: ")
            if choice == "left":
                print("You then lean to the left. The chair falls and the ropes are now loose...")
                break
            else:
                print("The chair gets back to it's previous position...")
    
    choices = choose("up",
                     inventory_enabled = False,
                     Left="You turn to the left... There is pure darkness...",
                     Right="On your right is your backpack...",
                     Back="You see the body of a woman on the ground... She wears a white shirt and a black skirt.",
                     Interact = "You can't interact with anything now..."
                     )
    for choice in choices:
        if choice == "back":
            if not enable_back:
                print("You turn around and see Sonia...")
            else:            
                choice = input("What do you do?: ")
                if choice == "interact":
                    print("You lean over the body and suddenly the woman wakes up...")
                    os.startfile(filename)
                    print("You get back ready for her attack...")
                    print("But she doesn't attack. She is in her 30s...")
                    print("She sees you and screams really loud.")
                    print("You calm her down.")
                    print("- Hey, hey... It's ok... - you say")
                    print("She throws her boots at you.")
                    print("- Easy! I'm here to help!")
                    print("She is now calm...")
                    print("- Who are you?!?! - she asks in horror...")
                    print("- Name's Lester.")
                    print("- Sonia. This twisted fuck got me here and locked me up...")
                    got_friend = True
                else:
                    print("You get back to your previous position...")
            enable_back = False
    print("You take your backpack from the table...")
    print("You get to the door and open it...")
    print("- Hmm... Why didn't he lock it? - you ask yourself")
    if got_friend:
        print("- Fuck... This is some kind of trap... - says Sonia.")
        print("You open the door and continue through...")
        LevelW(current_health, current_inventory, got_friend)
    else:
        print("You open the door and continue through...")
        LevelN(current_health, current_inventory)
