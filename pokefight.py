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
def PlayerAttack(PlayerPokemon, EnemyPokemon):
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

#the loop for the attack of the enemy
def EnemyAttack(EnemyPokemon, PlayerPokemon):
  sleep(1)
  SelectAttack = random.choice(EnemyPokemon["attacks"])
  print("\n{} attack with {} and do {} of damage".format(EnemyPokemon["name"],
                                                   SelectAttack["name"],
                                                   SelectAttack["damage"]))
  
  PlayerPokemon["CurrentHealth"] -= SelectAttack["damage"]

  print("-------------------------------")
  print("your current health is {}/{}".format(PlayerPokemon["CurrentHealth"],
                                              PlayerPokemon["BaseHealth"]))
  input("pulse cualquier tecla para continuar...")

#principal loop of the fight
def fight(PlayerProfile, EnemyPokemon):
  print("---- NUEVO COMBATE ----\n")

  PlayerPokemon = ChoosePokemon(PlayerProfile)

  print("contrincantes: {} vs {}".format(PokemonInfo(PlayerPokemon), 
                                         PokemonInfo(EnemyPokemon)))
  while PlayerPokemonLive(PlayerProfile) > 0 and EnemyPokemon["CurrentHealth"] > 0:
    PlayerAttack(PlayerPokemon, EnemyPokemon)
    #check if the enemy current health is non 0
    if EnemyPokemon["CurrentHealth"] <= 0:
      print("\n------------------------")
      print("You Win this fight!")
      print("------------------------")
      break
    EnemyAttack(EnemyPokemon, PlayerPokemon)
    #check if the player pokemon is alive
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
      #remove the dead pokemon and select new one
      PlayerProfile["PokemonInventory"].remove(PlayerPokemon)
      PlayerPokemon = ChoosePokemon(PlayerProfile)


  print("---- FIN DEL COMBATE ----")
  input("presiona ENTER para continuar...")


#fight(PlayerProfile, EnemyPokemon)