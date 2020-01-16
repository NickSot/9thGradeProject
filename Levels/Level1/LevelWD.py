import os
import sys
import time
from functions.functions import *
from Levels.Level2.IntroL2 import *

def LevelWD(current_health, current_inventory):
       os.startfile(filename3)
       global time
       global health
       global inventory
       global called
       global filename
       global filename1
       global filename2
       global cTriggered
       cTriggered = False
       called = False
       health = current_health
       inventory = current_inventory
       print("You enter a long hall with lots of open cells in the sides... There is noone in the room but you...")
       print("On your right there is an open cell with many writings on the walls... On your left there is a desk next to a cell with a gun ontop of it... In front of you is the long hall...")
       def firstUp(current_health, current_inventory):
              global counter
              choice = input("What do you do? ")
              while choice != 'left' and choice != 'right' and choice != 'up':
                     if choice == 'use':
                            use("You can't use those keys now...", "- ... - you don't hear anything from the other side\n- Hello. I am at some sort of prison right now...", "You can't use the pipe now...", "You can't use those keys now...")
                     if choice == 'back':
                            print("You can't go back in the main room now... You need to investigate...")
                     if choice == 'interact':
                            print("There is nothing to interact with...")
                     if choice == 'punch':
                            print("You punch the air...")
                     if choice == 'inventory':
                            printInventory(current_inventory)
                     if choice == 'discard':
                            current_inventory = discard()
                     choice = input("What do you do? ")
              if choice == 'left':
                     print("You go to the left...")
                     print("There is the gun with the note...")
                     choice = input("What do you do? ")
                     while choice != 'back':
                            if choice == 'left':
                                   print("You see the cell door and the reception desk behind it...")
                            if choice == 'right':
                                   print("You look at the long dark corridor in front of you...")
                            if choice == 'up':
                                   print("You can't go up...")
                                   print("There is a desk in front of you...")
                            if choice == 'inventory':
                                   printInventory(current_inventory)
                            if choice == 'use':
                                   use("You can't use those keys now...", "", "You can't use the pipe here...", "You can't use the keys now...")
                            if choice == 'discard':
                                   current_inventory = discard()
                            if choice == 'interact':
                                   counter+=1
                                   if counter == 1:
                                          print("You take the pistol...")
                                          current_inventory = appendToInventory("pistol")
                                   if counter == 2:
                                          print("You take the note and read it...")
                                          print("It says: 'There are some strange noices coming from the basement... Also the milk here tastes quite a bit different lately...'")
                            choice = input("What do you do? ")
                     if choice == 'back':
                            print("You go back to the cell door...")
                            print("It's very quiet...")
                            firstUp(current_health, current_inventory)
              if choice == 'right':
                     print("You go to the right and see the writings...")
                     print("They say: 'Hey, there... I've been watching you for a long time now, Nick... Come on... Deeper into the corridor...'")
                     print("You get back at the entrance...")
                     firstUp(current_health, current_inventory)
              print("You continue through the hall and see a door at the other end of it...")
              print("Suddenly you hear a loud noise behind you... The cell door is shut...")
              print("You turn around and see a very tall man with an axe in his hand...")
              os.startfile('images\\axeKiller.jpeg')
       def secondUp():
              global cTriggered
              choice = input("What do you do? ")
              while True:
                     if choice == 'use':
                            use("You start running towards him with the keys and attempt to stab him...\nHe grabs you by the neck and throws you to the ground...", "You try to call the police but the figure is now right in front of you...\nYou feel a very painful blow in the head...", "You take your pipe and attack him...He does not even move...\nHe hits you with his fist and you faint...", "You start running towards him with the keys and attempt to stab him...\nHe grabs you by the neck and throws you to the ground...", "You shoot him in the stomach 3 times. Your ammo has ended...\nHe doesn't even flinch...\nThe tall man rushes at you and hits you in the head with his axe..", "You take your scalpel and rush to the man...\nYou try to slash him but he grabs you by the neck and throws you to the ground...")
                     if choice == 'up':
                            print("You go up to him...He is fast and grabs you by the neck...\nThen you find yourself on the ground...\nSuddenly you see his boot coming down to your face...")
                     if choice == 'back':
                            print("You run back to the door at the end of the corridor...\n- Fuck...FUCK!!!- the door is locked...")
                            print("Your only option is to fight back...")
                            secondUp()
                            break
                     if choice == 'interact':
                            if cTriggered == False:
                                   print("- Hello? - you say shaking...\n- ... - he stands still and silent, while watching you...")
                                   cTriggered = True
                                   secondUp()
                                   break
                            else:
                                   print("- Hello? - you say again waiting for an answer...")
                                   print("The tall figure rushes at you and hits you in the face with his elbow...")
                     if choice == 'punch':
                            print("You rush at him and punch him in the stomach...")
                            print("He doesn't even flinch...")
                            print("Suddenly you feel a very painful strike at the back of your head...")
                     if choice == 'left':
                            print("You look at the cell on your left and there  are writings on it's wall too...")
                            print("They say: 'It's going to be great fun...'")
                            print("Suddenly the tall figure appears to be right in front of you...")
                            print("You feel a painful strike at the back of your head...")
                     if choice == 'right':
                            print("You see a cell but it's empty...")
                            print("Suddenly the tall figure appears to be right in front of you...")
                            print("You feel a painful strike at the back of your head...")
                     if choice == 'discard':
                            print("You can't discard anything now!!!")
                            secondUp()
                            break
                     if choice == 'inventory':
                            print("You can't look at the inventory now...")
                            print("You feel a painful strike at the back of your head...")
                            secondUp()
                            break
                     os.startfile(filename)
                     print("You are now unconscious...")
                     time.sleep(1)
                     IntroL2()
                     break
                     
       firstUp(current_health, current_inventory)
       secondUp()
