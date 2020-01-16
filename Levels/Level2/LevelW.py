from functions.functions import *
from Levels.Finale.Finale import *
import os
import time
import random

def LevelW(current_health, current_inventory, got_friend):
       global friend_dead
       enable_left = True
       enable_right = True
       friend_dead = False
       
       print("You enter a big oval room with some sort of altar at the other end of it...")
       print("- What is this?!?! - says Sonia...")
       print("There are two windows both of which are closed...")
       print("- Do you think we can get out? - she asks...")
       print("- I can boost you to the window. But unfortunately I won't be able to climb that high... - you say...")
       print("On your left there is a hook with a chain hanging from the ceiling...")
       print("On your right there is a body with a jigsaw right down his spine...")
       choices = choose("up",
                        Left="You go left...",
                        Right="You turn Right...",
                        Back="You can't go back...",
                        Interact="- This place is fucking terrifying...",
                        Punch="You punch the air... Are you serious?!?!?!")
       for choice in choices:
              if choice == "left":
                     if not enable_left:
                            print("You have nothing to do here anymore...")
                     else:
                            enable_left = False
                            print("You are now next to the hook...")
                            choices = choose("back",
                                             Up="You can't go up...",
                                             Back="You are now back at your previous position...",
                                             Left="You turn to the left and see darkness...",
                                             Right="You see Sonia crouching near the body with a jigsaw in his back...",
                                             Punch="You punch the air... Again...")

                            for choice in choices:
                                   if choice == "interact":
                                          appendToInventory("hook")
                                          inventory = current_inventory
              if choice == "right":
                     if not enable_right:
                            print("You have nothing to do here anymore...")
                     else:
                            enable_right = False
                            print("You are now next to the body with a jigsaw in his back...")
                            choices = choose("back",
                                             Up="You can't go up...",
                                             Back="You are now back at your previous position...",
                                             Left="You turn to the left and see Sonia near the hook...\n- Be careful with this thing... - you say...",
                                             Right="You see darkness...",
                                             Punch="You punch the air... Again...")

                            for choice in choices:
                                   if choice == "interact":
                                          appendToInventory("jigsaw")
                                          inventory = current_inventory


       current_inventory = inventory
       print("- UUUARGHHH! - you hear a roar from behind you...")
       print("You turn around fast and see the same man with the axe who knocked you out...")
       print("You quickly make a roll and he swings his axe and hits the floor...")
       print("- Sonia, stay behind me! - you shout...")
       print("The man turns around to see her completely helpless...")
       print("- Hehe... - he chortles...")
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
       friend_health = 100
       boss_hits = [10, 20, 30]
       os.startfile(filename2)
       hook_counter = 0
       jigsaw_counter = 0
       
       while boss_health > 0:
              if not friend_dead:
                     attacks_friend = random.choice([True, False])
              else:
                     attacks_friend = False
              
              if not attacks_friend:
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
              
              
              else:
                     print("The tall man starts swinging his axe towards Sonia.")
                     timer1 = time.time()
                     choices = choose(("use", "punch", "left", "back", "right"))
                     for choice in choices:
                            if choice == "use":
                                   choiceOfItem = use()
                                   if choiceOfItem == "hook":
                                          hook_counter += 1
                                          timer2 = time.time()
                                          print("- Sonia!!! - you shout...")
                                          timer = timer1 - timer2
                                          if hook_counter < 3:
                                                 if timer < 3:
                                                        print("You hit the tall man with the hook...")
                                                        print("- AAARGH!!! Son of bitch! - he screams...")
                                                        boss_health -= 20
                                                        print("The man has: " + str(boss_health) + " health")
                                                 else:
                                                        hit = random.choice(boss_hits)
                                                        if hit == boss_hits[0]:
                                                               print("The man strikes the woman in the head...")
                                                               friend_health -= hit
                                                        elif hit == boss_hits[1]:
                                                               print("The man strikes Sonia with the wooden part of his axe...")
                                                               friend_health -= hit
                                                        elif hit == boss_hits[2]:
                                                               print("The tall man slices Sonia with his axe")
                                                               friend_health -= hit
                                                        print("Sonia has: " + str(friend_health) + " health")
                                          else:
                                                 print("The hook is broken. You can't use it anymore...")
                                                 hit = random.choice(boss_hits)
                                                 if hit == boss_hits[0]:
                                                        print("The man strikes the woman in the head...")
                                                        friend_health -= hit
                                                 elif hit == boss_hits[1]:
                                                        print("The man strikes Sonia with the wooden part of his axe...")
                                                        friend_health -= hit
                                                 elif hit == boss_hits[2]:
                                                        print("The tall man slices Sonia with his axe")
                                                        friend_health -= hit
                                                 print("Sonia has: " + str(friend_health) + " health")

                                   if choiceOfItem == "jigsaw":
                                          jigsaw_counter_counter += 1
                                          timer2 = time.time()
                                          print("- Sonia!!! - you shout...")
                                          timer = timer1 - timer2
                                          if jigsaw_counter_counter < 3:
                                                 if timer < 3:
                                                        print("You slice the tall man with the jigsaw...")
                                                        print("- AAARGH!!! That fucking hurt! - he screams...")
                                                        boss_health -= 20
                                                        print("The man has: " + str(boss_health) + " health")
                                                 else:
                                                        hit = random.choice(boss_hits)
                                                        if hit == boss_hits[0]:
                                                               print("The man strikes the woman in the head with his fist...")
                                                               friend_health -= hit
                                                        elif hit == boss_hits[1]:
                                                               print("The man strikes Sonia with the wooden part of his axe...")
                                                               friend_health -= hit
                                                        elif hit == boss_hits[2]:
                                                               print("The tall man slices Sonia with his axe")
                                                               friend_health -= hit
                                                        print("Sonia has: " + str(friend_health) + " health")
                                          else:
                                                 print("The jigsaw is broken. You can't use it anymore...")
                                                 hit = random.choice(boss_hits)
                                                 if hit == boss_hits[0]:
                                                        print("The man strikes the woman in the head...")
                                                        friend_health -= hit
                                                 elif hit == boss_hits[1]:
                                                        print("The man strikes Sonia with the wooden part of his axe...")
                                                        friend_health -= hit
                                                 elif hit == boss_hits[2]:
                                                        print("The tall man slices Sonia with his axe")
                                                        friend_health -= hit
                                                 print("Sonia has: " + str(friend_health) + " health")


                            if choice == "punch":
                                   print("You punch the man but he doesn't even flinch...")
                                   boss_health -= 3
                                   print(str(boss_health))
                                   print("He turns around and hits you harder...")
                                   current_health = damage(current_health, 5)
                                   health = current_health
                            else:
                                   print("You can't do this now! Sonia is in danger!")
                                   hit = random.choice(boss_hits)
                                   if hit == boss_hits[0]:
                                          print("The man strikes the woman in the head...")
                                          friend_health -= hit
                                   elif hit == boss_hits[1]:
                                          print("The man strikes Sonia with the wooden part of his axe...")
                                          friend_health -= hit
                                   elif hit == boss_hits[2]:
                                          print("The tall man slices Sonia with his axe")
                                          friend_health -= hit
                                   print("Sonia has: " + str(friend_health) + " health")

                            if friend_health <= 0:
                                   friend_dead = True
                                   print("- NO!!! - you see the man slicing her throat... She grasps for air, but can't breathe...")
                                   print("Sonia is dead...")
                                   
                            break


              print("The man is dead...")
              if friend_dead:
                     print("You go to Sonia's body... You can see her fingers moving unintentionally...")
                     print("You start crying...")
                     print("Suddenly you start feeling bad...")
                     print("You pewk...")
                     print("You don't feel anything for a moment and then fall asleep on your own vomit.")
                     print("You can see a blurry figure coming to both of you. It's the psychopath that was with you in the other room...")
              else:
                     print("- Son of a bitch! - you say and see him dead...")
                     print("Sonia is standing stupified...")
                     print("- It's ok he is dead now... - you try to calm her down...")
                     print("You see her calming down a little bit...")
                     print("Suddenly you start feeling bad. Both of you. Sonia vomits and then you... You both fall on the ground paralized...")
                     print("You can see a blurry figure coming to both of you. It's the psychopath that was with you in the other room...")

              Finale(got_friend, friend_dead)
