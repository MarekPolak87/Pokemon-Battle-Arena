import random

import list_pokemon as lp, moves as mvs
import moves

stat_changes_multipliers = {
    -6: 0.25,
    -5: 0.28,
    -4: 0.33,
    -3: 0.40,
    -2: 0.50,
    -1: 0.66,
    0: 1,
    1: 1.5,
    2: 2,
    3: 2.5,
    4: 3,
    5: 3.5,
    6: 4,
    }

statuses = {
    1 : "OK",
    2 : "asleep",
    3 : "paralyzed",
    4 : "flinched",
    5 : "frozen",
    6 : "burned",
    7 : "poisoned",
    8 : "confused",
    9 : "dug",
    10 : "seeded",
    11 : "flown",
    12 : "fainted"
}

type_colors_for_GUI = {'grass' : 'chartreuse1',
                       'fire' : 'orangered1',
                       'water' : 'DodgerBlue2',
                       'bug' : 'chartreuse4',
                       'normal' : 'aliceblue',
                       'poison' : 'chocolate',
                       'electric' : 'yellow1',
                       'ground' : 'antiquewhite3',
                       'fairy' : 'deeppink1',
                       'fighting' : 'magenta',
                       'psychic' : 'gold1',
                       'rock' : 'gray57',
                       'ghost' : 'lightsteelblue2',
                       'ice' : 'aqua',
                       'dragon' : 'blueviolet'}
def move_assigner1(type1):
    chosen_move = ""
    if type1 == "fire":
        chosen_move = moves.fire_moves[random.randint(0, len(moves.fire_moves) - 1)][0]
    elif type1 == "poison":
        chosen_move = moves.poison_moves[random.randint(0, len(moves.poison_moves) - 1)][0]
    elif type1 == "psychic":
        chosen_move = moves.psychic_moves[random.randint(0, len(moves.psychic_moves) - 1)][0]
    elif type1 == "ice":
        chosen_move = moves.ice_moves[random.randint(0, len(moves.ice_moves) -1)][0]
    elif type1 == "normal":
        chosen_move = moves.normal_moves[random.randint(0, len(moves.normal_moves) -1)][0]
    elif type1 == "ground":
        chosen_move = moves.ground_moves[random.randint(0, len(moves.ground_moves) -1)][0]
    elif type1 == "water":
        chosen_move = moves.water_moves[random.randint(0, len(moves.water_moves) -1)][0]
    elif type1 == "ghost":
        chosen_move = moves.ghost_moves[random.randint(0, len(moves.ghost_moves) -1)][0]
    elif type1 == "flying":
        chosen_move = moves.flying_moves[random.randint(0, len(moves.flying_moves) -1)][0]
    elif type1 == "rock":
        chosen_move = moves.rock_moves[random.randint(0, len(moves.rock_moves) -1)][0]
    elif type1 == "fighting":
        chosen_move = moves.fighting_moves[random.randint(0, len(moves.fighting_moves) -1)][0]
    elif type1 == "grass":
        chosen_move = moves.grass_moves[random.randint(0, len(moves.grass_moves) -1)][0]
    elif type1 == "electric":
        chosen_move = moves.electric_moves[random.randint(0, len(moves.electric_moves) -1)][0]
    elif type1 == "bug":
        chosen_move = moves.grass_moves[random.randint(0, len(moves.grass_moves) -1)][0]
    elif type1 == "dragon":
        chosen_move = moves.flying_moves[random.randint(0, len(moves.flying_moves) - 1)][0]
    elif type1 == "fairy":
        chosen_move = moves.normal_moves[random.randint(0, len(moves.normal_moves) -1)][0]
    return chosen_move

def move_assigner2(type2,type1) :
    chosen_move = ""
    if type2 == "fire" :
        chosen_move = moves.fire_moves[random.randint(0, len(moves.fire_moves) -1)][0]
    elif type2 == "poison" :
        chosen_move = moves.poison_moves[random.randint(0, len(moves.poison_moves) -1)][0]
    elif type2 == "psychic" :
        chosen_move = moves.psychic_moves[random.randint(0, len(moves.psychic_moves) -1)][0]
    elif type2 == "ice" :
        chosen_move = moves.ice_moves[random.randint(0, len(moves.ice_moves) -1)][0]
    elif type2 == "normal" :
        chosen_move = moves.normal_moves[random.randint(0, len(moves.normal_moves) -1)][0]
    elif type2 == "ground" :
        chosen_move = moves.ground_moves[random.randint(0, len(moves.ground_moves) -1)][0]
    elif type2 == "water" :
        chosen_move = moves.water_moves[random.randint(0, len(moves.water_moves) -1)][0]
    elif type2 == "ghost" :
        chosen_move = moves.ghost_moves[random.randint(0, len(moves.ghost_moves) -1)][0]
    elif type2 == "flying" :
        chosen_move = moves.flying_moves[random.randint(0, len(moves.flying_moves) -1)][0]
    elif type2 == "rock" :
        chosen_move = moves.rock_moves[random.randint(0, len(moves.rock_moves) -1)][0]
    elif type2 == "fighting" :
        chosen_move = moves.fighting_moves[random.randint(0, len(moves.fighting_moves) -1)][0]
    elif type2 == "grass" :
        chosen_move = moves.grass_moves[random.randint(0, len(moves.grass_moves) -1)][0]
    elif type2 == "electric" :
        chosen_move = moves.electric_moves[random.randint(0, len(moves.electric_moves) -1)][0]
    elif type2 == "bug":
        chosen_move = moves.grass_moves[random.randint(0, len(moves.grass_moves) -1)][0]
    elif type2 == "dragon":
        chosen_move = moves.flying_moves[random.randint(0, len(moves.flying_moves) - 1)][0]
    elif type2 == "fairy":
        chosen_move = moves.normal_moves[random.randint(0, len(moves.normal_moves) -1)][0]
    else:
        if type1 == "fire" :
            chosen_move = moves.fire_moves[random.randint(0, len(moves.fire_moves) - 1)][0]
        elif type1 == "poison" :
            chosen_move = moves.poison_moves[random.randint(0, len(moves.poison_moves) - 1)][0]
        elif type1 == "psychic" :
            chosen_move = moves.psychic_moves[random.randint(0, len(moves.psychic_moves) - 1)][0]
        elif type1 == "ice" :
            chosen_move = moves.ice_moves[random.randint(0, len(moves.ice_moves) - 1)][0]
        elif type1 == "normal" :
            chosen_move = moves.normal_moves[random.randint(0, len(moves.normal_moves) - 1)][0]
        elif type1 == "ground" :
            chosen_move = moves.ground_moves[random.randint(0, len(moves.ground_moves) - 1)][0]
        elif type1 == "water" :
            chosen_move = moves.water_moves[random.randint(0, len(moves.water_moves) - 1)][0]
        elif type1 == "ghost" :
            chosen_move = moves.ghost_moves[random.randint(0, len(moves.ghost_moves) - 1)][0]
        elif type1 == "flying" :
            chosen_move = moves.flying_moves[random.randint(0, len(moves.flying_moves) - 1)][0]
        elif type1 == "rock" :
            chosen_move = moves.rock_moves[random.randint(0, len(moves.rock_moves) - 1)][0]
        elif type1 == "fighting" :
            chosen_move = moves.fighting_moves[random.randint(0, len(moves.fighting_moves) - 1)][0]
        elif type1 == "grass" :
            chosen_move = moves.grass_moves[random.randint(0, len(moves.grass_moves) - 1)][0]
        elif type1 == "electric" :
            chosen_move = moves.electric_moves[random.randint(0, len(moves.electric_moves) - 1)][0]
        elif type1 == "bug":
            chosen_move = moves.grass_moves[random.randint(0, len(moves.grass_moves) - 1)][0]
        elif type1 == "dragon" :
            chosen_move = moves.flying_moves[random.randint(0, len(moves.flying_moves) - 1)][0]
        elif type1 == "fairy" :
            chosen_move = moves.normal_moves[random.randint(0, len(moves.normal_moves) - 1)][0]
    return chosen_move
class Pokemon:
    def __init__(self, name):
        self.name = lp.pokemon_list[name]["name"]
        self.nr = lp.pokemon_list[name]["nr"]
        self.hp = lp.pokemon_list[name]["hp"]
        self.attack = [lp.pokemon_list[name]["attack"], 0]
        self.defense = [lp.pokemon_list[name]["defense"], 0]
        self.spec_att = [lp.pokemon_list[name]["spec_att"], 0]
        self.spec_def = [lp.pokemon_list[name]["spec_def"], 0]
        self.speed = [lp.pokemon_list[name]["speed"], 0]
        self.evasion = 0
        self.accuracy = 0
        self.chosen = False
        self.status = 1
        self.level = 50
        self.type1 = lp.pokemon_list[name]["type1"]
        self.type2 = lp.pokemon_list[name]["type2"]
        self.GUI_color = type_colors_for_GUI[lp.pokemon_list[name]["type1"]]
        self.move_1 = mvs.moves_g1[move_assigner1(lp.pokemon_list[name]["type1"])]
        self.move_2 = mvs.moves_g1[mvs.normal_moves[random.randint(0, len(moves.normal_moves) - 1)][0]]
        self.move_3 = mvs.moves_g1[move_assigner2(lp.pokemon_list[name]["type2"], lp.pokemon_list[name]["type1"])]
        self.move_4 = mvs.moves_g1[move_assigner2(lp.pokemon_list[name]["type2"], lp.pokemon_list[name]["type1"])]











