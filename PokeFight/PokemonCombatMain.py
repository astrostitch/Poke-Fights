from pokeload import GetAllPokemons
from pokefight import fight, PlayerPokemonLive
import random
from pprint import pprint
from time import sleep
import sys

#collect all the info of the player
def GetPlayerProfile(PokemonList):
  return {
    "player_name": input("What's your name traveller?\n"),
    "PokemonInventory": [random.choice(PokemonList) for a in range(3)],
    "combats": 0,
    "pokeballs": 1,
    "HealthPotion": 1
  }


#The Item lottery in the final fight
def ItemLottery(PlayerProfile):
  sleep(1)
  print("\n-------------------------------------------------------------")
  print("it will be assigned by lottery a pokeball or a health potion")
  HealthPotion = PlayerProfile["HealthPotion"]
  pokeballs = PlayerProfile["pokeballs"]
  #print the current pokeballs and health potion
  print("current pokeballs: {} | current healt potions: {}".format(pokeballs, HealthPotion))
  ChoiceList = [HealthPotion, pokeballs]
  choose = random.choice(ChoiceList)
  sleep(1)
  #stablish the lottery win
  if choose == pokeballs:
    print("You win a POKEBALL!!!")
    PlayerProfile["pokeballs"] += 1
    print("current pokeballs: {}".format(PlayerProfile["pokeballs"]))
    sleep(0.5)
  else:
    print("You win a HEALTH POTION!!!")
    PlayerProfile["HealthPotion"] += 1
    print("current healt potions: {}".format(PlayerProfile["HealthPotion"]))
    sleep(0.5)


#stablish the the health by the pokemon level
def PokemonHealth(Pokemon):
  if Pokemon["level"] > 1:
  #increase the live of the pokemons by level
    HealthToSum = 10 - Pokemon["level"]
    if HealthToSum > 0:
      Pokemon["BaseHealth"] += (Pokemon["level"] + HealthToSum) * Pokemon["level"]
      Pokemon["CurrentHealth"] += (Pokemon["level"] + HealthToSum) * Pokemon["level"]
    else:
      Pokemon["BaseHealth"] += (Pokemon["level"] + (+(HealthToSum)))
      Pokemon["CurrentHealth"] += (Pokemon["level"] + (+(HealthToSum)))     


#main function
def main():
  PokemonList = GetAllPokemons()
  PlayerProfile = GetPlayerProfile(PokemonList)
  PokemonInventory = PlayerProfile["PokemonInventory"]
  #randomize the level of the player pokemons and scale the health
  for index in range(len(PokemonInventory)):
    PokemonInventory[index]["level"] = random.randint(1, 7)
    PokemonHealth(PokemonInventory[index])
    
  #loop to continue the game if at least 1 player pokemon is alive
  while PlayerPokemonLive(PlayerProfile) > 0:
    EnemyPokemon = random.choice(PokemonList)
    fight(PlayerProfile, EnemyPokemon)
    if PlayerPokemonLive(PlayerProfile) > 0:
      ItemLottery(PlayerProfile)
  print("you lost in the fight: {}".format(PlayerProfile["combats"]))



if __name__ == "__main__":
  main() 