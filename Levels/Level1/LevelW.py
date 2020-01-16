import os
import sys
import time

from Levels.Level1.LevelWD import *
from functions.functions import *

"""
from Levels.Level1.LevelW import *
from Levels.Level1.LevelD import *
from Levels.Level1.Intro import *
"""

current_health = health
current_inventory = inventory

def LevelW():
       global current_health
       global time
       global health
       global current_inventory
       global enableLeft
       global enableRight
       global quitGame
       global called
       os.startfile(filename3)
       print("As you enter through the window you see the glowing moonlight\non the desk on your left...")
       print("There is a note on the shelf on your right that says something but needs a closer look...")
       print("In front of you is the door that leads to the main room of the hospital...")
       called = False
       def firstUp():
              global current_health
              global choice
              global health
              global current_inventory
              global called
              choice = input("What do you do? ")
              while choice != 'up':
                     if choice == 'punch':
                            print("You are punching the air... Why?")
                     if choice == 'inventory':
                            printInventory(current_inventory)
                     if choice == 'interact':
                            print("There is nothing to interact with...")
                     if choice == 'back':
                            print("You can't go back...")
                            print("The mission is not over yet.")
                            firstUp()
                            break
                     if choice == 'use':
                            use("Cannot use the car keys...", "- Yes? - the person asks...\n- I'm in some sort of a cabinet here...\n- Great... Move on...\n- Ok... - you hang up...")
                     if choice == 'discard':
                            current_inventory = discard()
                     if choice == 'left':
                            print("You go to the desk but there is nothing in your favour there... You get back to your entrance position...")
                            firstUp()
                            break
                     if choice == 'right':
                            print("You see the note on the shelf in front of you...")
                            while choice != 'back':
                                   if choice == 'up':
                                          print("You can't go further... There is a shelf in front of you...")
                                   if choice == 'left':
                                          print("You take another look at the door leading outside...")
                                   if choice == 'right':
                                          print("There is the window you just entered through...")
                                   if choice == 'punch':
                                          print("You punch the shelf... It's still there.")
                                   if choice == 'inventory':
                                          printInventory(current_inventory)
                                   if choice == "interact":
                                          print("You take the note. It says: 'The current state of the hospital is tragic...\nThe patients are more unstable than ever...\nWe need to shut it down now before it's too late\n   -Dr. Martin Penevski'\n- Ok... So the disappearances are not just lies? - you say to yourself...")
                                          print("You put the note back...")
                                   if choice == 'discard':
                                          current_inventory = discard()
                                   if choice == 'use':
                                          use("Cannot use the car keys...")
                                   choice = input("What do you do? ")
                            print("You get back to your entrance position...")
                            firstUp()
                            break
                     choice = input("What do you do? ")
              print("You sigh determined and go to the door...")
              print("As you open the door you feel the smell of rotten meat...")
              print("When you exit the cabinet you see corpses all over the place...")
              print("There is blood everywhere in the main hall and you cover your mouth...")
              print("In front of you there is the reception desk of the hospital...")
              print("On your left there is a corpse with a key in it's pocket...")
              print("And on your right there is a half broken steam pipe...(It may be useful in combat)")
              called = False
       def secondUp():
              global current_health
              global enableLeft
              global enableRight
              global health
              global current_inventory
              global hasPassedSecondUp
              global quitGame
              global called
              choice = input("What do you do? ")
              while choice != 'up' and choice != 'left' and choice != 'right':
                     if choice == 'interact':
                            print("There is nothing to interact with...")
                     if choice == 'back':
                            print("You can't go back...")
                            print("You have bussiness to attend to...")
                     if choice == 'punch':
                            print("You punch the air... Nothing changes...")
                     if choice == 'inventory':
                            printInventory(current_inventory)
                     if choice == 'use':
                            use("Can't use the keys now...", "-Ha ha, yes?\n- Umm... I've never seen anything like this... Hold on a sec...- you say and hang up...")
                     if choice == 'discard':
                            current_inventory = discard()
                     choice = input("What do you do? ")
              if choice == 'left':
                     if enableLeft == False:
                            print("You don't have anything to do there anymore...")
                            secondUp()
                     os.startfile(filename)
                     enableLeft = False
                     print("You go left and see the body of a dead policeman... You start digging into his pocket when he suddently jumps and grabs your foot")
                     if 'steam pipe' in current_inventory:
                            print("{Tip: You can use the pipe to kill the man...}")
                     choice = input("What do you do? ")
                     while True:
                            checkHealth()
                            if choice == 'inventory':
                                   print("You can't look at the inventory right now!!!")
                                   print("The man keeps scratching and biting you...")
                                   current_health = damage(current_health, 5)
                            if choice == 'up':
                                   print("Can't go up!!!")
                                   print("The man keeps scratching and biting you...")
                                   current_health = damage(current_health, 5)
                            if choice == 'back':
                                   print("Can't go back!!!")
                                   print("The man keeps scratching and biting you...")
                                   current_health = damage(current_health, 5)
                            if choice == 'left':
                                   print("Can't go left!!!")
                                   print("The man keeps scratching and biting you...")
                                   current_health = damage(current_health, 5)
                            if choice == 'right':
                                   print("Can't go right!!!")
                                   print("The man keeps scratching and biting you...")
                                   current_health = damage(current_health, 5)
                            if choice == 'interact':
                                   print("You try to push him off but he bites your hand...")
                                   current_health = damage(current_health, 10)
                            if choice == 'use':
                                   called = False
                                   choiceOfItem = use()
                                   if choiceOfItem == 'car keys':
                                          print("You try to stab the man with the keys but it does not work...")
                                          print("The man keeps scratching and biting you...")
                                          current_health = damage(current_health, 5)
                                   if choiceOfItem == 'phone':
                                          print("Cannot use that now!!!")
                                          print("The man keeps scratching and biting you...")
                                          current_health = damage(current_health, 5)
                                   if choiceOfItem == 'steam pipe':
                                          print("You strike him in the head with the pipe... He is dead...")
                                          break
                            if choice == 'discard':
                                   print("You cannot discard anything now!!!")
                                   print("The man keeps scratching and biting you...")
                                   current_health = damage(current_health, 5)
                            if choice == 'punch':
                                   checkHealth()
                                   print("You punch him a several times and he finally falls back...")
                                   print("He hits his head in the radiator behind him... He is dead...")
                                   print("However while you were striking him you were hit on the fingers a several times too...")
                                   current_health = damage(current_health, 5)
                                   break
                            choice = input("What do you do? ")
                     called = False
                     print("The man stands down with a fountain of blood pouring out of his head...")
                     print("You stand there horrified with your hands shaking")
                     print("Now that you calmed down and got rid of him you take the keys off of his pocket...")
                     current_inventory = appendToInventory('lunatic cells keys')
                     choice = input("What do you do now? ")
                     while choice != 'back':
                            if choice == 'up':
                                   print("You can't go up... There is a wall in front of you...")
                            if choice == 'inventory':
                                   printInventory(current_inventory)
                            if choice == 'interact':
                                   print("You check his body but there is nothing useful...")
                            if choice == 'left':
                                   print("You see a label on your right that says: 'Welcome to Furguson Hospital'")
                            if choice == 'right':
                                   print("You see the reception on your right...")
                            if choice == 'use':
                                   use("You can't use the keys now...", "- How can I assist?\n-This... It... We did not agree on this!!! Fuck! There are corpses everywhere... This shit is no joke!\n- Nick, we-\n- Okay, okay... Just call the police please.\n- Will do...\n- Thanks...- you sigh and hang up...")
                            if choice == 'discard':
                                   current_inventory = discard()
                            choice = input("What do you do? ")
                     if choice == 'back':
                            print("You get back to the entrance...")
                            secondUp()
              if choice == 'right':
                     if enableRight == False:
                            print("You have nothing to do there anymore...")
                            secondUp()
                     print("You go to the right and you are in front of the half broken pipe...")
                     choice = input("What do you do? ")
                     while choice != 'back':
                            if choice == 'up':
                                   print("You can't go up... There is a wall in front of you...")
                            if choice == 'left':
                                   print("You see the reception...")
                                   print("Corpses are lying everywhere...")
                            if choice == 'right':
                                   print("On your right there is a wall...")
                            if choice == 'punch':
                                   print("You punch the pipe but since it is rusty it hurts your hands...")
                                   current_health = damage(current_health, 2)
                            if choice == 'inventory':
                                   printInventory(current_inventory)
                            if choice == 'interact':
                                   print("You grab the pipe and start pulling with as much power as you've got...")
                                   print("Suddenly it breaks...")
                                   current_inventory = appendToInventory('steam pipe')
                                   enableRight = False
                            if choice == 'use':
                                   use("You can't use the keys now...", "- How can I assist?\n-This... It... We did not agree on this!!! Fuck! There are corpses everywhere... This shit is no joke!\n- Nick, we-\n- Okay, okay... Just call the police please.\n- Will do...\n- Thanks...- you sigh and hang up...")
                            if choice == 'discard':
                                   current_inventory = discard()
                            choice = input("What do you do? ")
                     if choice == 'back':
                            print("You get back to the entrance...")
                            secondUp()
              if choice == 'up':
                     if hasPassedSecondUp == False:
                            hasPassedSecondUp = True
                            print("With a hand on your mouth you walk up to the reception desk in horror...")
                            print("On your right there is a elevator leading to the upper floors...")
                            print("And on your left there is a cell door leading to the lunatic cells")
                            thirdUp()
                            return
                     if hasPassedSecondUp:
                            print("You go to the reception...")
                            thirdUp()
                            return
       def thirdUp():
              global current_health
              global current_inventory
              global called
              global health
              global inventory
              global hasPassedSecondUp
              global quitGame
              choice = input("What do you do? ")
              while choice != 'back' and choice != 'left':
                     if choice == 'up':
                            print("You go up and lean over the reception desk...\nThe receptionist is lying on the ground with his stomach torn...")
                            print("- Fucking disgusting - you whisper to yourself...")
                     if choice == 'use':
                            use("You can't use the car keys on this door", "- How can I assist?\n-This... It... We did not agree on this!!! Fuck! There are corpses everywhere... This shit is no joke!\n- Nick, we-\n- Okay, okay... Just call the police please.\n- Will do...\n- Thanks...- you sigh and hang up...", "You can't use the pipe at the moment...", "You can't use the key...")
                     if choice == 'inventory':
                            printInventory(current_inventory)
                     if choice == 'interact':
                            print("Nothing to interact with...")
                     if choice == 'right':
                            print("The elevator is not working... Needs a keycard...")
                     choice = input("What do you do? ")
              if choice == 'back':
                     print("You get back to the entrance...")
                     secondUp()
              if choice == 'left':
                     print("You get to the cell door...")
                     print("- Of course... It's locked...")
                     if 'lunatic cells keys' in current_inventory:
                            print("You have the key...")
                            choice = input("What do you do? ")
                            while choice != 'interact':
                                   if choice == 'up':
                                          print("You can't go up...")
                                          print("There is a cell door in front of you...")
                                   if choice == 'back':
                                          print("You get back at the reception...")
                                          thirdUp()
                                   if choice == 'punch':
                                          current_health = damage(current_health, 3)
                                          checkHealth()
                                   if choice == 'use':
                                          use("You can't use the car keys on this door", "- How can I assist?\n-This... It... We did not agree on this!!! Fuck! There are corpses everywhere... This shit is no joke!\n- Nick, we-\n- Okay, okay... Just call the police please.\n- Will do...\n- Thanks...- you sigh and hang up...", "You hit the door with the pipe... It does not break...", "You use the key to unlock the door...")
                                          #if choiceOfItem == 'lunatic cells key':
                                                 #print("You use the key to unlock the door...")
                                          break
                                   if choice == 'inventory':
                                          printInventory(current_inventory)
                                   if choice == 'left':
                                          if enableLeft == False:
                                                 print("You see the poor policeman that you killed lying...")
                                          if enableLeft == True:
                                                 print("Looks like that the only way to get through the door is the dead policeman...")
                                   if choice == 'right':
                                          print("There is a window... It reveals the waiting room")
                                   choice = input("What do you do? ")
                            print("You unlocked the door...")
                            print("You are now entering a dark area...")
                            os.startfile(filename1)
                            time.sleep(3)
                            LevelWD(current_health, current_inventory)
                                   
                     else:
                            while choice != 'back':
                                   if choice == 'up':
                                          print("You can't go up...")
                                          print("There is a cell door in front of you...")
                                   if choice == 'punch':
                                          current_health = damage(current_health, 3)
                                   if choice == 'inventory':
                                          printInventory(current_inventory)
                                   if choice == 'left':
                                          print("You see the poor policeman's body lying...")
                                   if choice == 'right':
                                          print("There is a window... It reveals the waiting room")
                                   if choice == 'interact':
                                          print("You have no keys...")
                                   if choice == 'discard':
                                          current_inventory = discard()
                                   choice = input("What do you do? ")
                            if choice == 'back':
                                   print("You get back at the reception...")
                                   thirdUp()
       firstUp()
       secondUp()
       thirdUp()
