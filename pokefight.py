from time import sleep
import random


#collect the important pokemon info
def PokemonInfo(pokemon):
  return "{} | LVL {} | Health {}/{} | Type {}".format(pokemon["name"], 
                                             pokemon["level"], 
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
  return "{} | type: {} | damage: {} ".format(pokemon["name"],
                                              pokemon["type"],
                                              pokemon["damage"])


#collect the full life of the pokemons you have
def PlayerPokemonLive(PlayerProfile):
  return sum([pokemon["CurrentHealth"] for pokemon in PlayerProfile["PokemonInventory"]])


#let the user choose the pokemon that is going to usea
def ChoosePokemon(PlayerProfile):

  chosen = None
  while not chosen:
    print("you have the next Pokemons:\n")
    #loop in the length of the pokemon inventory
    for index in range(len(PlayerProfile["PokemonInventory"])):
      print("{}. {}".format(index, PokemonInfo(PlayerProfile["PokemonInventory"][index])))
    try: #try to collect the pokemon that the user choose
      return PlayerProfile["PokemonInventory"][int(input("cual eliges? "))]
    except (ValueError, IndexError):
      print("unvalid option")


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
def PlayerTurn(PlayerPokemon, EnemyPokemon, PlayerProfile, AttackHistory, EnemyAttack):

    #cuando se elije el ataque del usuario solo se muestran ataques disponibles por nivel
    
  
  attack = None
  while not attack:
    print("------------------------")
    print("you have the next attacks:\n")
    #loop in every attack of the pokemon the user choose
    for index in range(len(PlayerPokemon["attacks"])):
      print("{}. {}".format(index, PokemonAttacks(PlayerPokemon["attacks"][index])))

    try:
      attack = PlayerPokemon["attacks"][int(input("con cual deseas atacar? "))]
      print(attack)
    except (ValueError, IndexError):
      print("unvalid attack option!")
      
  Div = TypeDividers
  Mult = TypeMultipliers
  BaseDamage = attack["damage"]
  multiplier = ChangeDamage(attack, EnemyPokemon, Div, Mult, BaseDamage)
  #print(multiplier)
  EnemyPokemon["CurrentHealth"] -= multiplier
  attack["damage"] = BaseDamage

  print("-----------------------------")
  print("The Enemy Health is {}/{}".format(EnemyPokemon["CurrentHealth"],
                                           EnemyPokemon["BaseHealth"]))
  print("-----------------------------")
  AttackHistory.append(PlayerPokemon)
    #check if the enemy current health is non 0
  if EnemyPokemon["CurrentHealth"] <= 0:
    PlayerProfile["combats"] += 1
    print("\n------------------------")
    print("You Win this fight!")
    print("------------------------")
    Experience(AttackHistory)
  return attack

#the loop for the attack of the enemy
def EnemyTurn(EnemyPokemon, PlayerPokemon, PlayerProfile, EnemyAttack, PlayerAttack):
  sleep(1)
  SelectAttack = EnemyAttack
  print("\n{} attack with {} and do {} of damage".format(EnemyPokemon["name"],
                                                   SelectAttack["name"],
                                                   SelectAttack["damage"]))
  print(EnemyAttack)
  Div = TypeDividers
  Mult = TypeMultipliers
  BaseDamage = EnemyAttack["damage"]
  multiplier = ChangeDamage(EnemyAttack, PlayerPokemon, Div, Mult,BaseDamage)
  EnemyPokemon["CurrentHealth"] -= multiplier
  EnemyAttack["damage"] = BaseDamage
  
  PlayerPokemon["CurrentHealth"] -= SelectAttack["damage"]

  print("-------------------------------")
  print("your current health is {}/{}".format(PlayerPokemon["CurrentHealth"],
                                              PlayerPokemon["BaseHealth"]))
  if PlayerPokemon["CurrentHealth"] <= 0: 
      #check if at least 1 player pokemon is alive
      if PlayerPokemonLive(PlayerProfile) <= 0:
        print("\n------------------------")
        print("---- GAME OVER!? ----")
        print("------------------------")
        return PlayerPokemonLive(PlayerProfile)
      else:
        sleep(1)
        print("\n-----------------------------------------------")
        print("your pokemon died, choose another one to fight...")
        print("-----------------------------------------------")
  input("press any key to continue...")


#leveling up the pokemons
def Experience(AttackHistory):
  for pokemon in AttackHistory:
    points = random.randint(1,5)
    pokemon["CurrentExp"] += points

    while pokemon["CurrentExp"] > 20:
      pokemon["CurrentExp"] == 20
      pokemon["CurrentExp"] -= 20
      pokemon["level"] += 1
      pokemon["CurrentHealth"] = pokemon["BaseHealth"]
      print("your pokemon has leveled up {}".format(PokemonInfo(pokemon)))

#principal loop of the fight
def fight(PlayerProfile, EnemyPokemon):


  print("---- NEW FIGHT ----\n")

  print("--------------------------------")
  print("tu adversario sera: {}".format(PokemonInfo(EnemyPokemon)))
  print("--------------------------------")
  PlayerPokemon = ChoosePokemon(PlayerProfile)
  AttackHistory = []

  print("\nopponents: {} vs {}\n".format(PokemonInfo(PlayerPokemon), 
                                         PokemonInfo(EnemyPokemon)))
  while PlayerPokemonLive(PlayerProfile) > 0 and EnemyPokemon["CurrentHealth"] > 0:
    action = None
    #check what the user want to do
    while action not in ["a", "P", "H", "C"]:
      action = input("what you want to do: [A]Attack, [P]Pokeball, [H]Health potion, [C]Change\n").lower()
    if action == "a":
      EnemyAttack = random.choice(EnemyPokemon["attacks"])
      PlayerAttack = PlayerTurn(PlayerPokemon, EnemyPokemon, PlayerProfile, AttackHistory, EnemyAttack)
      if EnemyPokemon["CurrentHealth"] > 0:
        EnemyTurn(EnemyPokemon, PlayerPokemon, PlayerProfile, EnemyAttack, PlayerAttack)
      else:
        pass

      #check if the player pokemon is alive
    elif action == "h":
      #TODO si hay curas, se aplica, cura 50 de vida hasta llegar a 100, si no tiene no se cura
      CurePokemon(PlayerPokemon, PlayerProfile)
      EnemyTurn(EnemyPokemon, PlayerPokemon, PlayerProfile, EnemyAttack)
    elif action == "p":
      #TODO SI TIENE POKEBALLS PROBABILIDAD DEL USUARIO SI MENOS SALUD MAS PROBABLE
      CapturePokemon(EnemyPokemon,PlayerProfile)
    elif action == "c":
      PlayerPokemon = ChoosePokemon(PlayerProfile)
      

      #remove the dead pokemon and select new one
      PlayerProfile["PokemonInventory"].remove(PlayerPokemon)
      PlayerPokemon = ChoosePokemon(PlayerProfile)



  print("---- END OF THE FIGHT ----")
  input("press ENTER to continue...")


#fight(PlayerProfile, EnemyPokemon)