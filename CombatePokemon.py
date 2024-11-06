from pokeload import GetAllPokemons
from pokefight import fight, PlayerPokemonLive
import random
from pprint import pprint
from time import sleep


#collect all the info of the player
def GetPlayerProfile(PokemonList):
  return {
    "player_name": input("como te llamas joven aventurero?\n"),
    "PokemonInventory": [random.choice(PokemonList) for a in range(3)],
    "combats": 0,
    "pokeballs": 1,
    "HealthPotion": 1
  }

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
    print("current pokeballs: {}".format(pokeballs))
  else:
    print("You win a HEALTH POTION!!!")
    PlayerProfile["HealthPotion"] += 1
    print("current healt potions: {}".format(HealthPotion))

def main():
  PokemonList = GetAllPokemons()
  PlayerProfile = GetPlayerProfile(PokemonList)
  #loop to continue the game if at least 1 player pokemon is alive
  while PlayerPokemonLive(PlayerProfile) > 0:
    EnemyPokemon = random.choice(PokemonList)
    fight(PlayerProfile, EnemyPokemon)
    if PlayerPokemonLive(PlayerProfile) > 0:
      ItemLottery(PlayerProfile)
  print("you lost in the fight: {}".format(PlayerProfile["combats"]))



if __name__ == "__main__":
  main() 