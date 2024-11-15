<h1 align=center>PokeFight</h1>

## Description
Python project about pokemon fights where a fight will happen in a Loop.

This readme is ready to read so you don´t need to download the files, but, if you want to download the files,
the instructions to donwload it are here: [Download Instructions](#download-instructions).

There are 150 pokemons everyone whit it's attacks, type, name and level, You start with 3 pokemons at random level between 1 and 7 pokemon and has to be leveling up by figthing,
you can catch the enemy pokemon, restore health of your pokemon or access your inventory

> [!NOTE]
> You can make an appointment or contribute to this little game by downloading it or writing any idea in the issues

## INDEX
Link to Pokemon stats: [Pokemon Stats](#pokemon-stats).

Link to explain the Profile section: [Profile](#profile).

Link to explain the Enemy Pokemon section: [Pokemons](#pokemons).

Link to explain the attacks and damage section: [Attacks and Damage](#attacks-and-damage).

Link to explain the Leveling section: [Leveling](#leveling).

Link to explain the capture pokemon section: [Capture Pokemon](#capture-pokemon).

Link to explain the Health Potion section: [Health Potion](#health-potion).

Link to explain the Item Lottery section: [Item Lottery](#item-lottery).

## Profile
You will have a Profile that you can access once you choose the pokemon.

In the profile it will be the pokemons you have with all the attacks and stats and
the inventory of pokeballs and health potions

> image of the profile function

### Pokemon Stats
The pokemons either if it's yours or enemy have the same number stats that will be:

> * name
> * health
> * type
> * attacks
> * level

## Pokemons

Link to explain the attacks and damage section: [Player Pokemons](#player-pokemons).

Link to explain the Enemy Pokemon section: [Enemy Pokemon](#enemy-pokemon).

### Player Pokemon
Start with 3 pokemons and with a random level and health adapted to each level, the attacks of the pokemons will be appearing by the level you are on,

> for example if you are on level 1 you will only have the attacks from that level,
> but, if your pokemon are in level 25 your pokemon will have the attacks of that level and below

In the start you would choose a pokemon between these 3 pokemons you have

[![imagen-2024-11-12-230811686.png](https://i.postimg.cc/vT9YDf5j/imagen-2024-11-12-230811686.png)](https://postimg.cc/JHrV2y6c)

and then it print the pokemons you've chosen vs the Enemy Pokemon

### Enemy Pokemon
The Enemy Pokemon will be choose randomness in the 150 pokemons we have and will have a diferent (higher, equal or less) level than you.
> The level of the pokemon is based on your level but with a variety of between 0 or 4 level plus

[![imagen-2024-11-11-224147516.png](https://i.postimg.cc/W3Czp1cz/imagen-2024-11-11-224147516.png)](https://postimg.cc/Q9gh0stZ)

## Attacks And Damage
Every turn a pokemon will attack with a random attack based on the level of the pokemon.

Every Attack will have some stats aswell, that will be:

> * name
> * Min Level
> * damage
> * type

The Damage will change by the type of the attack and the pokemons type.

Link to Player Attack: [Player Attack](#player-attack).

Link to explain the Enemy Attack: [Enemy Attack](#enemy-attack).

Link to explain the Damage: [Damage](#damage).

### Player Attack
It will show you the attacks you have avalible by the level you are on or below

[![imagen-2024-11-12-232423643.png](https://i.postimg.cc/0yj4fxB5/imagen-2024-11-12-232423643.png)](https://postimg.cc/LJdv4dSG)

The Player would choose an attack of the pokemon you have chosen previously to fight and if input you give to the program is not what expected
it will show a message of error

[![imagen-2024-11-12-232705887.png](https://i.postimg.cc/y8Gbp5Mm/imagen-2024-11-12-232705887.png)](https://postimg.cc/75g9fBYh)

### Enemy Attack 
The Enemy will attack with a random attack that the pokemon have and it can be used in the level the pokemon is

[![imagen-2024-11-12-230025441.png](https://i.postimg.cc/Kzf4xnr5/imagen-2024-11-12-230025441.png)](https://postimg.cc/BL8JCPz8)

### Damage
The damage will depend on the attack and the type of the pokemon that will receive it

If the pokemon type is strong against the attack type the attack will receive a penalty of damage, dividing it by 1.25,
If the pokemon type is weak afainst the attack type the attack will receive a boos of damage, multiplying it by 1.25

> image damagge function

## Leveling
The Pokemons you have will level up by fighting, every attack you do will give the pokemon points to level up

> image of the level up function

### Points
The level 1 needed points to level up will be 20 and will be increasing by level in 5.

The points will be given to the pokemon at the end of the battle if you win, and will have
a random chance based on the level of your pokemon compared to the other pokemon.

> image of the points given

### health
The base health in level 1 will be 100 and with every level up it increase in 10 points of health

## Capture Pokemon
You can capture pokemons by throwing them a pokeball you will have in the inventory.

### Chance of capturing
There will be a chance of capturing one depending on the level and the health of the pokemon that will be captured.
While the lower life the pokemon have, the higher will be the chances of capturing it,
and while the higher is the pokemon level in compare to your pokemon level the less chances you have to capture it

> image of the capture function

## Health Potion
You can use a Health Potion, which will be in your inventory, to cure 50 points of health to the pokemon you choose.
If you don't have it in the inventory or already have the life full it will print a message to tell you what happened

>image of the Health potion function

## Item Lottery
There will be given to you an object every time you finished a fight and have one or more pokemons alive,
It will be a random chance to get a pokeball o a Health potion

>image to item lottery function

## To Do

- [X] \Put colors in Terminal
- [ ] \Make an .exe to execute


> [!IMPORTANT]
> Below is how to install it downloading it or by git

## Download Instructions

Link to Download: [Download](#download).

Link to GIT Download: [GIT Download](#git-download).

Link to Install Visual Studio Code: [Install Visual Studio Code](#install-visual-studio-code).

### Download
click the blue button that says "code" and download the Zip

> image to download it

extract the zip

### GIT Download
Open a terminal and do "git clone (copy ssh url)"

```
git clone git@github.com:astrostitch/pokemon-game.git
```

### Install Visual Studio Code

To Install it You have to check if the interpreter is "python 3.11.10 ('.env':venv)"

>image to refer the interpreter

open a new terminal and go to "Pokefight"
```
cd ./pokemon-game/PokeFight
```
Run "Python PokemonCombatMain.py"
```
python Python PokemonCombatMain.py
```
