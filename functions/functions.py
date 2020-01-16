import os
import sys
import time

filename = os.path.realpath('audio\\scary.mp3')
filename1 = os.path.realpath('audio\\door.mp3')
filename2 = os.path.realpath('audio\\boss.mp3')
filename3 = os.path.realpath('audio\\scary1.mp3')
imgfilename = os.path.realpath('images\\image.jpg')
invCounter = 2
quitGame = False
called = False
enableLeft = True
enableRight = True
health = 100
inventory = ['car keys', 'phone']
needed_items = ['car keys', 'phone']
hasPassedSecondUp = False
counter = 0
       
def printInventory(current_inventory):
       print("You currently have: " + " ".join(current_inventory))
def checkHealth():
       global counter
       if health <= 0:
              print("GAME OVER...")
              choice = input("Do you wish to replay?('yes' or 'no') ")
              while choice != 'yes' and choice != 'no':
                     choice = input("Do you wish to replay? ")
              if choice == 'yes':
                            while counter < 6:
                                   print("\n")
                                   if counter == 3:
                                          print("   ---------------------------------NEW GAME-------------------------------")
                                   counter+=1
                            print("[phone ringing]...")
                            print("It is quarter  past 10 PM...")
                            print("- Hello? - you pick the phone up...")
                            print("- It's time... - says the voice on the other side...")
                            print("It is 2 hours later when you find yourself at the gate of the\nyard in front of the abandoned 'Furguson Hospital'")
                            print("You put the car keys into your backpocket and enter through the gate... \nNow you are in the yard.")
                            Intro()
              if choice == 'no':
                     print("Have a very nice and calm night...")
                     sys.exit()
def damage(curr_health, damage):
       global health
       curr_health = curr_health - damage
       print("Your current health state is: " + str(curr_health))
       health = curr_health
       checkHealth()
       return curr_health
def appendToInventory(item):
       global inventory
       global invCounter
       if invCounter > 5:
              print("You can't carry any more items...")
              return 0
       inventory.append(item)
       print(item + " added")
       invCounter+=1
       return inventory
def use(carKeyText = "", phoneText = "", steamPipeText = "", lunaticCellsKeysText = "", gunText = "", scalpelText = ""):
       global called
       global choiceOfItem
       choiceOfItem = input("Choose an item to use: ")
       if choiceOfItem == 'exit':
              return 0
       if choiceOfItem not in inventory:
              print("No such item in your inventory...")
       else:
              if choiceOfItem == 'car keys':
                     print(carKeyText)
              if choiceOfItem == 'phone':
                     if called == False:
                            called = True
                            print(phoneText)
                     else:
                            print("You've already called...")
              if choiceOfItem == 'steam pipe':
                     print(steamPipeText)
              if choiceOfItem == 'lunatic cells keys':
                     print(lunaticCellsKeysText)
              if choiceOfItem == 'pistol':
                     print(gunText)
              if choiceOfItem == 'scalpel':
                     print(scalpelText)          
       return choiceOfItem

def discard():
       global inventory
       global invCounter
       global needed_items
       ItemToDiscard = input("Choose an item to get rid of: ")
       if ItemToDiscard == 'exit':
              return 0
       if ItemToDiscard not in inventory:
              print("This item is not in the inventory...")
       if ItemToDiscard in inventory:
              if ItemToDiscard in needed_items:
                  print("You can't discard this item")
                  return inventory
              else:
                     inventory.remove(ItemToDiscard)
                     print(ItemToDiscard + " removed...")
                     invCounter-=1
                     return inventory

def choose(choiceToProceed, secondChoiceToProceed=None, inventory_enabled = True, Up = "", Left="", Right="", Back="", Interact="", Punch=""):
       choice = input("What do you do?: ")
       while choice != choiceToProceed and choice != secondChoiceToProceed:
              if choice == "up":
                     print(Up)
              if choice == "left":
                     print(Left)
              if choice == "right":
                     print(Right)
              if choice == "back":
                     print(Back)
              if choice == "interact":
                     print(Interact)
              if choice == "punch":
                     print(Punch)
              if inventory_enabled:
                     if choice == "use":
                            choiceOfItem = use()
                     if choice == "inventory":
                            printInventory(inventory)
                     if choice == "discard":
                            inventory = discard()
              else:
                     if choice == "use" or choice == "inventory" or choice == "discard":
                            print("You can't use your inventory...")
                     else:
                            pass
              yield choice
              choice = input("What do you do?: ")
            
              
              
