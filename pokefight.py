from time import sleep
import random


#collect the important pokemon info
def PokemonInfo(pokemon):
  return "{} | Health {}/{} | Type {}".format(pokemon["name"],  
                                             pokemon["CurrentHealth"], 
                                             pokemon["BaseHealth"],
                                             pokemon["type"])


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
  sleep(1)
  chosen = None
  #meanwhile the user not choose a pokemon it will repeat the question
  while not chosen:
    print("\nyou have the next Pokemons:\n")
    #loop in the length of the pokemon inventory
    for index in range(len(PlayerProfile["PokemonInventory"])):
      print("{}. {}".format(index, PokemonInfo(PlayerProfile["PokemonInventory"][index])))
    try: #try to collect the pokemon that the user choose
      return PlayerProfile["PokemonInventory"][int(input("cual eliges? "))]
    except (ValueError, IndexError):
      print("unvalid option")


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
  print("-----------------------------")
  print("The Enemy Health is {}/{}".format(EnemyPokemon["CurrentHealth"],
                                           EnemyPokemon["BaseHealth"]))
  print("-----------------------------")
  AttackHistory.append(PlayerPokemon)
    #check if the enemy current health is non 0
  if EnemyPokemon["CurrentHealth"] <= 0:
    PlayerProfile["combats"] += 1
    sleep(0.1)
    print("\n------------------------")
    print("You Win this fight!")
    print("------------------------")
    Experience(AttackHistory, EnemyPokemon)
  return attack


#the loop for the attack of the enemy
def EnemyTurn(EnemyPokemon, PlayerPokemon, PlayerProfile, EnemyAttack):
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
  print("-------------------------------")
  print("your current health is {}/{}".format(PlayerPokemon["CurrentHealth"],
                                              PlayerPokemon["BaseHealth"]))
  #check if the player pokemon are alive
  if PlayerPokemon["CurrentHealth"] <= 0: 
      sleep(1)
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
        #remove the dead pokemon and select new one
        PlayerProfile["PokemonInventory"].remove(PlayerPokemon)
  input("press any key to continue...")


#cure the pokemon
def CurePokemon(PlayerPokemon, PlayerProfile):
  if PlayerProfile["HealthPotion"] > 0:
    PlayerPokemon["CurrentHealth"] += 50
    print("\n----------------------------------------------")
    print("you heal 50 to {}".format(PlayerPokemon["name"]))
    
    if PlayerPokemon["CurrentHealth"] > PlayerPokemon["BaseHealth"]:
      PlayerPokemon["CurrentHealth"] = PlayerPokemon["BaseHealth"]
      
    print("his actual life is {}/{}".format(PlayerPokemon["CurrentHealth"], PlayerPokemon["BaseHealth"]))
    PlayerProfile["HealthPotion"] -= 1
    print("---------------------------")
    print("Current Health Potions: {}".format(PlayerProfile["HealthPotion"]))
    print("----------------------------------------------")
  else:
    print("-----------------------------------")
    print("you dont have any Health Potion!!!")
    print("-----------------------------------")
  
  
def CapturePokemon(EnemyPokemon,PlayerProfile):
  pass

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
      print("your pokemon has leveled up {}".format(PokemonInfo(pokemon)))
      print("the live of {} has increase in 10: Current live: {}/{}".format(pokemon["name"], 
                                                                            pokemon["CurrentHealth"],
                                                                            pokemon["BaseHealth"]))

#principal loop of the fight
def fight(PlayerProfile, EnemyPokemon):
  sleep(1)
  print("---- NEW FIGHT ----\n")
  print("--------------------------------")
  print("tu adversario sera: {}".format(PokemonInfo(EnemyPokemon)))
  print("--------------------------------")
  PlayerPokemon = ChoosePokemon(PlayerProfile)
  AttackHistory = []
  #multiply enemy pokemon level base on my level
  if PlayerPokemon["level"] >= EnemyPokemon["level"]:
    EnemyPokemon["level"] *= 2

  print("\nopponents: {} vs {}\n".format(PokemonInfo(PlayerPokemon), 
                                         PokemonInfo(EnemyPokemon)))
  #meanwhile the Player pokemons are alive and the enemy is not dead it will the fight loop
  while PlayerPokemonLive(PlayerProfile) > 0 and EnemyPokemon["CurrentHealth"] > 0:
    sleep(1)
    action = None
    #check what the user want to do
    while action not in ["a", "p", "h", "c"]:
      action = input("what you want to do: [A]Attack, [P]Pokeball, [H]Health potion, [C]Change\n").lower()
    if action == "a":
      
      #random choose the enemy attack by level
      for index in range(len(EnemyPokemon["attacks"])):
        EnemyAttack = EnemyPokemon["attacks"]
        if EnemyPokemon["level"] >= int(EnemyAttack[index]["MinLevel"]):
          EnemyAttack = random.choice(EnemyPokemon["attacks"])
          break
          
      PlayerTurn(PlayerPokemon, EnemyPokemon, PlayerProfile, AttackHistory)
      #check if the enemy health is more than 0
      if EnemyPokemon["CurrentHealth"] > 0:
        EnemyTurn(EnemyPokemon, PlayerPokemon, PlayerProfile, EnemyAttack)
        #check if there are at least one pokemon alive
        if PlayerPokemonLive(PlayerProfile) > 0 and PlayerPokemon["CurrentHealth"] <= 0:
          PlayerPokemon = ChoosePokemon(PlayerProfile)
      
      #check if the player pokemon is alive
    elif action == "h":
      CurePokemon(PlayerPokemon, PlayerProfile)
      EnemyTurn(EnemyPokemon, PlayerPokemon, PlayerProfile, EnemyAttack)
    elif action == "p":
      #TODO SI TIENE POKEBALLS PROBABILIDAD DEL USUARIO SI MENOS SALUD MAS PROBABLE
      CapturePokemon(EnemyPokemon,PlayerProfile)
    elif action == "c":
      PlayerPokemon = ChoosePokemon(PlayerProfile)

  print("---- END OF THE FIGHT ----")
  input("press ENTER to continue...")


#fight(PlayerProfile, EnemyPokemon)