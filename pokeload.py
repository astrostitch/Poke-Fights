from requests_html import HTMLSession
import pickle
import random

#libreria base de los pokemon
PokemonBase = {
  "name": "", 
  "CurrentHealth": 100,
  "BaseHealth": 100,
  "level": random.randint(1,7),
  "type": "",
  "CurrentExp": 0
}

URLBase = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/pkmn&pk="
URLAttack = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/movimientos_nivel&pk="

#collect the name of the pokemons we are going to use
def GetPokemon(index):

  url = "{}{}".format(URLBase, index)
  urlattacks = "{}{}".format(URLAttack, index) + "#rze"

  session = HTMLSession()
  #copy the library of the pokemon
  NewPokemon = PokemonBase.copy()
  PokemonPage = session.get(url)

  NewPokemon["type"] = []

  NewPokemon["name"] = PokemonPage.html.find(".mini", first=True).text.split("\n")[0]
  for img in  PokemonPage.html.find(".pkmain", first = True).find(".bordeambos", first = True).find("img"):
    NewPokemon["type"].append(img.attrs["alt"])

  AttackPage = session.get(urlattacks)
  NewPokemon["attacks"] = []

  for AttackItem in AttackPage.html.find(".pkmain")[-1].find("tr .check3"):
    attack = {
      "name": AttackItem.find("td", first = True).find("a", first = True).text,
      "type": AttackItem.find("td")[1].find("img", first = True).attrs["alt"],
      "MinLevel": AttackItem.find("th",first = True).text,
      "damage": int(AttackItem.find("td")[3].text.replace("--", "0"))
    }
    NewPokemon["attacks"].append(attack)

  return NewPokemon



#collect the pokemons and create the file to it
def GetAllPokemons():
  try: #try to open the file with the pokemons
    print("cargando el archivo de Pokemons...\n")
    with open("pokefile.pkl", "rb") as pokefile: 
      AllPokemons = pickle.load(pokefile)
  except FileNotFoundError:
    print("archivo no encontrado, descargando de la pokedex!...\n")
    AllPokemons = []
    #collect every pokemon
    for index in range(151):
      AllPokemons.append(GetPokemon(index + 1))
      print("*")
    print("-------------------------------------------------\n")
    print("todos los pokemons han sido cargados con exito!!!")
    with open("pokefile.pkl", "wb") as pokefile:
      pickle.dump(AllPokemons, pokefile)
  print("Lista de pokemons cargados!!!")
  return AllPokemons