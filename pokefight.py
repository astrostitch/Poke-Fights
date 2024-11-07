from time import sleep
import random


#collect the important pokemon info
def PokemonInfo(pokemon):
  return "{} | Health {}/{} | Type {} | level: {}".format(pokemon["name"],  
                                             pokemon["CurrentHealth"], 
                                             pokemon["BaseHealth"],
                                             pokemon["type"],
                                             pokemon["level"])


#show the player inventory
def PokemonInventory(PlayerProfile):

  #go through the pokemon inventory
  for index in range(len(PlayerProfile["PokemonInventory"])):
    sleep(0.1)
    pokemon = PlayerProfile["PokemonInventory"]
    print("\n{}. Name: {} | Health: {}/{} | Type: {} | Level: {} | CurrentEXP: {}\n".format(index, 
                                                                                          pokemon[index]["name"], 
                                                                                          pokemon[index]["CurrentHealth"],
                                                                                          pokemon[index]["BaseHealth"],
                                                                                          pokemon[index]["type"],
                                                                                          pokemon[index]["level"],
                                                                                          pokemon[index]["CurrentExp"]))
    #go through the attacks in the pokemon
    for attacks in range(len(pokemon[index]["attacks"])):
      attack = pokemon[index]["attacks"]
      SubIndex = index
      sleep(0.25)
      print(" {}.{}. Name: {} // Type: {} // Min level: {} // Damage: {}".format(attacks, SubIndex,
                                                                               attack[attacks]["name"],
                                                                               attack[attacks]["type"],
                                                                               attack[attacks]["MinLevel"],
                                                                               attack[attacks]["damage"]))
    
    
#print the info of the player, name, level, inventory, combats, pokeballs, Health Potions
def InfoPlayer(PlayerProfile):
  sleep(0.1)
  print("what do you want to see?")
  Info = input("[I]Inventory, [U]utility\n").lower()
  if Info == "i":
    PokemonInventory(PlayerProfile)
  if Info == "u":
    sleep(0.1)
    print("----------------------")
    print("Pokeballs: {}\nHealth Potions: {}".format(PlayerProfile["pokeballs"],
                                                     PlayerProfile["HealthPotion"]))
    print("----------------------")
  

#library of weakness for each type
TypeDividers = {
  "normal": ["lucha"],
  "fuego": ["agua", "tierra", "roca"],
  "agua": ["planta", "eléctrico"],
  "planta": ["fuego", "hielo", "veneno", "volador", "bicho"],
  "eléctrico": ["tierra"],
  "hielo": ["fuego", "lucha", "roca", "acero"],
  "lucha": ["volador", "psíquico", "hada"],
  "veneno": ["tierra", "psíquico"],
  "tierra": ["agua", "planta", "hielo"],
  "volador": ["eléctrico", "hielo", "roca"],
  "psíquico": ["bicho", "fantasma", "siniestro"],
  "bicho": ["fuego", "volador", "roca"],
  "roca": ["agua", "planta", "lucha", "tierra", "acero"],
  "fantasma": ["fantasma", "siniestro"],
  "dragón": ["hielo", "dragón", "hada"],
  "siniestro": ["lucha", "bicho", "hada"],
  "acero": ["fuego", "lucha", "tierra"],
  "hada": ["veneno", "acero"]
}
    
    
#library of strengths for each type
TypeMultipliers = {
  "normal": [],
  "fuego": ["planta", "hielo", "bicho", "acero"],
  "agua": ["fuego", "tierra", "roca"],
  "planta": ["agua", "tierra", "roca"],
  "eléctrico": ["agua", "volador"],
  "hielo": ["planta", "tierra", "volador", "dragón"],
  "lucha": ["normal", "hielo", "roca", "siniestro", "acero"],
  "veneno": ["planta", "hada"],
  "tierra": ["fuego", "eléctrico", "veneno", "roca", "acero"],
  "volador": ["planta", "lucha", "bicho"],
  "psíquico": ["lucha", "veneno"],
  "bicho": ["planta", "psíquico", "siniestro"],
  "roca": ["fuego", "hielo", "volador", "bicho"],
  "fantasma": ["psíquico", "fantasma"],
  "dragón": ["dragón"],
  "siniestro": ["psíquico", "fantasma"],
  "acero": ["hielo", "roca", "hada"],
  "hada": ["lucha", "dragón", "siniestro"]
}


#collect the important info of the pokemon attacks
def PokemonAttacks(pokemon):
  return "{} | type: {} | damage: {} | level: {}".format(pokemon["name"],
                                              pokemon["type"],
                                              pokemon["damage"],
                                              pokemon["MinLevel"])


#collect the full life of the pokemons you have
def PlayerPokemonLive(PlayerProfile):
  return sum([pokemon["CurrentHealth"] for pokemon in PlayerProfile["PokemonInventory"]])


#let the user choose the pokemon that is going to usea
def ChoosePokemon(PlayerProfile):
  sleep(0.25)
  chosen = None
  #meanwhile the user not choose a pokemon it will repeat the question
  while not chosen:
    print("you have the next Pokemons:\n")
    #loop in the length of the pokemon inventory
    for index in range(len(PlayerProfile["PokemonInventory"])):
      sleep(0.1)
      print("{}. {}".format(index, PokemonInfo(PlayerProfile["PokemonInventory"][index])))
    try: #try to collect the pokemon that the user choose
      sleep(0.1)
      return PlayerProfile["PokemonInventory"][int(input("Your Choose: "))]
    except (ValueError, IndexError):
      print("\nunvalid option\n")


#Multiply or divide the damage by the strengths or weaknesses of the pokemons
def ChangeDamage(attack, EnemyPokemon, Div, Mult, BaseDamage):
  
  if EnemyPokemon["type"] in Div.get(attack["type"], []):
    attack["damage"] /= 1.25
    print("The attack has receive a 1.25 penalty for pokemon resistances")
    print("Base damage: {} | Current damage: {}".format(BaseDamage, attack["damage"]))
    sleep(1)
    return attack["damage"]
  
  elif EnemyPokemon["type"] in Mult.get(attack["type"], []):
    attack["damage"] *= 1.25
    print("The attack has receive a 1.25 multiply for pokemon resistances")
    print("Base damage: {} | Current damage: {}".format(BaseDamage, attack["damage"]))
    sleep(1)
    return attack["damage"]
  
  return attack["damage"]

   
#the loop for the attack of the player
def PlayerTurn(PlayerPokemon, EnemyPokemon, PlayerProfile, AttackHistory):
    
  attack = None
  #meanwhile there are not attacks choosen it will repeat
  while not attack:
    print("------------------------")
    print("you have the next attacks:\n")
    #loop in every attack of the pokemon the user choose
    for index in range(len(PlayerPokemon["attacks"])):
      attacks = PlayerPokemon["attacks"]
      if attacks[index]["MinLevel"] == "":
        attacks[index]["MinLevel"] = "1"
      elif PlayerPokemon["level"] < int(attacks[index]["MinLevel"]):
        pass
      elif PlayerPokemon["level"] >= int(attacks[index]["MinLevel"]):
        sleep(0.5)
        print("{}. {}".format(index, PokemonAttacks(PlayerPokemon["attacks"][index])))
        
    #try to let the user choose the attack that it want to use
    try:
      attack = PlayerPokemon["attacks"][int(input("con cual deseas atacar? "))]
    except (ValueError, IndexError):
      print("unvalid attack option!")
  #apply the multipliers or dividers for the attack
  Div = TypeDividers
  Mult = TypeMultipliers
  BaseDamage = attack["damage"]
  multiplier = ChangeDamage(attack, EnemyPokemon, Div, Mult, BaseDamage)
  EnemyPokemon["CurrentHealth"] -= multiplier
  attack["damage"] = BaseDamage
  sleep(0.25)
  print("-----------------------------")\
  #check if the enemy current health is non 0
  if EnemyPokemon["CurrentHealth"] > 0:
    print("The Enemy Health is {}/{}".format(EnemyPokemon["CurrentHealth"],
                                             EnemyPokemon["BaseHealth"]))
    print("-----------------------------")
    AttackHistory.append(PlayerPokemon)
  else:
    EnemyPokemon["CurrentHealth"] = 0
    print("The Enemy Health is {}/{}".format(EnemyPokemon["CurrentHealth"],
                                             EnemyPokemon["BaseHealth"]))
    print("-----------------------------")
    AttackHistory.append(PlayerPokemon)
    PlayerProfile["combats"] += 1
    sleep(0.1)
    print("\n------------------------")
    print("You Win this fight!")
    print("------------------------")
    Experience(AttackHistory, EnemyPokemon)
  return attack


#the loop for the attack of the enemy
def EnemyTurn(EnemyPokemon, PlayerPokemon, PlayerProfile, EnemyAttack, EnemyAttackHistory):
  sleep(0.5)
  SelectAttack = EnemyAttack
  print("\n{} attack with {} and do {} of damage".format(EnemyPokemon["name"],
                                                   SelectAttack["name"],
                                                   SelectAttack["damage"]))
  #set the multiplier or divider of the attacks
  Div = TypeDividers
  Mult = TypeMultipliers
  BaseDamage = EnemyAttack["damage"]
  multiplier = ChangeDamage(EnemyAttack, PlayerPokemon, Div, Mult,BaseDamage)
  PlayerPokemon["CurrentHealth"] -= multiplier
  EnemyAttack["damage"] = BaseDamage
  sleep(0.25)
  if PlayerPokemon["CurrentHealth"] > 0: 
    print("-------------------------------")
    print("your current health is {}/{}".format(PlayerPokemon["CurrentHealth"],
                                                PlayerPokemon["BaseHealth"]))
  #check if the player pokemon are alive
  else:
    PlayerPokemon["CurrentHealth"] = 0
    print("-------------------------------")
    print("your current health is {}/{}".format(PlayerPokemon["CurrentHealth"],
                                              PlayerPokemon["BaseHealth"]))
    sleep(0.75)
    #check if at least 1 player pokemon is alive
    if PlayerPokemonLive(PlayerProfile) <= 0:
      print("\n------------------------")
      print("---- GAME OVER!? ----")
      print("------------------------")
      return PlayerPokemonLive(PlayerProfile)
    else:
      sleep(0.75)
      print("\n-----------------------------------------------")
      print("your pokemon died, choose another one to fight...")
      print("-----------------------------------------------")
      Experience(EnemyAttackHistory, PlayerPokemon)
      #remove the dead pokemon and select new one
      try:
        PlayerProfile["PokemonInventory"].remove(PlayerPokemon)
      except Exception:
        print("that pokemon is dead already...maybe a bug...better continue...nothing happen here")
  input("press any key to continue...")


#multiply enemy pokemon level base on my level
def MultiplyEnemyLevel(PlayerPokemon, EnemyPokemon):
  if PlayerPokemon["level"] >= EnemyPokemon["level"]:
    EnemyPokemon["level"] = random.randint(PlayerPokemon["level"] - 1,PlayerPokemon["level"] + 4)
  if EnemyPokemon["level"] == 0:
    EnemyPokemon["level"] = 1
  elif EnemyPokemon["level"] > 1:
    EnemyPokemon["BaseHealth"] += (EnemyPokemon["level"] * 10)
    EnemyPokemon["CurrentHealth"] = EnemyPokemon["BaseHealth"]
    
    
#cure the pokemon
def CurePokemon(PlayerPokemon, PlayerProfile):
  if PlayerProfile["HealthPotion"] > 0:
    PlayerPokemon["CurrentHealth"] += 50
    print("\n----------------------------------------------")
    print("you heal 50 to {}".format(PlayerPokemon["name"]))
    #stablish the maximum health recovery
    if PlayerPokemon["CurrentHealth"] > PlayerPokemon["BaseHealth"]:
      PlayerPokemon["CurrentHealth"] = PlayerPokemon["BaseHealth"]
    #print the currrent and base Health
    print("his actual life is {}/{}".format(PlayerPokemon["CurrentHealth"], PlayerPokemon["BaseHealth"]))
    PlayerProfile["HealthPotion"] -= 1
    print("---------------------------")
    print("Current Health Potions: {}".format(PlayerProfile["HealthPotion"]))
    print("----------------------------------------------")
  else:
    print("-----------------------------------")
    print("you dont have any Health Potion!!!")
    print("-----------------------------------")
  
  
#Capture the pokemon by a Chance
def CapturePokemon(EnemyPokemon,PlayerProfile,PlayerPokemon,FinishCombat):
  sleep(0.5)
  CaptureChance = random.randint(5,15)
  WinChance = random.randint(1, 100)
  #change the chance of capturing it by the level of the pokemons
  if EnemyPokemon["level"] > PlayerPokemon["level"]:
    CaptureChance = random.randint(3, 12)
    WinChance = random.randint(25, 100)
  elif EnemyPokemon["level"] < PlayerPokemon["level"]: 
    CaptureChance = random.randint(7, 18)
    WinChance = random.randint(1, 75)
  PlayerProfile["pokeballs"] -= 1
  #change the chance by the health, less health increase the chance
  if EnemyPokemon["CurrentHealth"] < EnemyPokemon["BaseHealth"]:
    CaptureChance += (EnemyPokemon["BaseHealth"] - EnemyPokemon["CurrentHealth"])
  #apply the probability
  if WinChance < CaptureChance:
    sleep(0.5)
    print("\nyou captured {}!!!".format(PokemonInfo(EnemyPokemon)))
    PlayerProfile["PokemonInventory"].append(EnemyPokemon)
    FinishCombat = True
  else:
    sleep(0.5)
    print("\nYou did not capture {}".format(PokemonInfo(EnemyPokemon)))


#leveling up the pokemons
def Experience(AttackHistory, EnemyPokemon):
  for pokemon in AttackHistory:
    #random points by level of the pokemons
    if pokemon["level"] < EnemyPokemon["level"]:
      LowPointPerPFight = 3
      HighPointPerFigth = 7
    elif pokemon["level"] > EnemyPokemon["level"]:
      LowPointPerPFight = 1
      HighPointPerFigth = 3
    else:
      LowPointPerPFight = 1
      HighPointPerFigth = 5
    point = random.randint(LowPointPerPFight,HighPointPerFigth)
    NecessaryPoints = 20
    pokemon["CurrentExp"] += point   
    while pokemon["CurrentExp"] > NecessaryPoints:
      pokemon["CurrentExp"] == NecessaryPoints
      pokemon["CurrentExp"] -= NecessaryPoints
      pokemon["level"] += 1
      NecessaryPoints += 5
      #increase the live of the pokemons 
      pokemon["BaseHealth"] += 10
      pokemon["CurrentHealth"] += 10
      print("---------------------------------------------------------")
      print("{} has leveled up {}".format(EnemyPokemon, PokemonInfo(pokemon)))
      print("the live of {} has increase in 10: Current live: {}/{}".format(pokemon["name"], 
                                                                            pokemon["CurrentHealth"],
                                                                            pokemon["BaseHealth"]))

#principal loop of the fight
def fight(PlayerProfile, EnemyPokemon):
  sleep(0.4)
  print("---- NEW FIGHT ----\n")
  #escoger el pokemon para combatir
  PlayerPokemon = ChoosePokemon(PlayerProfile)
  AttackHistory = []
  EnemyAttackHistory = []
  FinishCombat = False
  
  #multiply enemy pokemon level base on my level
  MultiplyEnemyLevel(PlayerPokemon, EnemyPokemon)
    
  print("--------------------------------")
  print("tu adversario sera: {}".format(PokemonInfo(EnemyPokemon)))
  print("--------------------------------")

  sleep(0.25)
  print("\nopponents: {} vs {}\n".format(PokemonInfo(PlayerPokemon), 
                                         PokemonInfo(EnemyPokemon)))
  #meanwhile the Player pokemons are alive and the enemy is not dead it will the fight loop
  while PlayerPokemonLive(PlayerProfile) > 0 and EnemyPokemon["CurrentHealth"] > 0 or FinishCombat == True:
    sleep(0.2)
    action = None
    EnemyAttacks = EnemyPokemon["attacks"]
    #check what the user want to do
    while action not in ["a", "p", "h", "c", "x"]:
      action = input("\nwhat you want to do: [A]Attack, [P]Pokeball, [H]Health potion, [C]Change, [X]Profile\n").lower()
    if action == "a":
      EnemyAttack = None
      #random choose the enemy attack by level
      for index in range(len(EnemyPokemon["attacks"])):
        if EnemyPokemon["level"] >= int(EnemyAttacks[index]["MinLevel"]):
          EnemyAttack = random.choice(EnemyPokemon["attacks"])
          break
       
      PlayerTurn(PlayerPokemon, EnemyPokemon, PlayerProfile, AttackHistory)
      #check if the enemy health is more than 0
      if EnemyPokemon["CurrentHealth"] > 0:
        EnemyTurn(EnemyPokemon, PlayerPokemon, PlayerProfile, EnemyAttack, EnemyAttackHistory)
        #check if there are at least one pokemon alive
        if PlayerPokemonLive(PlayerProfile) > 0 and PlayerPokemon["CurrentHealth"] <= 0:
          PlayerPokemon = ChoosePokemon(PlayerProfile)
      
      #check if the player pokemon is alive
    elif action == "h":
      CurePokemon(PlayerPokemon, PlayerProfile)
      EnemyTurn(EnemyPokemon, PlayerPokemon, PlayerProfile, EnemyAttack, EnemyAttackHistory)
    elif action == "p":
      CapturePokemon(EnemyPokemon,PlayerProfile,PlayerPokemon, FinishCombat)
    elif action == "c":
      PlayerPokemon = ChoosePokemon(PlayerProfile)
    elif action == "x":
      InfoPlayer(PlayerProfile)

  print("---- END OF THE FIGHT ----")
  input("press ENTER to continue...")