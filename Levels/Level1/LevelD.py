import os
import sys
from functions.functions import *
from Levels.Level1.LevelWD import *

current_health = health
current_inventory = inventory

def LevelD():
       global current_health
       global current_inventory
       global time
       global health
       global inventory
       global enableLeft
       global enableRight
       global called
       os.startfile(filename3)
       enableRight = True
       enableLeft = True
       called = False
       print("You are now in the backdoor room...")
       print("- Shit...- you whisper to yourself while looking all around you...")
       print("There is blood everywhere. Walls, ceiling, floor...It's a mess...")
       print("On your left there is a desk with a dead nurse on the other side...")
       print("On your right there is a bloody note on a chair...")
       print("In front of you is the door which leads to the main room of the hospital...")
       def firstUp():
              global current_health
              global current_inventory
              global time
              global health
              global enableLeft
              global enableRight
              global called
              choice = input("What do you do? ")
              while choice != 'up':
                     if choice == 'back':
                            print("Can't go away now...")
                     if choice == 'use':
                            use("You can't use those keys now...", "- Yes?- says the unknown voice...\n- Hey... I never agreed on this!!! It's a fucking mess!\n- Calm down, Nick... We-\nOkay, okay... There has been some sort of massacre...")
                     if choice == 'left':
                            print("You go to the desk...")
                            choice = input("What do you do? ")
                            while True:
                                   if choice == 'up':
                                          print("You can't go up...")
                                   if choice == 'left':
                                          print("You take a look at the entrance... It's all bloody...")
                                   if choice == 'right':
                                          print("You see the door leading to the main room...")
                                   if choice == 'interact':
                                          print("You check if the nurse is really dead...")
                                          print("She is... No pulse, no heartbeat...")
                                   if choice == 'inventory':
                                          printInventory(current_inventory)
                                   if choice == 'punch':
                                          print("You punch the desk...")
                                   if choice == 'use':
                                          use("You can't use those keys now...")
                                   if choice == 'back':
                                          firstUp()
                                          break
                                   if choice == 'discard':
                                          discard()
                                   choice = input("What do you do? ")
                     if choice == 'right':
                            print("You go to the chair with the bloody note on it...")
                            choice = input("What do you do? ")
                            while True:
                                   if choice == 'up':
                                          print("You can't go up...")
                                   if choice == 'left':
                                          print("You see the door leading to the main room...")
                                   if choice == 'right':
                                          print("You look at the entrance... It's bloody...")
                                   if choice == 'interact':
                                          print("You take a look at the note... There is nothing but blood..")
                                   if choice == 'inventory':
                                          printInventory(current_inventory)
                                   if choice == 'punch':
                                          print("You punch the desk...")
                                   if choice == 'use':
                                          use("You can't use those keys now...")
                                   if choice == 'back':
                                          firstUp()
                                          break
                                   if choice == 'discard':
                                          current_inventory = discard()
                                   choice = input("What do you do? ")
                     choice = input("What do you do? ")
              if choice == 'up':
                     print("You try to open the door leading to the main room... It's locked")
                     choice = input("What do you do? ")
                     while choice != 'right':
                            if choice == 'up':
                                   print("You can't go up... There is a door in front of you...")
                            if choice == 'left':
                                   print("You see the bloody wall on your left. There is soething ")
                            if choice == 'interact':
                                   print("You try to open the door again but it's locked and won't open...")
                            if choice == 'inventory':
                                   printInventory(current_inventory)
                            if choice == 'punch':
                                   print("You punch the door...")
                            if choice == 'use':
                                   use("You can't use those keys now...")
                            if choice == 'back':
                                   firstUp()
                                   break
                            if choice == 'discard':
                                   current_inventory = discard()
                            choice = input("What do you do? ")
              print("In front of you is a corridor which leads to some kind of a lab...")
       def secondUp():
              global current_health
              global current_inventory
              global time
              global health
              global inventory
              global enableLeft
              global enableRight
              global called
              choice = input("What do you do? ")
              while choice != 'up':
                     if choice == 'right':
                            print("You look at the entrance...")
                     if choice == 'left':
                            print("You see the door...")
                     if choice == 'back':
                            firstUp()
                            break
                     if choice == 'use':
                            use("Can't use those keys now...")
                     if choice == 'interact':
                            print("There is noting to interact with")
                     if choice == 'discard':
                            current_inventory = discard()
                     if choice == 'punch':
                            print("You punch the air...")
                     if choice == 'inventory':
                            printInventory()
                     choice = input("What do you do? ")
              if choice == 'up':
                     print("You continue through the hallway...")
                     print("As you enter the laboratory you see two beds with two patients lying on them...")
                     print("Both of the people's stomaches are torn...")
                     print("The one on the right has a scalpel in his guts...")
                     print("The other one has a key inside of him...")
                     print("In front of you is a cell door leading to a big hall with loads of cells in it...")
       def thirdUp():
              global current_health
              global current_inventory
              global time
              global health
              global enableLeft
              global enableRight
              global called
              choice = input("What do you do? ")
              while choice != 'up' and choice != 'right' and choice != 'left':
                     if choice == 'inventory':
                            printInventory(current_inventory)
                     if choice == 'discard':
                            current_inventory = discard()
                     if choice == 'use':
                            use("Can't use those keys...", "- Yes?\n- There is some sort of a laboratory here...\n- Good, continue your research...")
                     if choice == 'back':
                            print("You can't go back now... You've got bussiness to attend to...")
                     if choice == 'punch':
                            print("You punch the air...")
                     choice = input("What do you do? ")
              if choice == 'left':
                     enableLeft = False
                     print("You go to the left body...")
                     choice = input("What do you do? ")
                     while True:
                            if choice == 'up':
                                   print("You can't go up...")
                            if choice == 'right':
                                   print("You see a big lamp on your right...")
                                   print("Maybe it was for the surgeon to see better...")
                            if choice == 'left':
                                   print("You see the other corpse...")
                            if choice == 'back':
                                   print("You go back at the entrance...")
                                   thirdUp()
                                   break
                            if choice == 'use':
                                   use("Can't use those keys now...", "", "", "", "You can't use the scalpel here...")
                            if choice == 'interact':
                                   print("You take the scalpel out of the dead person's insides...")
                                   current_inventory = appendToInventory('scalpel')
                                   enableLeft = False
                                   break
                            if choice == 'discard':
                                   current_inventory = discard()
                            if choice == 'punch':
                                   print("You punch the corpse... It's still there...")
                            if choice == 'inventory':
                                   printInventory(current_inventory)
                            choice = input("What do you do? ")
              if choice == 'right':
                     if not enableRight:
                            print("You have nothing to do there anymore...")
                            thirdUp()
                     enableRight = False
                     print("You move slowly to the left corpse and try to get the key off of his gut...")
                     os.startfile(filename)
                     print("Suddenly he dives into you...")
                     print("He starts strangling you...")
                     if 'scalpel' in current_inventory:
                            print("{Tip: You can use the scalpel to defend yourself}")
                     choice = input("What do you do? ")
                     while True:
                            if choice == 'up':
                                   print("You can't go up!!!")
                                   print("The man keeps strangling you...")
                                   current_health = damage(current_health, 10)
                            if choice == 'right':
                                   print("You can't Go right!!!")
                                   print("The man keeps strangling you...")
                                   current_health = damage(current_health, 10)
                            if choice == 'left':
                                   print("Can't go left!!!")
                                   print("The man keeps strangling you...")
                                   current_health = damage(current_health, 10)
                            if choice == 'back':
                                   print("Can't go back!!!")
                                   print("The man keeps strangling you...")
                                   current_health = damage(current_health, 10)
                            if choice == 'use':
                                   choiceOfItem = use()
                                   if choiceOfItem == 'scalpel':
                                          print("You turn on the scalpel and go trough the man's skull...")
                                          break
                                   else:
                                          print("You can't use that now! The man keeps strangling you...")
                                          current_health = damage(current_health, 10)
                            if choice == 'interact':
                                   print("You try to get him off but he keeps strangling...")
                                   current_health = damage(current_health, 10)
                            if choice == 'discard':
                                   print("You can't discard items now!!!")
                                   print("The man keeps strangling you...")
                                   current_health = damage(current_health, 10)
                            if choice == 'punch':
                                   print("You punch the man multiple times... He falls back and hits his head in a radiator behind him...")
                                   print("You are hurt too...")
                                   current_health = damage(current_health, 5)
                                   break
                            if choice == 'inventory':
                                   print("You can't see your inventory now!!!")
                                   print("The man keeps strangling you...")
                                   current_health = damage(current_health, 10)
                            choice = input("What do you do? ")
                     print("The person is now dead...")
                     print("The key has fallen out of his stomach...")
                     current_inventory = appendToInventory('lunatic cells keys')
                     print("Covered in blood you go back at the entrance...")
                     thirdUp()
              if choice == 'up':
                     print("You go to the cell door...")
                     choice = input("What do you do? ")
                     while choice != 'interact' and choice != 'use':
                            if choice == 'up':
                                   print("You can't go up...")
                            if choice == 'back':
                                   thirdUp()
                            if choice == 'use':
                                   use("Can't use those keys now...", "", "", "", "You can't use that now...")
                            if choice == 'interact':
                                   print("You are now entering a dark area...")
                                   LevelWD(current_health, current_inventory)
                            if choice == 'discard':
                                   current_inventory = discard()
                            if choice == 'punch':
                                   print("You punch the cell door...")
                                   print("The rust hurts your hand...")
                                   current_health = damage(current_health, 3)
                            if choice == 'inventory':
                                   printInventory(current_inventory)
                            choice = input("What do you do? ")
                     if choice == 'interact':
                            if 'lunatic cells keys' in current_inventory:
                                   print("You are now entering a dark area...")
                                   LevelWD(current_health, current_inventory)
                            else:
                                   print("You've got to take the key for the door...")
                                   print("You are back at the entrance...")
                                   thirdUp()
                     if choice == 'use':
                            if 'lunatic cells keys' in current_inventory:
                                   print("You are now entering a dark area...")
                                   os.startfile(filename1)
                                   LevelWD(current_health, current_inventory)
                            else:
                                   print("You've got to take the key for the door...")
                                   print("You are back at the entrance...")
                                   thirdUp()
       firstUp()
       secondUp()
       thirdUp()
