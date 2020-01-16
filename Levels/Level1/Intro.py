import os
import sys
import time
from functions.functions import *
from Levels.Level1.LevelD import *
from Levels.Level1.LevelW import *

def Intro():
       print("[phone ringing]...")
       print("It is quarter  past 10 PM...")
       print("- Hello? - you pick it up...")
       print("- It's time... - says the voice on the other side...")
       print("It is 2 hours later when you find yourself at the gate of the\nyard in front of the abandoned 'Furguson Hospital'")
       print("You put the car keys into your backpocket and enter through the gate... \nNow you are in the yard.")
       choice = input("What do you do? ")
       while choice != 'up' and choice != 'back' and choice != 'left' and choice != 'right' and choice != 'punch' and choice != 'interact' and choice != 'discard' and choice != 'inventory' and choice != 'use':
              print("{IF YOU DO NOT KNOW THE COMMANDS OF THE GAME\nPLEASE READ THE TXT FILE IN THE DIRECTORY}\n")
              choice = input("What do you do? ")
       while choice != 'up':
              if choice == 'back':
                     print("The mission is not completed yet...")
              if choice == 'left':
                     print("You look at the beautiful fountain covered in leafs\nbut there is no time for distractions")
              if choice == 'right':
                     print("You see the clocktower of the hospital.\nIt shows 20 past 12 AM. No time to waste...")
              if choice == 'interact':
                     print("There is nothing to interact with...")
              if choice == 'punch':
                     print("You punch the air...")
              if choice == 'inventory':
                     print("You currently have: " + ", ".join(inventory))
              if choice == 'use':
                     use("Can't use the car keys now...", "- How can we help you? - says the voice on the other side\n- I'm at the location...Looks pretty old this place...\n- Good. Keep going and report any stange events...\n- Will do.- you say and hang up...")
              if choice == 'discard':
                     discard()
              choice = input("What do you do? ")
       print("You approach the main gate of the hospital...")
       time.sleep(2)
       os.startfile(imgfilename)
       def firstUp():
              global called
              choice = input("What do you do? ")
              while choice != 'left' and choice != 'right' and choice != 'back':
                     if choice == 'up':
                            print("You can't continue ahead...\nThere is a gate in front of you")
                     if choice == 'interact':
                            print("- Of fucking course!!! It's locked... - you whisper to yourself...")
                     if choice == 'punch':
                            print("You punch the door.")
                            print("It doesn't break...")
                     if choice == 'inventory':
                            print("You currently have: " + "".join(inventory))
                     if choice == 'use':
                            use("Can't use the keys now... You have a mission to attend to...")
                     if choice == 'discard':
                            discard()
                     choice = input("What do you do? ")
              if choice == 'back':
                     print("You get back to the yard gate...")
                     Intro()
              if choice == 'left':
                     print("You turn to the left and see a broken window on the first floor\nwith a garbage bin below it...")
                     print("Maybe you could climb up there and get in...")
                     choice = input("What do you do? ")
                     while choice != 'interact' and choice != 'back':
                            if choice == 'up':
                                   print("There is a wall in front of you...")
                                   print("Can't go this way...")
                            if choice == 'left':
                                          print("You see your BMV behind the yard gate\nbut you must complete the mission first...")
                            if choice == 'right':
                                   print("You see the wall near the gate...")
                            if choice == 'punch':
                                   print("You punch the wall with the window on it... It's still there...")
                            if choice == 'inventory':
                                   print("You currently have: " + "".join(inventory))
                            if choice == 'use':
                                   use("Can't use the keys now...")
                            if choice == 'discard':
                                   discard()
                            choice = input("What do you do? ")
                     if choice == 'interact':
                            print("You start climbing the wall with bare hands ontop of the bin...")
                            print("You barely make it to the window all dusty and dirty...")
                            print("You are now inside...")
                            LevelW()
                     if choice == 'back':
                            print("You get back to the main gate...")
                            firstUp()
                            
              if choice == 'right':
                     print("You see a path, leading to somewhere behind the hospital...")
                     print("You can go and investigate...")
                     choice = input("What do you do? ")
                     while choice != 'up' and choice != 'back':
                            if choice == 'left':
                                   print("You can't go left... There is a wall...")
                            if choice == 'right':
                                   print("You take a look at the bright moon behind your car...")
                            if choice == 'interact':
                                   print("Nothing to interact with...")
                            if choice == 'punch':
                                   print("You punch the air...")
                            if choice == 'inventory':
                                   print("You currently have: " + "".join(inventory))
                            if choice == 'use':
                                   use("Can't use them now...")
                            if choice == 'discard':
                                   discard()
                            choice = input("What do you do? ")
                     if choice == 'up':
                            print("You continue through the tiny path until you see a door leading to the hospital...")
                            print("You open the door carefully and get in...")
                            LevelD()
                     if choice == 'back':
                            print("You get back to the main gate...")
                            firstUp()
       firstUp()
