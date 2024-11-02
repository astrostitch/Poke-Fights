from requests_html import HTMLSession
import pickle

#libreria base de los pokemon
PokemonBase = {
  "name": "", 
  "CurrentHealth": 100,
  "BaseHealth": 100,
  "level": 1,
  "type": "",
  "CurrentExp": 0
}

URLBase = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/pkmn&pk="
URLAttack = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/movimientos_nivel&pk="

#conseguir el pokemon que vamos a usar
def GetPokemon(index):

  url = "{}{}".format(URLBase, index)
  urlattacks = "{}{}".format(URLAttack, index) + "#rze"

  session = HTMLSession()

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




def GetAllPokemons():
  AllPokemons = []
  for index in range(151):
    AllPokemons.append(GetPokemon(index + 1))
  with open("pokefile.pkl", "wb") as pokefile:
    pickle.dump(AllPokemons, pokefile)
  return AllPokemons

def main():
  GetAllPokemons()
  GetPokemon(GetAllPokemons)

  print(GetPokemon(GetAllPokemons))

if __name__ == "__main__":
  main()
