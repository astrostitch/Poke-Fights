from pokeload import GetAllPokemons
from pokefight import fight, PlayerPokemonLive
import random
from pprint import pprint



def GetPlayerProfile(PokemonList):
  return {
    "player_name": input("como te llamas joven aventurero?\n"),
    "PokemonInventory": [random.choice(PokemonList) for a in range(3)],
    "combats": 0,
    "pokeballs": 0,
    "HealthPotion": 0
  }








def main():
  PokemonList = GetAllPokemons()
  PlayerProfile = GetPlayerProfile(PokemonList)
  #pprint(PlayerProfile)
  while PlayerPokemonLive(PlayerProfile) > 0:
    EnemyPokemon = random.choice(PokemonList)
    fight(PlayerProfile, EnemyPokemon)
  print("has perdido en el combate numero: {}".format(PlayerProfile["combats"]))



if __name__ == "__main__":
  main() 