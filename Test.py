import pygame
pygame.init()
screenSize=(640,480)
surface=pygame.display.net_node(screenSize)
pygame.display.flip()
import random
import time
global bossh
bossh=250
global wboss
wboss=1
global p1_name
p1_name=0
global p2_name
p2_name=0
x=0
y=0
subclass1=0
subclass2=0
bandages=0
bandages2=0
p1weapon="Sword"
p2weapon="Sword"
global attack_damagelight1
attack_damagelight1=10
global attack_damagelight2
attack_damagelight2=10
global attack_damageheavy1
attack_damageheavy1=10
global attack_damageheavy2
attack_damageheavy2=10
global p1_health
p1health=100
global p2health
p2health=100
global money1
money1=random.randint(5000,20000)
global money2
money2=random.randint(5000,20000)
money1=int(money1)
money2=int(money2)
#Variable Defining
def bloodvilla():
  print("Welcome to the Village of Bloodmist!")
  print("You both arive at the village and find thieves robbing houses.")
  print
def purgatoryone():
  print("Nice Job!")
  print("You beat the easiest dungeon.")
  print("Player 1 Health")
  print(p1health)
  print("Player 2 Health")
  print(p2health)
  print("Each person Gets 20 Health!")
  p1health=p1health+20
  p2health=p2health+20
  print("Each Person Also gets 5 bandages")
  bandages=bandages+5
  bandages2=bandages2+5
  des1=input("Do you want to go to A.) the Village of the Bloodmist(Easy) or B.) the Lavapool(Hard)?")
  des1=str(des1)
  if des1=="A":
    
def firstdungeon():
  print("You beat the first dungeon!")
def lightcast2():
  global bossh
  print("You used your Lightning Cast spell!")
  print("It did 5 damage to the boss.")
  bossh=bossh-5
  dragonfight()
def maget2():
  global p2health
  print("You Choose to heal your teammate.")
  print("You gained 5 health.")
  p2health=p2health+5
  dragonfight()
    
  
def mageself2():
  global p2health
  print("You Choose to heal yourself.")
  print("You gained 5 health.")
  p2health=p2health+5
  dragonfight()
def fightmechanicsmage2():
  print("Player 2")
  fightop1=input("What do you do, Heal Yourself, Lightning Cast,Heal Teammate?")
  if fightop1=="Heal Yourself":
    mageself2()
  if fightop1=="Lightning Cast":
    lightcast2()
  if fightop1=="Heal Teammate":
    maget2()
def lightcast1():
  global bossh
  print("You used your Lightning Cast spell!")
  print("It did 5 damage to the boss")
  bossh=bossh-5
  if subclass2=="Healer":
    fightmechanicsmage2()
  else:
    fightmechanics2()
def maget1():
  global p2health
  print("You Choose to heal your teamate.")
  print("You gained 5 health")
  p2health=p2health+5
  if subclass2=="Healer":
    fightmechanicsmage2()
  else:
    fightmechanics2()
def mageself1():
  global p1health
  print("You Choose to heal yourself.")
  print("You gained 5 health")
  p1health=p1health+5
  fightmechanicsmage2()
def fightmechanicsmage1():
  print("Player 1")
  fightop1=input("What do you do, Heal Yourself, Lightning Cast,Heal Teammate?")
  if fightop1=="Heal Yourself" or "hy":
    mageself1()
  if fightop1=="Lightning Cast" or "la":
    lightcast1()
  if fightop1=="Heal Teammate" or "ht":
    maget1()
    
def playerdodge2():
  global bossh
  global p2health
  print(p2_name)
  print("The boss is attacking you!")
  dodgep1=input("Dodge left or right?")
  dodgep1=random.randint(1,10)
  if dodgep1>=7:
    print("You took no damage.")
    if subclass1=="Healer":
      fightmechanicsmage1()
    else:
      fightmechanics1()
  if dodgep1<=7:
    print("You took 10 damage.")
    p2health=p2health-10
    print("Health ")
    print(p2health)
    if subclass1=="Healer":
      fightmechanicsmage1()
    else:
      fightmechanics1()
    
def playerdodge1():
  global bossh
  global p1health
  print(p1_name)
  print("the boss is attacking you!")
  dodgep1=input("Dodge left or right")
  dodgep1=random.randint(1,10)
  if dodgep1>=7:
    print("You took no damage")
    if subclass1=="Healer":
      fightmechanicsmage1()
    else:
      fightmechanics1()
  if dodgep1<=7:
    print("You took 10 damage.")
    p1health=p1health-10
    print("Health ")
    print(p1health)
    if subclass1=="Healer":
      fightmechanicsmage1()
    else:
      fightmechanics1()

def dragonfight():
  global wboss
  if p1health==0:
    print("You Lost!")
  if p2health==0:
    print("You Lost!")
  if bossh<=1 and wboss==1:
      archerafter()
  if bossh<=1 and wboss==2:
      afterfight2()
  if bossh<=1 and wboss==3:
      almosts()
  if bossh<=1 and wboss==4:
      firstdungeon()
  print("The enemy launches its attack.")
  playerhit=random.randint(1,2)
  if playerhit==1:
    playerdodge1()
  if playerhit==2:
    playerdodge2()

def hidenheal2():
  global bossh
  global p1health
  print("You decided to hide and heal. ")
  if bandages2==0:
    print("You don't have any bandages left, its the boss's turn.")
    dragonfight()
  else:
    print("You recover 5 health.")
    p2health=p2health+5
    print("Health "+p2health)
    dragonfight()
#Heal For player 2
def heavya2():
  global bossh
  global wboss
  global p2health
  print("You decide to do a heavy attack.")
  rheavy2=random.randint(1,10)
  if rheavy2>=6.5:
    print("You missed your heavy attack, you were out in the open so you took 5 damage.")
    p2health=p2health-5
    print("Player 2 Health ")
    print(p2health)
    dragonfight()
  else:
    print("Your heavy attack was sucessful!")
    bossh=bossh-attack_damageheavy2
    if bossh<=1 and wboss==1:
      archerafter()
    if bossh<=1 and wboss==2:
      afterfight2()
    if bossh<=1 and wboss==3:
      almosts()
    if bossh<=1 and wboss==4:
      firstdungeon()
    print("Boss Health,")
    print(bossh)
    if bossh<=1:
      print("You defeated the boss.")
    dragonfight()
def lighta2():
  global wboss
  global bossh
  global p2health
  print("You decide to do a light attack.")
  rlight2=random.randint(1,10)
  if rlight2>=9.5:
    print("You missed your light attack, you were out in the open so you took 5 damage.")
    p2health=p2health-5
    print("Player 2 Health ")
    print(p2health)
    dragonfight()
  else:
    print("Your light attack was sucessful!")
    bossh=bossh-attack_damagelight2
    print("Boss Health ")
    print(bossh)
    dragonfight()
    if bossh<=1 and wboss==1:
      archerafter()
    if bossh<=1 and wboss==2:
      afterfight2()
    if bossh<=1 and wboss==3:
      almosts()
    if bossh<=1 and wboss==4:
      firstdungeon()

def fightmechanics2():
  
  print("Player 2")
  fightop1=input("What do you do? Hide and bandage, Light Attack, or Heavy Attack")
  if fightop1=="Hide and Bandage" or "hob":
    hidenheal2()
  if fightop1=="Light Attack" or "la":
    lighta2()
  if fightop1=="Heavy Attack" or "ha":
    heavya2()


def hidenheal1():
  global subclass1
  global subclass2
  global bossh
  global p1health

  print("You decided to hide and heal")
  time.sleep(0.4)
  if bandages==0:
    print("You don't have any bandages left, it's your partners turn.")
    if subclass2=="Healer":
      fightmechanicsmage2()
    else:
      fightmechanics2()
  else:
    print("You recover 5 health.")
    p1health=p1health+5
    print("Health "+p1health )
    if subclass2=="Healer":
      fightmechanicsmage2()
    else:
      fightmechanics2()
#heal for First Player
def heavya1():
  global wboss
  global subclass1
  global subclass2
  global bossh
  global p1health
  print("You decide to do a heavy attack.")
  time.sleep(0.4)
  rheavy2=random.randint(1,10)
  if rheavy2>=5:
    print("You missed your heavy attack, you were out in the open so you took 5 damage.")
    p1health=p1health-5
    print("Player 1 Health")
    print(p1health)
    if subclass2=="Healer":
      fightmechanicsmage2()
    else:
      fightmechanics2()
  else:
    print("Your heavy attack was sucessful!")
    time.sleep(0.4)
    bossh=bossh-attack_damageheavy1
    if bossh<=1 and wboss==1:
      archerafter()
    if bossh<=1 and wboss==2:
      afterfight2()
    if bossh<=1 and wboss==3:
      almosts()
    if bossh<=1 and wboss==4:
      print("Boss Health,")
      print(bossh)
    if subclass2=="Healer":
      fightmechanicsmage2()
    else:
      fightmechanics2()
      
def lighta1():
  global subclass1
  global subclass2
  global p1health
  global wboss
  time.sleep(0.4)
  print("You decide to do a light attack.")
  rheavy2=random.randint(1,10)
  if rheavy2>=8:
    time.sleep(0.4)
    print("You missed your light attack, you were out in the open so you took 5 damage.")
    p1health=p1health-5
    print("Player 1 Health")
    print(p1health)
    if subclass2=="Healer":
      fightmechanicsmage2()
    else:
      fightmechanics2()
  else:
    time.sleep(0.4)
    global bossh
    print("Your light attack was successful!")
    bossh=bossh-attack_damagelight1
    print("Boss Health,")
    print(bossh)
    if subclass2=="Healer":
      fightmechanicsmage2()
    else:
      fightmechanics2()
    if bossh<=1 and wboss==1:
      archerafter()
    if bossh<=1 and wboss==2:
      afterfight2()
    if bossh<=1 and wboss==3:
      almosts()
    if bossh<=1 and wboss==4:
      firstdungeon()
def fightmechanics1():
  print("Player 1")
  fightop1=input("What do you do? Hide and bandage, Light Attack, or Heavy Attack")
  if fightop1=="Hide and Bandage" or "hob":
    hidenheal1()
  if fightop1=="Light Attack" or "la":
    lighta1()
  if fightop1=="Heavy Attack" or "ha":
    heavya1()
def dungeon1left():
  global subclass1
  global subclass2
  print("You walk for about five minutes and find that the dungeon opens up.")
  print("You see a dragon with a wooden chest behind him.")
  print("The dragon turns and looks at you..... get ready for a fight.")
  if subclass1=="Healer":
      fightmechanicsmage1()
  else:
      fightmechanics1()
def dungeon1right():
  print("You walk to the end of the right side......You seem to be going in a loop and find yourself back at the start.")
  dungeonstart1()
def dungeonstart1():
  print("You come across the entrance and you have a decision,")
  side=input("Left or Right")
  side=str(side)
  if side=="Left":
    dungeon1left()
    
  if side=="Right":
    dungeon1right()
  
def adstart():
  print("Your adventure begins in your first dungeon")
  dungeonstart1()

def moneyadd1():
  global x
  global money1
  money1=money1+x
  x=0
  print(money1)
#This is The Money Function to add money player 1.

def moneysub1():
  money1=money1-y
  y=0
  print(money1)
#This is the function to Subtract Money player 1.

def moneyadd2():
  global x
  global money2
  money2=money2+x
  x=0
  print(money2)
#This is The Money Function to add money player 2.

def moneysub2():
  global y
  money2=money2-y
  y=0
  print(money2)
#This is the function to Subtract Money player 2.

#Start of Game
def startgame():
  global subclass1
  global subclass2
  import random
  import time
  global bossh
  global wboss
  wboss=1
  bossh=250
  global p1_name
  p1_name=0
  global p2_name
  p2_name=0
  x=0
  y=0
  bandages=0
  bandages2=0
  p1weapon="Sword"
  p2weapon="Sword"
  global attack_damagelight1
  attack_damagelight1=10
  global attack_damagelight2
  attack_damagelight2=10
  global attack_damageheavy1
  attack_damageheavy1=10
  global attack_damageheavy2
  attack_damageheavy2=10
  global p1health
  p1health=100
  global p2health
  p2health=100
  global money1
  money1=random.randint(5000,20000)
  global money2
  money2=random.randint(5000,20000)
  money1=int(money1)
  money2=int(money2)
#Variable Defining
  print("Welcome to the world of Oropos! This is our two person co-operative game.")
  time.sleep(0.4)
  print("The object of this game is go through the adventure and stay alive. On the way, you can earn loads of gold to help you.")
  time.sleep(0.4)
  print("Let's start.")
  time.sleep(0.4)
  p1_name=input("What is your name?")
  p1_name=str(p1_name)
  time.sleep(0.4)
  print("Hello and welcome, "+ p1_name)
  time.sleep(0.4)
  print("")
  p2_name=input("What is your name Player 2?")
  p2_name=str(p2_name)
  time.sleep(0.4)
  print("Hello and welcome, "+ p2_name)
  time.sleep(0.4)
  print("")
  print("You have a big decision ahead of you "+p1_name)
  time.sleep(0.4)
  print("A Mage. A long range, squishy, magic attacker with decent damage.")
  time.sleep(0.4)
  print("A Healer. A medic at the back who helps injured comrades survive to fight another battle.")
  time.sleep(0.4)
  print("A Rogue. A full attacker with huge damage, but with extremely low health.")
  time.sleep(0.4)
  print("Or a Knight. A decently healthed, all around average fighter.  ")
  subclass1=input("What class will you be?")
  time.sleep(0.4)
  subclass1=str(subclass1)
  if subclass1=="Mage":
    attack_damagelight1=30
    attack_damageheavy1=40
    p1health=80
  if subclass1=="Healer":
    attack_damagelight1=5
    attack_damageheavy1=10
    p1health=300
  if subclass1=="Rogue":
    attack_damagelight1=45
    attack_damageheavy1=70
    p1health=30
  if subclass1=="Knight":
    attack_damagelight1=20
    attack_damageheavy1=30
    p1health=100
  time.sleep(0.4)
  print("Great You are a "+ subclass1+" "+ p1_name)
  print("")
  print("")
  print("You have a big choice ahead of you "+p2_name)
  subclass2=input("What class will you be? Mage, Healer, Rogue, or Knight?")
  subclass2=str(subclass2)
  if subclass2=="Mage":
    attack_damagelight2=30
    attack_damageheavy2=40
    p2health=80
  if subclass2=="Healer":
    attack_damagelight2=5
    attack_damageheavy2=10
    p2health=300
  if subclass2=="Rogue":
    attack_damagelight2=45
    attack_damageheavy2=70
    p2health=30
  if subclass2=="Knight":
    attack_damagelight2=20
    attack_damageheavy2=30
    p2health=100
    time.sleep(0.4)
  print("Great You are a "+subclass2+" "+p2_name)
  time.sleep(0.4)
  print("According to your class, it will determine your health and attack. Everything will be displayed below.")
  print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
  time.sleep(0.4)
  print("Health For Player 1")
  print(p1health)
  time.sleep(0.4)
  print("Health for Player 2")
  print(p2health)
  time.sleep(0.4)
  print("Player 1 Attack Damage")
  print(attack_damagelight1)
  time.sleep(0.4)
  print("Player 2 Attack Damage")
  print(attack_damagelight2)
  time.sleep(0.4)
  print("Now that you know all of your stats you will now begin your quest.")
  wakeup()
def wakeup():
  print("Gahhhhh, what was that dream...?")
  time.sleep(0.4)
  print("Ehh whatever.")
  time.sleep(0.4)
  print("Anyways, today's the big day!")
  time.sleep(0.4)
  print("I'm going to go to the Capital to get my first quest alongside my friend")
  time.sleep(0.4)
  print("I hear it's gonna be worth alot of gold. Woo whee!")
  time.sleep(0.4)
  print("Let's see what I should get...")
  time.sleep(0.4)
  print("Some money")
  time.sleep(0.4)
  print("And a map.")
  time.sleep(0.4)
  print("Here is a picture of the map :")
  time.sleep(0.4)
  kingdom()
  print("Now it's time to meet")
  time.sleep(0.4)
  print("...")
  time.sleep(0.1)
  print("...")
  time.sleep(0.1)
  print("...") 
  time.sleep(0.1)
  print("Player 1 Meets Up With Player 2.")
  time.sleep(0.4)
  print("*They share info.*")
  time.sleep(0.4)
  print(money1)
  time.sleep(0.4)
  print(money2)
  time.sleep(0.4)
  print("You guys prepare to leave.")
  time.sleep(0.4)
  info=input("Would you like to learn more about the places you are going to?")
  if info=="Yes":
    learning()
  if info=="No":
    decision1()
def learning():
  print("Watching Mountains.")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("One of the mysterious places in the world of Oropos.")
  time.sleep(0.4)
  print("Known for it's weird, moving eye at the top of the highest peak.")
  time.sleep(0.4)
  print("Travelers who went exploring in these mountain always ends up battered up after leaving.")
  time.sleep(0.4)
  print("Noone knows why... as they won't tell.")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("Village of the Bloodmist.")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("One of the most dangerous places in the world.")
  time.sleep(0.4)
  print("Rumors say this village trains their kids so hard, that they are forced into a killing competition between each other just to graduate.")
  time.sleep(0.4)
  print("That's how they got the name 'Bloodmist'...")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("Village of the Edge.")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("The place known for the bravery of it's soldiers.")
  time.sleep(0.4)
  print("They are willing to die for anything just to protect their honor.")
  time.sleep(0.4)
  print("Rumors say they never lose stamina if it's for the protection of others.")
  decision1()
def decision1():
  decision=input("*Do you want to A.) go to the Watching Mountains (Easy difficulty) , B.) go to the Village of the Bloodmist (Normal Difficulty) or C.) go to the Village of the Edge (Hard Difficulty)?*")
  if decision=="A":
    print("Alright, let's go to the Watching Mountain first!")
    dungeon_mountains()
  if decision=="B":
    print("Alright, let's go to the Village of the Bloodmist first!")
    bloodmist()
  if decision=="C":
    print("Alright, let's go to the Village of the Edge first!")
    
def kingdom():  
  print("|___________________________________________________________________________________________________________________________________________________________________________________________________________________________________|")
  time.sleep(0.4)
  print("|               /                                                                                                                         |           |                                                                       |     |")
  time.sleep(0.4)
  print("|              /                                                                                                                          |           |                                  ___                                  |     |")
  time.sleep(0.4)
  print("|             /                                                                                                                           |           |                                 /   \                                 |     |")
  time.sleep(0.4)
  print("|            /                                                                                                                            |           |                                /     \                                |     |")
  time.sleep(0.4)
  print("|           /                                                                                                                             |           |                /\             /       \             /\                |     |")
  time.sleep(0.4)
  print("|          /                                                                                                                              |           |               /  \           /         \           /  \               |     |")
  time.sleep(0.4)
  print("|         /                                                                                                                               |           |              /    \         /           \         /    \              |     |")
  time.sleep(0.4)
  print("|        /                                                                                                                                |           |             /      \       /             \       /      \             |     |")
  time.sleep(0.4)
  print("|       /                                                                                                                                 |           |            /        \_____/               \_____/        \            |     |")
  time.sleep(0.4)
  print("|      /                                                                                    ________________                              |           |            |                                             |            |     |")
  time.sleep(0.4)
  print("|     /     /|\                                                                            (       /        )                             |           |            |                                             |            |     |")
  time.sleep(0.4)
  print("|    /       |                                                                            (        /         )                            |           |            |                                             |            |     |")
  time.sleep(0.4)
  print("|   /        |                                                                             (        \       )                             |           |            |       Corrupt Kingdom of Knowltrolls        |            |     |")
  time.sleep(0.4)
  print("|  /         |                                                                              (_______\______)                              |           |            |                                             |            |     |")
  time.sleep(0.4)
  print("|_/    Dungeon of the Lavapool                                                                                                            |           |            |                                             |            |     |")
  time.sleep(0.4)
  print("|                                                                                                  /|\                                    |           |            |                                             |            |     |")
  time.sleep(0.4)
  print("|                                                                                                   |                                     |           |            |_____________________________________________|            |     |")
  time.sleep(0.4)
  print("|                                                                                                   |                                     |           |                                                                       |     |")
  time.sleep(0.4)
  print("|                                                                                     Dungeon of the Lightning Cloud                      |           |                                                                       |     |")
  time.sleep(0.4)
  print("|                                                                                                                                         |           |_______________________________________________________________________|     |")
  time.sleep(0.4)
  print("|                                                                                                                                         |                                                                                         |")
  time.sleep(0.4)
  print("|                                                                                                                                         |                                                                                         |")
  time.sleep(0.4)
  print("|                                                                                                                                         |                                         Wall Of Maria                                   |")
  time.sleep(0.4)
  print("|                                                                                                                                         |                                                                                         |")
  time.sleep(0.4)
  print("|                                                                                                                                         |                                                                                         |")
  time.sleep(0.4)
  print("|                                                                                                                                         |_________________________________________________________________________________________|")
  time.sleep(0.4)
  print("|                                                                                                                                                                                                                                   |")
  time.sleep(0.4)
  print("|                                                                                                                                                                                                                                   |")
  time.sleep(0.4)
  print("|                                                                                                                                                                                 Wall Of St. Lewis                                 |")
  time.sleep(0.4)
  print("|                                                                                                                                                                                                                                   |")
  time.sleep(0.4)
  print("|                                                                                                                                                                                                                                   |")
  time.sleep(0.4)
  print("|                                                                                                                                                                                                                                   |")
  time.sleep(0.4)
  print("|    Dungeon of the  Watching Mountains                                                                                                                                                                                             |")
  time.sleep(0.4)
  print("|               |                                                                                                                                                                                                                   |")
  time.sleep(0.4)
  print("|               |                                                                                                                                                                                                                   |")
  time.sleep(0.4)
  print("|               |                             /\                                                                                                                                                         Dungeon of Bloodshed Lake  |")
  time.sleep(0.4)
  print("|               |                            /  \                                                                                                                                                                  |                |")
  time.sleep(0.4)
  print("|              \|/                          /    \                                                                                                                                                                 |                |")
  time.sleep(0.4)
  print("|                    /\                    /      \                                                                                                                                                                |                |")
  time.sleep(0.4)
  print("|                   /  \                  /        \                                                                                                                                                               |                |")
  time.sleep(0.4)
  print("|                  /    \                /   ( | )  \                                                                                                                                                              |                |")
  time.sleep(0.4)
  print("|               /\/      \              /            \                                                                                                                                                            \|/               |")
  time.sleep(0.4)
  print("|              /  \       \     /\     /              \                      Village of the Bloodmist                                                                                                            ____________-___-_-|")
  time.sleep(0.4)
  print("|             /    \  /\   \   /  \   /                \                              |                                                          Sister Village of the Bloodmist                                |                   |")
  time.sleep(0.4)
  print("|           /\      \/  \   \ /    \ /                  \                             |                                                                      |                                                 /                    |")
  time.sleep(0.4)
  print("|          /  \     /    \   /      /                    \                            |                                                                      |                                                |                     |")
  time.sleep(0.4)
  print("|         /    \   /      \ /      /                      \                           |                                                                      |                                             -_|                      |")
  time.sleep(0.4)
  print("|        /      \ /        \      /                        \                         \|/                                                                    \|/                                           /          (------)       |")
  time.sleep(0.4)
  print("|       /        \          \    /                          \                  ______    ______    ______                                                 ______                                         |          (----|----)     |")
  time.sleep(0.4)
  print("|      /          \          \  /                            \                /      \  /      \  /      \                                               /      \                                       /            (------)       |")
  time.sleep(0.4)
  print("|                             \/                                              |      |  |      |  |      |                                               |      |                                      |                            |")
  time.sleep(0.4)
  print("|                                                                             |      |  |      |  |      |                                               |      |                     -__----_____---__|                            |")
  time.sleep(0.4)
  print("|   -_--________-_---____-__--________------___--__-__-_                                                                                         _--------_----__-_-___----------___--                  \                           |")
  time.sleep(0.4)
  print("|                                                       __-_---__-----_-----__-_-_----                                    _--__-_--_---____---_--                                                        |                          |")
  time.sleep(0.4)
  print("|                                                                                     -___---__-----_-_-_--_---__-_-__---_                                                                                _                         |")
  time.sleep(0.4)
  print("|                                                                                                                                                                                            ____--__-_---  \                       |")
  time.sleep(0.4)
  print("|                                                   ____--___-_------                                                                                                                        _               \____                  |")
  time.sleep(0.4)
  print("|                                       __-_--_---__                 __-_-----___------____                                                                                             ____-                     \                 |")
  time.sleep(0.4)
  print("|   ___---_____-__--_--_--___--___----__                                                   _-__---_                              _---___                                         -__--_-                          \                 |")
  time.sleep(0.4)
  print("|                                                                                                  __-----_------__----_--__---_-       ___----                           __--_--                                  |________________|")
  time.sleep(0.4)
  print("|                                                                                                                                              ____---__-___--____--____-_                                                          |")
  time.sleep(0.4)
  print("|                                                                                                                                                                                                                                   |")
  time.sleep(0.4)
  print("|                                                                                                                                                                                                                                   |")
  time.sleep(0.4)
  print("| You are here, in the village of Dertan                                                                                                                                                                                            |")
  time.sleep(0.4)
  print("|            |                                                                                                                                                                                                                      |")
  time.sleep(0.4)
  print("|            |                                                                                                                                                                               Village of the Edge                    |")
  time.sleep(0.4)
  print("|            |                                                                                                                                                                                        |                             |")
  time.sleep(0.4)
  print("|           \|/                                                                                                                                                                                       |                             |")
  time.sleep(0.4)
  print("|                        ______    ______                                                                                                                                                            \|/                            |")
  time.sleep(0.4)
  print("|         ()  ()        /      \  /      \                                                                                                                                                         ______                           |")
  time.sleep(0.4)
  print("|         \/  \/        |      |  |      |                                                                                                                                                        /      \                          |")
  time.sleep(0.4)
  print("|         /\  /\        |      |  |      |                                                                                                                                                        |      |                          |")
  time.sleep(0.4)
  print(" _______________________|______|__|______|________________________________________________________________________________________________________________________________________________________|______|__________________________|")
def bloodmist():
  print("*This dungeon is the normal dungeon.* ")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("*You head out*")
  time.sleep(0.4)
  print("*On the way to the mountains you meet a merchant, where you can buy gear if you choose*")
  #enter shop function
  print("*Now that your geared up you now can begin your quest.*")
  time.sleep(0.4)
  print("*As you make your way to the Bloodmist Village, you meet a couple of thugs.*")
  time.sleep(0.4)
  print("*Let's beat them up.*")
  #enter fight functions
  time.sleep(0.4)
  print("*Gained 1500 gold*")
  money1=money1+1500
  money2=money2+1500
  print("*Nearly a week passes and you almost reach the gates of the Village of the Bloodmist.*")
  time.sleep(0.4)
  guards=input("*Guards stand in your way. Do you want to A.) Fight them and get through, or B.) Bribe them with 5,000 gold? *")
  if guards=="Fight" or "A":
    fightbm()
    enteringbm()
  if guards=="Bribe" or "B":
    bribes()
    enteringbm()
def enteringbm():
  print("You make it into the Bloodmist.")
  time.sleep(0.4)
  print("People are giving you weird stares...")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("2 men come up to you.")
  time.sleep(0.4)
  print("'Who are you people'")
  time.sleep(0.4)
  print("'We are just travelers, no need to mind us'")
  time.sleep(0.4)
  print("'Our village is private property, outsiders are not welcome.'")
  time.sleep(0.4)
  print("'Don't worry, we'll leave.'")
  time.sleep(0.4)
  print("'No you won't, you'll be staying with us...with your corpses.'")
  time.sleep(0.4)
  print("*Prepare to fight*")
  #enter fight functions
  print("'You may have beat us, but watch out. Mr.M is unbeatable.'")
  time.sleep(0.4)
  print("*You are intrigued.*")
  time.sleep(0.4)
  print("*You make your way around town and find a shop.*")
  #enter shop functions
  print("'Thanks for coming!'")
  
def bribes():    
    x=5000
    moneysub1()
    x=5000
    moneysub2()
def fightbm():
  print("hi")
  #enter fight functions
def dungeon_mountains():
  global bossh
  global wb
  global money1
  global money2
  global p1health
  global p2health
  print("*This dungeon is the easiest dungeon, right choice?*")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("...")
  print("*On the way to the mountains you meet a merchant, where you can buy gear if you choose*")
  #enter shop function
  print("*Now that your geared up you now can begin your quest.*")
  time.sleep(0.4)
  print("*You enter the dungeon and you are greeted by four archers.*")
  time.sleep(0.4)
  print("ALRIGHT, OUR FIRST FIGHT!!! WOOOOOOOO!!!!")
  time.sleep(0.4)
  print("LET'S GOOOOOOO")
  print(p2_name)
  print("*They start firing at you.*")
  wboss=1
  bossh=50
  if subclass1=="Healer":
      wboss=1
      fightmechanicsmage1()
  else:
    fightmechanics1()
def archerafter():
  global money1
  global money2
  global bossh
  global wboss
  time.sleep(0.4)
  print("Nice job! Behind the archers you see a silver chest. Inside the chest you each get 10000 gold.")
  money1=money1+10000
  print(money1)
  money2=money2+10000
  print(money2)
  time.sleep(0.4)
  print("Let's keep going.")
  time.sleep(0.4)
  print("*Mysterious mountain men appear...*")
  bossh=100
  wboss=2
  if subclass1=="Healer":
      fightmechanicsmage1()
  else:
    fightmechanics1()
def afterfight2 ():
  global p1health
  global p2health
  global bossh
  global wboss
  time.sleep(0.4)
  print("'Who are you people and why are you here?'")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("'We are a group of people who have adapted to this region.")
  time.sleep(0.4)
  print("'We want to live, please don't hurt us.'")
  time.sleep(0.4)
  print("We'll give you some gear if you want, just spare our lives.'")
  time.sleep(0.4)
  print("'Well, alright! Sure.'")
  p1health=p1health+50
  print(p1health)
  p2health=p2health+50
  print(p2health)
  print("*You both just recieved 50 health.*")
  time.sleep(0.4)
  print("'By the way, do you happen to know the fastest route through these mountains?'")
  time.sleep(0.4)
  print("'I'm trying to get to the Capital right away.'")
  time.sleep(0.4)
  print("'Sure, however the fastest way through the peak. Are you sure you are ready?'")
  time.sleep(0.4)
  print("'Hell yeah I'm ready! Let's go!!!'")
  time.sleep(0.4)
  print("'Alright, then.'")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("...")
  time.sleep(0.4)
  print("*You are climbing on the highest peak*")
  time.sleep(0.4)
  print("*Wild, ferocious beasts appear before your eyes.*")
  time.sleep(0.4)
  print("*They seem to be protecting something.*")
  time.sleep(0.4)
  print("*Prepare to fight.*")
  wboss=3
  boss=250
  if subclass1=="Healer":
    wboss=3
    boss=250
    fightmechanicsmage1()
  else:
    boss=3
    boss=250
    fightmechanics1()
def almosts(): 
  global money1
  global money2
  global bossh
  global wboss
  print("*Gained 1000 gold.*")
  money1=money1+1000
  print(money1)
  money2=money2+1000
  print(money2)
  print("'*You have reached the top*")
  wboss=4
  bossh=500
  adstart()
startgame() 
