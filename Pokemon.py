# -- Name: Pokemon
# -- Author: Oliver Culbert
# -- Date: 27/02/26

# ------- Imports ----------
import random
import time

# ------- Variables ---------
wild_pokemon = [
    {"Name":"Charizard","Type":"Fire","Level":random.randint(1,3),"Health":random.randint(15,25),"Attack":["Ember",5,"Flamethrower",10]},
    {"Name":"Venasuar","Type":"Grass","Level":random.randint(1,3),"Health":random.randint(15,25),"Attack":["Vine Whip",4,"Razor Leaf",8]},
    {"Name":"Blastoise","Type":"Water","Level":random.randint(1,3),"Health":random.randint(15,25),"Attack":["Water Gun",5,"Hydro Pump",9]},
    {"Name":"Pikachu","Type":"Electric","Level":random.randint(1,3),"Health":random.randint(15,25),"Attack":["Thunder Shock",6,"Thunderbolt",9]},
    {"Name":"Mewtwo","Type":"Psychic","Level":random.randint(1,3),"Health":random.randint(15,25),"Attack":["Confusion",7,"Psychic",11]},
    {"Name":"Eevee","Type":"Normal","Level":random.randint(1,3),"Health":random.randint(15,25),"Attack":["Tackle",4,"Quick Attack",6]}
]

own_pokemon = [{"Name":"Pidgy","Type":"Flying","Level":3,"Health":20,"Attack":["Flap",4,"Wing Attack",7]}]

# ------- Functions ----------
def overworld_timer():
    timer = random.randint(1,5)
    print("Exploring for",timer,"seconds...")
    time.sleep(timer)
    print("A battle begins!\n")
    battle()


def battle():
    enemy_pokemon = random.choice(wild_pokemon)
    player_pokemon = own_pokemon[0]
    enemy_hp = enemy_pokemon["Health"]
    player_hp = player_pokemon["Health"]
    print("Your Pokemon:",player_pokemon["Name"],"| HP:",player_hp)
    print("A wild",enemy_pokemon["Name"],"appeared!")
    print(enemy_pokemon["Name"],"HP:",enemy_hp,"\n")

    while True:
        # ----- PLAYER TURN -----
        print("Choose your attack")
        print("1.",player_pokemon["Attack"][0])
        print("2.",player_pokemon["Attack"][2])

        choice = input("> ")

        if choice == "1":
            damage = player_pokemon["Attack"][1]
            move = player_pokemon["Attack"][0]

        elif choice == "2":
            damage = player_pokemon["Attack"][3]
            move = player_pokemon["Attack"][2]

        else:
            print("Invalid move!")
            continue

        print(player_pokemon["Name"],"used",move)
        enemy_hp -= damage
        print(enemy_pokemon["Name"],"HP:",enemy_hp,"\n")
        if enemy_hp <= 0:
            print("The wild",enemy_pokemon["Name"],"fainted!")
            break

        time.sleep(1)

        # ----- ENEMY TURN -----
        enemy_attack_randomiser = random.randrange(0,3,2)
        enemy_move = enemy_pokemon["Attack"][enemy_attack_randomiser]
        enemy_damage = enemy_pokemon["Attack"][enemy_attack_randomiser+1]
        print(enemy_pokemon["Name"],"used",enemy_move)
        player_hp -= enemy_damage
        print(player_pokemon["Name"],"HP:",player_hp,"\n")

        if player_hp <= 0:
            print(player_pokemon["Name"],"fainted!")
            break

        time.sleep(1)


# ------- Start ---------
overworld_timer()