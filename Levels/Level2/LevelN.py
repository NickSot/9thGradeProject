import os
import time
import random
from functions.functions import *
from Levels.Finale.Finale import *

def LevelN(current_health, current_inventory):
       enable_left = True
       enable_right = True
       health = current_health
       inventory = current_inventory
       os.startfile(filename3)
       print("In front of you is a big dark room... It's oval and there are windows on the ceiling...")
       print("Looks like it's some kind of church...")
       print("- What the fuck is this?!?! - you ask yourself...")
       print("You see the moonlight glaring through. It's almost morning...")
       print("On your left there is a hook hanging from the ceiling...")
       print("On your right there is a bloody corpse with a jigsaw through his back...")
       choices = choose("up",
                        Left="You go to the hook...",
                        Right="You go to the body with the jigsaw inside his back...",
                        Back="Can't go back...",
                        Interact="You can't interact with aything here...",
                        Punch="You punch the air...",
                        )

       for choice in choices:
              if choice == "left":
                     enable_left = False
                     choices1 = choose("back",
                                      Up="You can't go up...",
                                      Left="You turn to the left and see the door you came through...",
                                      Right="You turn to the right and see the big room...",
                                      Back = "You get back to your previous position...",
                                      Punch="You punch the air..."
                                      )
                     for choice1 in choices1:
                            if choice1 == "interact":
                                   current_inventory = appendToInventory("hook")
                                   inventory = current_inventory
                            
              if choice == "right":
                     enable_right = False
                     choices1 = choose("back",
                                      Up="You can't go up...",
                                      Left="You turn to the left and see the big room...",
                                      Right="You turn to the right and see the door you went through...",
                                      Back = "You get back to your previous position...",
                                      Punch="You punch the air..."
                                      )
                     for choice1 in choices1:
                            if choice1 == "interact":
                                   current_inventory = appendToInventory("jigsaw")
                                   inventory = current_inventory
              if choice == "back":
                     print("You get back to your previous position...")
                                   
       current_inventory = inventory
       print("- UUUARGHHH! - you hear a roar from behind you...")
       print("You turn around fast and see the same man with the axe who knocked you out...")
       print("You quickly make a roll and he swings his axe and hits the floor...")
       time.sleep(2)
       print("{You are entering a boss fight...\nEvery action must be completed in less than or 3 seconds.\nIf you dont, you will lose health and eventually die...}")
       print("Prepare...")
       time.sleep(4)
       i = 0
       while i < 3:
              print(str(i + 1))
              time.sleep(1)
              i+=1
       boss_health = 100
       boss_hits = [10, 20, 30]
       os.startfile(filename2)
       hook_counter = 0
       jigsaw_counter = 0
       
       while boss_health > 0:
              print("The tall man starts swinging his axe towards you...")
              timer1 = time.time()
              choices = choose(("use", "punch", "left", "back", "right"))
              for choice in choices:
                     if choice == "use":
                            choiceOfItem = use()
                            if choiceOfItem == "hook":
                                   hook_counter += 1
                                   timer2 = time.time()
                                   timer = timer2 - timer1
                                   if hook_counter < 4:
                                          if timer < 3:
                                                 print("You throw the hook at the man and it hits him...")
                                                 print("ARGH!!! - the roars yells in pain")
                                                 boss_health -= 20
                                                 print(str(boss_health))
                                                 print("You get your hook back to yourself with the chains...")
                                   
                                          else:
                                                 hit = random.choice(boss_hits)
                                                 if hit == boss_hits[0]:
                                                        current_health = damage(current_health, hit)
                                                        health = current_health
                                                 elif hit == boss_hits[1]:
                                                        current_health = damage(current_health, hit)
                                                        health = current_health
                                                 elif hit == boss_hits[2]:
                                                        current_health = damage(current_health, hit)
                                                        health = current_health
                                   else:
                                          print("The hook is broken... You can't use it anymore")
                                          hit = random.choice(boss_hits)
                                          if hit == boss_hits[0]:
                                                 current_health = damage(current_health, hit)
                                                 health = current_health
                                          elif hit == boss_hits[1]:
                                                 current_health = damage(current_health, hit)
                                                 health = current_health
                                          elif hit == boss_hits[2]:
                                                 current_health = damage(current_health, hit)
                                                 health = current_health
                                                 
                            if choiceOfItem == "jigsaw":
                                   jigsaw_counter += 1
                                   timer2 = time.time()
                                   timer = timer2 - timer1
                                   if jigsaw_counter > 3:       
                                          if timer  < 3:
                                                 print("You slice the tall man with the jigsaw...")
                                                 print("- AAARGH! Fucker...")
                                                 boss_health -= 20
                                          else:
                                                 hit = random.choice(boss_hits)
                                                 if hit == boss_hits[0]:
                                                        current_health = damage(current_health, hit)
                                                        health = current_health
                                                 elif hit == boss_hits[1]:
                                                        current_health = damage(current_health, hit)
                                                        health = current_health
                                                 elif hit == boss_hits[2]:
                                                        current_health = damage(current_health, hit)
                                                        health = current_health
                                   else:
                                          print("The jigsaw is broken... You can't use it anymore")
                                          hit = random.choice(boss_hits)
                                          if hit == boss_hits[0]:
                                                 current_health = damage(current_health, hit)
                                                 health = current_health
                                          elif hit == boss_hits[1]:
                                                 current_health = damage(current_health, hit)
                                                 health = current_health
                                          elif hit == boss_hits[2]:
                                                 current_health = damage(current_health, hit)
                                                 health = current_health
                     if choice == "punch":
                            timer2 = time.time()
                            timer = timer2 - timer1
                            if timer < 3:
                                   print("You punch him in the stomach but he strikes you in the face...")
                                   current_health = damage(current_health, 5)
                                   health = current_health
                                   boss_health -= 3
                                   print("The man has: " + str(boss_health) + " health")
                            else:
                                   hit = random.choice(boss_hits)
                                   if hit == boss_hits[0]:
                                          print("You don't punch him in time and he hits you with the wooden part of the axe you...")
                                          current_health = damage(current_health, hit)
                                          health = current_health
                                   elif hit == boss_hits[1]:
                                          print("You don't punch him in time and he hits you with the metal part of the axe you...")
                                          current_health = damage(current_health, hit)
                                          health = current_health
                                   elif hit == boss_hits[2]:
                                          print("You don't punch him in time and he slices you with the axe you...")
                                          current_health = damage(current_health, hit)
                                          health = current_health
                     if choice == "up":
                            print("You go up to the man...")
                            hit = random.choice(boss_hits)
                            if hit == boss_hits[0]:
                                   print("He hits you with the wooden part of the axe you...")
                                   current_health = damage(current_health, hit)
                                   health = current_health
                            elif hit == boss_hits[1]:
                                   print("He hits you with the metal part of the axe you...")
                                   current_health = damage(current_health, hit)
                                   health = current_health
                            elif hit == boss_hits[2]:
                                   print("He slices you with the axe you...")
                                   current_health = damage(current_health, hit)
                                   health = current_health
                     if choice == "interact":
                            timer2 = time.time()
                            timer = timer2 - timer1
                            if timer < 3:
                                   print("You grab the man but he pushes you off and slaps you...")
                                   damage(current_health, 5)
                                   boss_health -= 2
                                   print("The man has: " + str(boss_health) + " health")
                            else:
                                   print("You fail to grab the man")
                                   hit = random.choice(boss_hits)
                                   if hit == boss_hits[0]:
                                          print("He hits you with the wooden part of the axe you...")
                                          current_health = damage(current_health, hit)
                                          health = current_health
                                   elif hit == boss_hits[1]:
                                          print("He hits you with the metal part of the axe you...")
                                          current_health = damage(current_health, hit)
                                          health = current_health
                                   elif hit == boss_hits[2]:
                                          print("He slices you with the axe you...")
                                          current_health = damage(current_health, hit)
                                          health = current_health   
                     else:
                            timer2 = time.time()
                            timer = timer2 - timer1
                            if timer < 3:
                                   print("You dodge the man's attack...")
                            else:
                                   hit = random.choice(boss_hits)
                                   if hit == boss_hits[0]:
                                          print("You don't dodge in time and he hits you with the wooden part of the axe you...")
                                          current_health = damage(current_health, hit)
                                          health = current_health
                                   elif hit == boss_hits[1]:
                                          print("You don't dodge in time and he hits you with the metal part of the axe you...")
                                          current_health = damage(current_health, hit)
                                          health = current_health
                                   elif hit == boss_hits[2]:
                                          print("You don't dodge in time and he slices you with the axe you...")
                                          current_health = damage(current_health, hit)
                                          health = current_health
                     break
                                                        
       
       os.startfile(filename3)
       print("The man is lying in front of you on the ground with blood rushing out of his mouth...")
       print("You are back at your previous position at the entrance...")
       choices = choose("up")
       for choice in choices:
              if choice == "left":
                     if not enable_left:
                            print("You have nothing to do here anymore...")
                     else:
                            choices1 = choose("back",
                                      Up="You can't go up...",
                                      Left="You turn to the left and see the door you came through...",
                                      Right="You turn to the right and see the big room...",
                                      Back = "You get back to your previous position...",
                                      Punch="You punch the air..."
                                      )
                            for choice1 in choices1:
                                   if choice1 == "interact":
                                          current_inventory = appendToInventory("hook")
                                          inventory = current_inventory
              if choice == "right":
                     if not enable_right:
                            print("You have nothing to do here anymore...")
                     else:
                            choices1 = choose("back",
                                      Up="You can't go up...",
                                      Left="You turn to the left and see the big room...",
                                      Right="You turn to the right and see the door you went through...",
                                      Back = "You get back to your previous position...",
                                      Punch="You punch the air..."
                                      )
                            for choice1 in choices1:
                                   if choice1 == "interact":
                                          current_inventory = appendToInventory("jigsaw")
                                          inventory = current_inventory
              
       print("You go to some sort of altar...")
       print("There are lit candles ontop of it and an icon of the man who was torturing you earlier...")
       print("Also there is a piece of paper next to the icon...")
       print("- What the hell?!?! - you say outloud...")
       choices = choose("back",
                        Up="You can't go up...",
                        Left="On your left is nothing but a window...",
                        Right="You see a dead rat impaled on a metal spike...",
                        Punch="You punch the altar. Nothing happens...",
                        Interact="You take the letter and it reads: 'I asked Layla to buy some sedatives for the patients...\nI think their behaviour is really uncommon...\ I'm starting to speculate that somethin or someone is making them do stuff like this.'")
       for choice in choices:
              if choice == "back":
                     os.startfile(filename2)
                     print("Just as you head back to exit the room the tall man grabs you by the throat...")
                     print("- You are so fucked, mate! Soon you will be real sorry for coming here! - he spills blood from his mouth to your face and dies.")
                     print("- What the FUCK?!?!?! - you spit out the blood that has entered your mouth...")
                     print("- I already am fucking asshole!")
                     print("You get back to the room you went through but everything seems quite different...")
                     print("There is a disco ball at the center and there is no chair. The woman who was lying on the floor is now dancing.")
                     print("Her stomach is torn and her insides are hanging out and dripping slowly. She is screaming in pain, looking at you.")
                     print("You vomit. The whole floor gets covered in your vomit and you continue as the level of it starts rising.")
                     print("Suddenly you both start drowning in the vomit you have produced...")
                     
              
       Finale()
