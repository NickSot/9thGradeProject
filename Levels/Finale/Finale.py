from functions.functions import *
import os
import time

current_health = health

def stronger_friend(current_health):
       friend_health = 100
       print("- So... The rules are simple... You just have to listen to the questions I ask and answer them... Because real strength of an individual are not his musles, but his brain...")
       print("You can see Sonia doing something with her left hand but you don't know what it is...")
       print("The man is standing near a black board apparently explaining the rules of the game...")
       print("Suddenly he spots the motion of the woman's hand.")
       print("Hey, what the fuck?!? - he yells and quickly goes to Sonia.")
       time.sleep(3)
       choices = choose("interact", inventory_enabled=False)
       for choice in choices:
              if choice != "interact":
                     print("You can't move anywhere... You are tied.")
                     friend_health -= 10
                     print("Sonia's health is: " + str(friend_health))
                     
       print("You use on finger to grab the metal pipe near the bed and start pulling as hard as you can...")
       time.sleep(2)
       print("Your left arm is now free...")
       print("The psychopath comes to you and starts beating you up...")
       current_health = damage(current_health, 20)
       print("- HEEELP!!! - Sonia screams...")
       print("She has dialed the police and now they are on their way...")
       print("- SHUT THE FUCK UP!!! - says the man...")
       print("You start untying your right arm...")
       
def Finale(got_friend=False, friend_dead=False):
       global current_health
       print("You wake up but this time on a patient's bed... You are tied very tightly.")
       print("You suddenly see the man with the white apron siting next to you...")
       print("He punches you and knocks a tooth out of your mouth...")
       current_health = damage(current_health, 3)
       if got_friend and not friend_dead:
              print("Sonia is on the bed next to you... She is still asleep...")
              print("- I get out to take the fucking trash out and when I get back I see this shit?!? - the psychopath screams...")
              print("- Whatever... I brought you here in my special place... Both of you... - he says...")
              print("- Here I experiment with my poor victims. Today I want to prove to myself how the stronger organism always wins... - the man says")
              print("Suddenly Sonia wakes up.\n- Oh, and here is the other organism - the lunatic says and laughs maniacally...")
              stronger_friend(current_health)
       if got_friend and friend_dead:
              print("- You motherfucker!!! - you yell at him...")
              print("He punches you one more time but this time harder...")
              current_health = damage(current_health, 5)
              print("- Fuck off you fucking slut!!! - he yells back...")
              print("- You can call me whatever you want but I know what I am... - he then says...")
              print("- I want to play a game...")
              print("You spit in his face... He then starts punching you repeatedly...")
              current_health = damage(current_health, 20)
              print("- Looks like I'll have to teach you some manners, won't I?")
              print("- Why?!?! Why did you do all of this?!? - you ask...")
              print("- Because I can... So back to the game...")
       else:
              print("- I get out for fucking 10 minutes and you turned all the fucking place around!!!")
              print("You turn to the left and see another bed with the woman you saw earlier on it...")
              print("- Oh, she is just a test subject like you... - the man says...")
              print("- Today I decided we shall play a very very fun game! - he continues...")
              print("The woman wakes up and starts screaming immediately...")
              print("The man slaps her.\n- Hey! - you yell...")
              print("He turns around and punches you too...")
              current_health = damage(current_health, 5)
              print("- That's more like it... - he says...")
              
