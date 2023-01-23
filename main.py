import os, time

water = 100
boat = False
whale = False


def startGame():
  os.system('clear') # clear the screen for the player
  print("Welcome! You are the main character navigating through the Seven Seas.")
  print()
  print()
  print("Let's get to the ocean!")
  time.sleep(5) # wait 3 seconds before moving on
  seaShore() # runs to send the player to cave #1

def seaShore():
  global boat # use the boat variable from the top
  os.system('clear')
  if boat:
    print("You are in the boat. Would you like to sail?")
  else:
    print("You are in the sea. There is a boat on the shore, will you sail or stay? What would you like to do?")
  decision = input(">>").strip().lower()
  if decision.find("boat") > -1:
    print("Picking up the boat.")
    boat = True
    time.sleep(3)
    seaShore()
  elif decision.find("stay") > -1:
    print("You got scarred and ended up collecting sea shells.")
    time.sleep(3)
    seaShore()
  elif decision.find("sail") > -1:
    print("Sailing into the deep blue sea .")
    time.sleep(3)
    oceanBlue()
  else:
    print("Sorry, that command is not found.")
    time.sleep(3)
    seaShore()

  
def oceanBlue():
  global water
  os.system('clear')
  print("Welcome to the deep blue sea")
  print()
  print()
  print("welcome do not fall off the boat be careful on your journey")
  time.sleep(5) # wait 3 seconds before moving on
  deepBlueSea() # runs to send the player to cave #1

def deepBlueSea():
  global water # use the water variable from the top
  os.system('clear')
  if water:
    print("You are in the Sea. Are you thirsty? Yes or No")
  else:
    print("You are in the sea. There is a bucket of water on the boat, will you drink it yes or no? What would you like to do?")
  decision = input(">>").strip().lower()
  if decision.find("water") > -1:
    print("Picking up the water.")
    water = True
    time.sleep(3)
    deepBlueSea()
  elif decision.find("yes") > -1:
    print("You drank it and there was some flies in it but its alright because if not you would have fainted from dehydration.")
    time.sleep(3)
    findingCompany() #this where im at 
  elif decision.find("no") > -1:
    print("You fainted and the boat fliped now you are drowning. Oh No!")
    time.sleep(3)
    oceanBlue()
  else:
    print("Sorry, that command is not found.")
    time.sleep(3)
    oceanBlue()


def horizon():
  global whale
  os.system('clear')
  pass
  
def findingCompany():
  global whale 
  os.system('clear')
  if whale:
    print("You so lonly will u befriend the whale")
  else:
    print("You so lonly will u befriend the whale? Make a friend? Yes or No")
  decision = input(">>").strip().lower()
  if decision.find("whale") > -1:
    print("Make a friend.")
    whale = True
    time.sleep(3)
    findingCompany()
  elif decision.find("yes") > -1:
    print("You made a friend and heading back to civilation.")
    time.sleep(3)
    endGame()
  elif decision.find("no") > -1:
    print("You are so lonley and will spend your last days in sea")
    time.sleep(3)
    findingCompany()
  else:
    print("Sorry, that command is not found.")
    time.sleep(3)
    findingCompany()

def endGame():
  os.system("clear")
  print ("congratulations!!! You're alive. The End!")
  time.sleep(5)
  os.system("clear")
  

startGame()