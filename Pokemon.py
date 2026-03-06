# -- Name: Pokemon
# -- Author: Oliver Culbert
# -- Date: 27/02/26

# ------- Imports ----------
import random
import time
# ------- Variables ---------
wild_pokemon = [
    {"Name":"Charizard","Type":"Fire","Level":random.randint(1, 3),"Health":random.randint(15, 25),"Attack":["Ember",5,"Flamethrower",10]},
    {"Name":"Venasuar","Type":"Grass","Level":random.randint(1, 3),"Health":random.randint(15, 25),"Attack":["Vine Whip",4,"Razor Leaf",8]},
    {"Name":"Blastoise","Type":"Water","Level":random.randint(1, 3),"Health":random.randint(15, 25),"Attack":["Water Gun",5,"Hydro Pump",9]},
    {"Name":"Pikachu","Type":"Electric","Level":random.randint(1, 3),"Health":random.randint(15, 25),"Attack":["Thunder Shock",6,"Thunderbolt",9]},
    {"Name":"Mewtwo","Type":"Psychic","Level":random.randint(1, 3),"Health":random.randint(15, 25),"Attack":["Confusion",7,"Psychic",11]},
    {"Name":"Eevee","Type":"Normal","Level":random.randint(1, 3),"Health":random.randint(15, 25),"Attack":["Tackle",4,"Quick Attack",6]}
]

own_pokemon = [{"Name":"Pidgy", "Type":"Flying", "Level":3, "Health": 20, "Attack": ["Flap", 4, "Wing Attack", 7]}]

# ------- Functions ----------
def overworld_timer():
    timer = random.randint(1, 5)
    print(timer)
    time.sleep(timer)
    print("Battle Begins")
    battle()


def battle():
    x = random.randint(0, len(wild_pokemon)-1)
    enemy_pokemon = wild_pokemon[x]
    player_pokemon = own_pokemon[0]
    player_pokemon_hp = player_pokemon["Health"]

    print("Player pokemon:", player_pokemon["Name"])
    print("Player pokemon Hp:", player_pokemon_hp)

    print("A wild", enemy_pokemon["Name"], "appeared")
    print("It's a", enemy_pokemon["Type"], "type pokemon")
    print("It's a level", enemy_pokemon["Level"])
    print("It has", enemy_pokemon["Health"], "health")

# ------- Start ---------
while True:
    enemy_attack_randomiser = random.randrange(0, 3, 2)
    print("Random number for attack", enemy_attack_randomiser)
    print(enemy_pokemon["Name"], "attacks with", enemy_pokemon["Attack"][enemy_attack_randomiser], "for",
          enemy_pokemon["Attack"][enemy_attack_randomiser + 1], "damage")
    player_pokemon_hp = player_pokemon_hp - enemy_pokemon["Attack"][enemy_attack_randomiser + 1]
    print(player_pokemon["Name"], "has", player_pokemon_hp, "health")

    overworld_timer()

overworld_timer()
