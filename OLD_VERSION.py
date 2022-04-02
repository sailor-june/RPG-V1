import random

hero_hp = 100
 
badguy = ["rat",
"j.k. rowling",
"goblin",
"mean cat",
"hobogoblin",
"Derek",
"centaur",
"stump",
"",
"missingno."]


name = input("What is thy name, o wand'rer? ")
if name == "":
  name = input("Speak up! What is thy name? ")

badguy[9] = input("And who is thy greatest foe? ")
if badguy[9] == "":
  badguy[9] = input("Speak up! who is thy greatest foe? ")


def get_init():
    print('what will you do, ', name,  """?
    (1)attack, or (2)surrender """)
    initiative = input(int())
    return initiative


def combat():
  global hero_hp
  global name
  bad_id = random.randint(0, len(badguy)-1)
  bad_name = badguy[bad_id]
  bad_hp = bad_id * 6
  
  
  print("""
  A wild """, bad_name, " appears!")
  print("""
  your hp: """, hero_hp)
  print("enemy hp: ", bad_hp)
  
  initiative = get_init()
  if initiative == 0:
    get_init()
  elif initiative == 1:
    print(name, " swings wildly!")
    print(bad_name, " lunges toward you!")
    get_badhit = (bad_id * random.randint(1,6))
    get_herohit = (5* random.randint(1,6))
    bad_hp = bad_hp - get_herohit
    hero_hp = hero_hp - get_badhit
    if get_herohit >= 25:
      print(" a critical hit!")
    print (name, " did ", get_herohit, " damage!")
    get_init()
     
    print (bad_name, " did", get_badhit," damage!")
  elif initiative == 2:
      
      print('A shameful display!')
      print(bad_name, " swings with all their might!")
      print (bad_name, " hits for critical damage")
      hero_hp = 0
      print("your hp: 0")
      print("enemy hp: ", bad_hp)
  get_init()
    

 
      
  if hero_hp <= 0:
    print("You have been defeated, slain by a ", bad_name, ". F in the chat.")
  

  if hero_hp <= 0 and bad_hp<=0:
    print("As you fall to the ground bleeding, your only comfort is the sight of the dreaded ", bad_name, "Lying slain before you. Rest in peace, oh noble one.")


  if hero_hp > 0 and bad_hp <= 0:
    print("Victory is yours! The ", bad_name, "has been defeated!") 
 
combat()
