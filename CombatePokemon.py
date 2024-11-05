from pokeload import GetAllPokemons
from pokefight import fight, PlayerPokemonLive
import random
from pprint import pprint


#collect all the info of the player
def GetPlayerProfile(PokemonList):
  return {
    "player_name": input("como te llamas joven aventurero?\n"),
    "PokemonInventory": [random.choice(PokemonList) for a in range(3)],
    "combats": 0,
    "pokeballs": 0,
    "HealthPotion": 0
  }

def ItemLottery(PlayerProfile):
  """segun aleatorio sumo cura o pokeball"""

def main():
  PokemonList = GetAllPokemons()
  PlayerProfile = GetPlayerProfile(PokemonList)
  #loop to continue the game if at least 1 player pokemon is alive
  while PlayerPokemonLive(PlayerProfile) > 0:
    EnemyPokemon = random.choice(PokemonList)
    fight(PlayerProfile, EnemyPokemon)
    ItemLottery(PlayerProfile)
  print("you lost in the fight: {}".format(PlayerProfile["combats"]))



if __name__ == "__main__":
  main() 