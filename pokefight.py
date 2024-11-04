from time import sleep
import random


#collect the important pokemon info
def PokemonInfo(pokemon):
  return "{} | LVL {} | Health {}/{}".format(pokemon["name"], 
                                             pokemon["level"], 
                                             pokemon["CurrentHealth"], 
                                             pokemon["BaseHealth"])


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


#the loop for the attack of the player
def PlayerAttack(PlayerPokemon, EnemyPokemon, PlayerProfile, AttackHistory):
  attack = None
  while not attack:
    print("------------------------")
    print("you have the next attacks:\n")
    #loop in every attack of the pokemon the user choose
    for index in range(len(PlayerPokemon["attacks"])):
      print("{}. {}".format(index, PokemonAttacks(PlayerPokemon["attacks"][index])))

    try:
      attack = PlayerPokemon["attacks"][int(input("con cual deseas atacar? "))]
    except (ValueError, IndexError):
      print("unvalid attack option!")
  EnemyPokemon["CurrentHealth"] -= attack["damage"]
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


#the loop for the attack of the enemy
def EnemyAttack(EnemyPokemon, PlayerPokemon, PlayerProfile):
  sleep(1)
  SelectAttack = random.choice(EnemyPokemon["attacks"])
  print("\n{} attack with {} and do {} of damage".format(EnemyPokemon["name"],
                                                   SelectAttack["name"],
                                                   SelectAttack["damage"]))
  
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

  PlayerPokemon = ChoosePokemon(PlayerProfile)
  AttackHistory = []

  print("\nopponents: {} vs {}\n".format(PokemonInfo(PlayerPokemon), 
                                         PokemonInfo(EnemyPokemon)))
  while PlayerPokemonLive(PlayerProfile) > 0 and EnemyPokemon["CurrentHealth"] > 0:
    action = None
    #check what the user want to do
    while action not in ["A", "P", "H", "C"]:
      action = input("what you want to do: [A]Attack, [P]Pokeball, [H]Health potion, [C]Change")
    if action == action.lower("A"):
      
      PlayerAttack(PlayerPokemon, EnemyPokemon, PlayerProfile, AttackHistory)
      EnemyAttack(EnemyPokemon, PlayerPokemon, PlayerProfile)
      #check if the player pokemon is alive
    elif action == action.lower("H"):
      #TODO si hay curas, se aplica, cura 50 de vida hasta llegar a 100, si no tiene no se cura
      CurePokemon(PlayerPokemon, PlayerProfile)
      EnemyAttack(EnemyPokemon)
    elif action == action.lower("P"):
      #TODO SI TIENE POKEBALLS PROBABILIDAD DEL USUARIO SI MENOS SALUD MAS PROBABLE
      CapturePokemon(EnemyPokemon,PlayerProfile)
    elif action == action.lower("C"):
      PlayerPokemon = ChoosePokemon(PlayerProfile)s
      

      #remove the dead pokemon and select new one
      PlayerProfile["PokemonInventory"].remove(PlayerPokemon)
      PlayerPokemon = ChoosePokemon(PlayerProfile)



  print("---- END OF THE FIGHT ----")
  input("press ENTER to continue...")


#fight(PlayerProfile, EnemyPokemon)