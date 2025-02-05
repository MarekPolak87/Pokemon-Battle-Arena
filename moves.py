import random

moves_g1 = {
    # "Absorb" : {
    #     "name" : "Absorb", "nr" : 1, "move_type" : "grass", "category" : "special", "TM" : 0, "power" : 20,
    #     "accuracy" : 100, "PP" : 25
    #     },
    "Acid" : {
        "name" : "Acid", "nr" : 2, "move_type" : "POISON", "category" : "special", "TM" : 0, "power" : 40,
        "accuracy" : 100, "PP" : 30
        },
    "Acid Armor" : {
        "name" : "Acid Armor", "nr" : 3, "move_type" : "POISON", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 0, "PP" : 20
        },
    "Agility" : {
        "name" : "Agility", "nr" : 4, "move_type" : "PSYCHIC", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 0, "PP" : 30
        },
    "Amnesia" : {
        "name" : "Amnesia", "nr" : 5, "move_type" : "PSYCHIC", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 0, "PP" : 20
        },
    "Aurora Beam" : {
        "name" : "Aurora Beam", "nr" : 6, "move_type" : "ICE", "category" : "special", "TM" : 0, "power" : 65,
        "accuracy" : 100, "PP" : 20
        },
    "Barrage" : {
        "name" : "Barrage", "nr" : 7, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 15,
        "accuracy" : 85, "PP" : 20
        },
    "Barrier" : {
        "name" : "Barrier", "nr" : 8, "move_type" : "PSYCHIC", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 0, "PP" : 20
        },
    # "Bide" : {
    #     "name" : "Bide", "nr" : 9, "move_type" : "NORMAL", "category" : "physical", "TM" : 34, "power" : 0,
    #     "accuracy" : 0, "PP" : 10
    #     },
    # "Bind" : {
    #     "name" : "Bind", "nr" : 10, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 15,
    #     "accuracy" : 85, "PP" : 20
    #     },
    "Bite" : {
        "name" : "Bite", "nr" : 11, "move_type" : "DARK", "category" : "physical", "TM" : 0, "power" : 60,
        "accuracy" : 100, "PP" : 25
        },
    "Blizzard" : {
        "name" : "Blizzard", "nr" : 12, "move_type" : "ICE", "category" : "special", "TM" : 14, "power" : 110,
        "accuracy" : 70, "PP" : 5
        },
    "Body Slam" : {
        "name" : "Body Slam", "nr" : 13, "move_type" : "NORMAL", "category" : "physical", "TM" : 8, "power" : 85,
        "accuracy" : 100, "PP" : 15
        },
    "Bone Club" : {
        "name" : "Bone Club", "nr" : 14, "move_type" : "GROUND", "category" : "physical", "TM" : 0, "power" : 65,
        "accuracy" : 85, "PP" : 20
        },
    # "Bonemerang" : {
    #     "name" : "Bonemerang", "nr" : 15, "move_type" : "GROUND", "category" : "physical", "TM" : 0, "power" : 50,
    #     "accuracy" : 90, "PP" : 10
    #     },
    "Bubble" : {
        "name" : "Bubble", "nr" : 16, "move_type" : "WATER", "category" : "special", "TM" : 0, "power" : 40,
        "accuracy" : 100, "PP" : 30
        },
    "Bubble Beam" : {
        "name" : "Bubble Beam", "nr" : 17, "move_type" : "WATER", "category" : "special", "TM" : 11, "power" : 65,
        "accuracy" : 100, "PP" : 20
        },
    # "Clamp" : {
    #     "name" : "Clamp", "nr" : 18, "move_type" : "WATER", "category" : "physical", "TM" : 0, "power" : 35,
    #     "accuracy" : 85, "PP" : 15
    #     },
    "Comet Punch" : {
        "name" : "Comet Punch", "nr" : 19, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 18,
        "accuracy" : 85, "PP" : 15
        },
    "Confuse Ray" : {
        "name" : "Confuse Ray", "nr" : 20, "move_type" : "GHOST", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 100, "PP" : 10
        },
    "Confusion" : {
        "name" : "Confusion", "nr" : 21, "move_type" : "PSYCHIC", "category" : "special", "TM" : 0, "power" : 50,
        "accuracy" : 100, "PP" : 25
        },
    "Constrict" : {
        "name" : "Constrict", "nr" : 22, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 10,
        "accuracy" : 100, "PP" : 35
        },
    # "Conversion" : {
    #     "name" : "Conversion", "nr" : 23, "move_type" : "NORMAL", "category" : "status", "TM" : 0, "power" : 0,
    #     "accuracy" : 0, "PP" : 30
    #     },
    # "Counter" : {
    #     "name" : "Counter", "nr" : 24, "move_type" : "FIGHTING", "category" : "physical", "TM" : 18, "power" : 0,
    #     "accuracy" : 100, "PP" : 20
    #     },
    "Crabhammer" : {
        "name" : "Crabhammer", "nr" : 25, "move_type" : "WATER", "category" : "physical", "TM" : 0, "power" : 100,
        "accuracy" : 90, "PP" : 10
        },
    "Cut" : {
        "name" : "Cut", "nr" : 26, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 50,
        "accuracy" : 95, "PP" : 30
        },
    "Defense Curl" : {
        "name" : "Defense Curl", "nr" : 27, "move_type" : "NORMAL", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 0, "PP" : 40
        },
    # "Dig" : {
    #     "name" : "Dig", "nr" : 28, "move_type" : "GROUND", "category" : "physical", "TM" : 28, "power" : 80,
    #     "accuracy" : 100, "PP" : 10
    #     },
    # "Disable" : {
    #     "name" : "Disable", "nr" : 29, "move_type" : "NORMAL", "category" : "status", "TM" : 0, "power" : 0,
    #     "accuracy" : 100, "PP" : 20
    #     },
    "Dizzy Punch" : {
        "name" : "Dizzy Punch", "nr" : 30, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 70,
        "accuracy" : 100, "PP" : 10
        },
    # "Double Kick" : {
    #     "name" : "Double Kick", "nr" : 31, "move_type" : "FIGHTING", "category" : "physical", "TM" : 0, "power" : 30,
    #     "accuracy" : 100, "PP" : 30
    #     },
    "Double Slap" : {
        "name" : "Double Slap", "nr" : 32, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 15,
        "accuracy" : 85, "PP" : 10
        },
    "Double Team" : {
        "name" : "Double Team", "nr" : 33, "move_type" : "NORMAL", "category" : "status", "TM" : 32, "power" : 0,
        "accuracy" : 0, "PP" : 15
        },
    # "Double-Edge" : {
    #     "name" : "Double-Edge", "nr" : 34, "move_type" : "NORMAL", "category" : "physical", "TM" : 10, "power" : 120,
    #     "accuracy" : 100, "PP" : 15
    #     },
    # "Dragon Rage" : {
    #     "name" : "Dragon Rage", "nr" : 35, "move_type" : "DRAGON", "category" : "special", "TM" : 23, "power" : 0,
    #     "accuracy" : 100, "PP" : 10
    #     },
    # "Dream Eater" : {
    #     "name" : "Dream Eater", "nr" : 36, "move_type" : "PSYCHIC", "category" : "special", "TM" : 42, "power" : 100,
    #     "accuracy" : 100, "PP" : 15
    #     },
    "Drill Peck" : {
        "name" : "Drill Peck", "nr" : 37, "move_type" : "FLYING", "category" : "physical", "TM" : 0, "power" : 80,
        "accuracy" : 100, "PP" : 20
        },
    # "Earthquake" : {
    #     "name" : "Earthquake", "nr" : 38, "move_type" : "GROUND", "category" : "physical", "TM" : 26, "power" : 100,
    #     "accuracy" : 100, "PP" : 10
    #     },
    "Egg Bomb" : {
        "name" : "Egg Bomb", "nr" : 39, "move_type" : "NORMAL", "category" : "physical", "TM" : 37, "power" : 100,
        "accuracy" : 75, "PP" : 10
        },
    "Ember" : {
        "name" : "Ember", "nr" : 40, "move_type" : "FIRE", "category" : "special", "TM" : 0, "power" : 40,
        "accuracy" : 100, "PP" : 25
        },
    # "Explosion" : {
    #     "name" : "Explosion", "nr" : 41, "move_type" : "NORMAL", "category" : "physical", "TM" : 47, "power" : 250,
    #     "accuracy" : 100, "PP" : 5
    #     },
    "Fire Blast" : {
        "name" : "Fire Blast", "nr" : 42, "move_type" : "FIRE", "category" : "special", "TM" : 38, "power" : 110,
        "accuracy" : 85, "PP" : 5
        },
    "Fire Punch" : {
        "name" : "Fire Punch", "nr" : 43, "move_type" : "FIRE", "category" : "physical", "TM" : 0, "power" : 75,
        "accuracy" : 100, "PP" : 15
        },
    # "Fire Spin" : {
    #     "name" : "Fire Spin", "nr" : 44, "move_type" : "FIRE", "category" : "special", "TM" : 0, "power" : 35,
    #     "accuracy" : 85, "PP" : 15
    #     },
    # "Fissure" : {
    #     "name" : "Fissure", "nr" : 45, "move_type" : "GROUND", "category" : "physical", "TM" : 27, "power" : 0,
    #     "accuracy" : 30, "PP" : 5
    #     },
    "Flamethrower" : {
        "name" : "Flamethrower", "nr" : 46, "move_type" : "FIRE", "category" : "special", "TM" : 0, "power" : 90,
        "accuracy" : 100, "PP" : 15
        },
    "Flash" : {
        "name" : "Flash", "nr" : 47, "move_type" : "NORMAL", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 100, "PP" : 20
        },
    # "Fly" : {
    #     "name" : "Fly", "nr" : 48, "move_type" : "FLYING", "category" : "physical", "TM" : 0, "power" : 90,
    #     "accuracy" : 95, "PP" : 15
    #     },
    # "Focus Energy" : {
    #     "name" : "Focus Energy", "nr" : 49, "move_type" : "NORMAL", "category" : "status", "TM" : 0, "power" : 0,
    #     "accuracy" : 0, "PP" : 30
    #     },
    "Fury Attack" : {
        "name" : "Fury Attack", "nr" : 50, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 15,
        "accuracy" : 85, "PP" : 20
        },
    "Fury Swipes" : {
        "name" : "Fury Swipes", "nr" : 51, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 18,
        "accuracy" : 80, "PP" : 15
        },
    "Glare" : {
        "name" : "Glare", "nr" : 52, "move_type" : "NORMAL", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 100, "PP" : 30
        },
    "Growl" : {
        "name" : "Growl", "nr" : 53, "move_type" : "NORMAL", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 100, "PP" : 40
        },
    # "Growth" : {
    #     "name" : "Growth", "nr" : 54, "move_type" : "NORMAL", "category" : "status", "TM" : 0, "power" : 0,
    #     "accuracy" : 0, "PP" : 20
    #     },
    # "Guillotine" : {
    #     "name" : "Guillotine", "nr" : 55, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 0,
    #     "accuracy" : 30, "PP" : 5
    #     },
    # "Gust" : {
    #     "name" : "Gust", "nr" : 56, "move_type" : "FLYING", "category" : "special", "TM" : 0, "power" : 40,
    #     "accuracy" : 100, "PP" : 35
    #     },
    "Harden" : {
        "name" : "Harden", "nr" : 57, "move_type" : "NORMAL", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 0, "PP" : 30
        },
    # "Haze" : {
    #     "name" : "Haze", "nr" : 58, "move_type" : "ICE", "category" : "status", "TM" : 0, "power" : 0, "accuracy" : 0,
    #     "PP" : 30
    #     },
    "Headbutt" : {
        "name" : "Headbutt", "nr" : 59, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 70,
        "accuracy" : 100, "PP" : 15
        },
    # "High Jump Kick" : {
    #     "name" : "High Jump Kick", "nr" : 60, "move_type" : "FIGHTING", "category" : "physical", "TM" : 0,
    #     "power" : 130, "accuracy" : 90, "PP" : 10
    #     },
    "Horn Attack" : {
        "name" : "Horn Attack", "nr" : 61, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 65,
        "accuracy" : 100, "PP" : 25
        },
    # "Horn Drill" : {
    #     "name" : "Horn Drill", "nr" : 62, "move_type" : "NORMAL", "category" : "physical", "TM" : 7, "power" : 0,
    #     "accuracy" : 30, "PP" : 5
    #     },
    "Hydro Pump" : {
        "name" : "Hydro Pump", "nr" : 63, "move_type" : "WATER", "category" : "special", "TM" : 0, "power" : 110,
        "accuracy" : 80, "PP" : 5
        },
    # "Hyper Beam" : {
    #     "name" : "Hyper Beam", "nr" : 64, "move_type" : "NORMAL", "category" : "special", "TM" : 15, "power" : 150,
    #     "accuracy" : 90, "PP" : 5
    #     },
    "Hyper Fang" : {
        "name" : "Hyper Fang", "nr" : 65, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 80,
        "accuracy" : 90, "PP" : 15
        },
    "Hypnosis" : {
        "name" : "Hypnosis", "nr" : 66, "move_type" : "PSYCHIC", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 60, "PP" : 20
        },
    "Ice Beam" : {
        "name" : "Ice Beam", "nr" : 67, "move_type" : "ICE", "category" : "special", "TM" : 13, "power" : 90,
        "accuracy" : 100, "PP" : 10
        },
    "Ice Punch" : {
        "name" : "Ice Punch", "nr" : 68, "move_type" : "ICE", "category" : "physical", "TM" : 0, "power" : 75,
        "accuracy" : 100, "PP" : 15
        },
    # "Jump Kick" : {
    #     "name" : "Jump Kick", "nr" : 69, "move_type" : "FIGHTING", "category" : "physical", "TM" : 0, "power" : 100,
    #     "accuracy" : 95, "PP" : 10
    #     },
    "Karate Chop" : {
        "name" : "Karate Chop", "nr" : 70, "move_type" : "FIGHTING", "category" : "physical", "TM" : 0, "power" : 50,
        "accuracy" : 100, "PP" : 25
        },
    "Kinesis" : {
        "name" : "Kinesis", "nr" : 71, "move_type" : "PSYCHIC", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 80, "PP" : 15
        },
    # "Leech Life" : {
    #     "name" : "Leech Life", "nr" : 72, "move_type" : "bug", "category" : "physical", "TM" : 0, "power" : 80,
    #     "accuracy" : 100, "PP" : 10
    #     },
    # "Leech Seed" : {
    #     "name" : "Leech Seed", "nr" : 73, "move_type" : "GRASS", "category" : "status", "TM" : 0, "power" : 0,
    #     "accuracy" : 90, "PP" : 10
    #     },
    "Leer" : {
        "name" : "Leer", "nr" : 74, "move_type" : "NORMAL", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 100, "PP" : 30
        },
    "Lick" : {
        "name" : "Lick", "nr" : 75, "move_type" : "GHOST", "category" : "physical", "TM" : 0, "power" : 30,
        "accuracy" : 100, "PP" : 30
        },
    # "Light Screen" : {
    #     "name" : "Light Screen", "nr" : 76, "move_type" : "PSYCHIC", "category" : "status", "TM" : 0, "power" : 0,
    #     "accuracy" : 0, "PP" : 30
    #     },
    "Lovely Kiss" : {
        "name" : "Lovely Kiss", "nr" : 77, "move_type" : "NORMAL", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 75, "PP" : 10
        },
    # "Low Kick" : {
    #     "name" : "Low Kick", "nr" : 78, "move_type" : "FIGHTING", "category" : "physical", "TM" : 0, "power" : 0,
    #     "accuracy" : 100, "PP" : 20
    #     },
    "Meditate" : {
        "name" : "Meditate", "nr" : 79, "move_type" : "PSYCHIC", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 0, "PP" : 40
        },
    # "Mega Drain" : {
    #     "name" : "Mega Drain", "nr" : 80, "move_type" : "GRASS", "category" : "special", "TM" : 21, "power" : 40,
    #     "accuracy" : 100, "PP" : 15
    #     },
    "Mega Kick" : {
        "name" : "Mega Kick", "nr" : 81, "move_type" : "NORMAL", "category" : "physical", "TM" : 5, "power" : 120,
        "accuracy" : 75, "PP" : 5
        },
    "Mega Punch" : {
        "name" : "Mega Punch", "nr" : 82, "move_type" : "NORMAL", "category" : "physical", "TM" : 1, "power" : 80,
        "accuracy" : 85, "PP" : 20
        },
    # "Metronome" : {
    #     "name" : "Metronome", "nr" : 83, "move_type" : "NORMAL", "category" : "status", "TM" : 35, "power" : 0,
    #     "accuracy" : 0, "PP" : 10
    #     },
    # "Mimic" : {
    #     "name" : "Mimic", "nr" : 84, "move_type" : "NORMAL", "category" : "status", "TM" : 31, "power" : 0,
    #     "accuracy" : 0, "PP" : 10
    #     },
    "Minimize" : {
        "name" : "Minimize", "nr" : 85, "move_type" : "NORMAL", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 0, "PP" : 10
        },
    # "Mirror Move" : {
    #     "name" : "Mirror Move", "nr" : 86, "move_type" : "FLYING", "category" : "status", "TM" : 0, "power" : 0,
    #     "accuracy" : 0, "PP" : 20
    #     },
    # "Mist" : {
    #     "name" : "Mist", "nr" : 87, "move_type" : "ICE", "category" : "status", "TM" : 0, "power" : 0, "accuracy" : 0,
    #     "PP" : 30
    #     },
    "Night Shade" : {
        "name" : "Night Shade", "nr" : 88, "move_type" : "GHOST", "category" : "special", "TM" : 0, "power" : 0,
        "accuracy" : 100, "PP" : 15
        },
    "Pay Day" : {
        "name" : "Pay Day", "nr" : 89, "move_type" : "NORMAL", "category" : "physical", "TM" : 16, "power" : 40,
        "accuracy" : 100, "PP" : 20
        },
    "Peck" : {
        "name" : "Peck", "nr" : 90, "move_type" : "FLYING", "category" : "physical", "TM" : 0, "power" : 35,
        "accuracy" : 100, "PP" : 35
        },
    # "Petal Dance" : {
    #     "name" : "Petal Dance", "nr" : 91, "move_type" : "GRASS", "category" : "special", "TM" : 0, "power" : 120,
    #     "accuracy" : 100, "PP" : 10
    #     },
    "Pin Missile" : {
        "name" : "Pin Missile", "nr" : 92, "move_type" : "BUG", "category" : "physical", "TM" : 0, "power" : 25,
        "accuracy" : 95, "PP" : 20
        },
    "Poison Gas" : {
        "name" : "Poison Gas", "nr" : 93, "move_type" : "POISON", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 90, "PP" : 40
        },
    "Poison Powder" : {
        "name" : "Poison Powder", "nr" : 94, "move_type" : "POISON", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 75, "PP" : 35
        },
    "Poison Sting" : {
        "name" : "Poison Sting", "nr" : 95, "move_type" : "POISON", "category" : "physical", "TM" : 0, "power" : 15,
        "accuracy" : 100, "PP" : 35
        },
    "Pound" : {
        "name" : "Pound", "nr" : 96, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 40,
        "accuracy" : 100, "PP" : 35
        },
    "Psybeam" : {
        "name" : "Psybeam", "nr" : 97, "move_type" : "PSYCHIC", "category" : "special", "TM" : 0, "power" : 65,
        "accuracy" : 100, "PP" : 20
        },
    "Psychic" : {
        "name" : "Psychic", "nr" : 98, "move_type" : "PSYCHIC", "category" : "special", "TM" : 29, "power" : 90,
        "accuracy" : 100, "PP" : 10
        },
    "Psywave" : {
        "name" : "Psywave", "nr" : 99, "move_type" : "PSYCHIC", "category" : "special", "TM" : 46, "power" : 0,
        "accuracy" : 100, "PP" : 15
        },
    # "Quick Attack" : {
    #     "name" : "Quick Attack", "nr" : 100, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 40,
    #     "accuracy" : 100, "PP" : 30
    #     },
    # "Rage" : {
    #     "name" : "Rage", "nr" : 101, "move_type" : "NORMAL", "category" : "physical", "TM" : 20, "power" : 20,
    #     "accuracy" : 100, "PP" : 20
    #     },
    "Razor Leaf" : {
        "name" : "Razor Leaf", "nr" : 102, "move_type" : "GRASS", "category" : "physical", "TM" : 0, "power" : 55,
        "accuracy" : 95, "PP" : 25
        },
    # "Razor Wind" : {
    #     "name" : "Razor Wind", "nr" : 103, "move_type" : "NORMAL", "category" : "special", "TM" : 2, "power" : 80,
    #     "accuracy" : 100, "PP" : 10
    #     },
    # "Recover" : {
    #     "name" : "Recover", "nr" : 104, "move_type" : "NORMAL", "category" : "status", "TM" : 0, "power" : 0,
    #     "accuracy" : 0, "PP" : 5
    #     },
    # "Reflect" : {
    #     "name" : "Reflect", "nr" : 105, "move_type" : "PSYCHIC", "category" : "status", "TM" : 33, "power" : 0,
    #     "accuracy" : 0, "PP" : 20
    #     },
    # "Rest" : {
    #     "name" : "Rest", "nr" : 106, "move_type" : "PSYCHIC", "category" : "status", "TM" : 44, "power" : 0,
    #     "accuracy" : 0, "PP" : 5
    #     },
    # "Roar" : {
    #     "name" : "Roar", "nr" : 107, "move_type" : "NORMAL", "category" : "status", "TM" : 0, "power" : 0,
    #     "accuracy" : 0, "PP" : 20
    #     },
    "Rock Slide" : {
        "name" : "Rock Slide", "nr" : 108, "move_type" : "ROCK", "category" : "physical", "TM" : 48, "power" : 75,
        "accuracy" : 90, "PP" : 10
        },
    "Rock Throw" : {
        "name" : "Rock Throw", "nr" : 109, "move_type" : "ROCK", "category" : "physical", "TM" : 0, "power" : 50,
        "accuracy" : 90, "PP" : 15
        },
    "Rolling Kick" : {
        "name" : "Rolling Kick", "nr" : 110, "move_type" : "FIGHTING", "category" : "physical", "TM" : 0, "power" : 60,
        "accuracy" : 85, "PP" : 15
        },
    "Sand Attack" : {
        "name" : "Sand Attack", "nr" : 111, "move_type" : "GROUND", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 100, "PP" : 15
        },
    "Scratch" : {
        "name" : "Scratch", "nr" : 112, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 40,
        "accuracy" : 100, "PP" : 35
        },
    "Screech" : {
        "name" : "Screech", "nr" : 113, "move_type" : "NORMAL", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 85, "PP" : 40
        },
    "Seismic Toss" : {
        "name" : "Seismic Toss", "nr" : 114, "move_type" : "FIGHTING", "category" : "physical", "TM" : 19, "power" : 0,
        "accuracy" : 100, "PP" : 20
        },
    # "Self-Destruct" : {
    #     "name" : "Self-Destruct", "nr" : 115, "move_type" : "NORMAL", "category" : "physical", "TM" : 36, "power" : 200,
    #     "accuracy" : 100, "PP" : 5
    #     },
    "Sharpen" : {
        "name" : "Sharpen", "nr" : 116, "move_type" : "NORMAL", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 0, "PP" : 30
        },
    "Sing" : {
        "name" : "Sing", "nr" : 117, "move_type" : "NORMAL", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 55, "PP" : 15
        },
    # "Skull Bash" : {
    #     "name" : "Skull Bash", "nr" : 118, "move_type" : "NORMAL", "category" : "physical", "TM" : 40, "power" : 130,
    #     "accuracy" : 100, "PP" : 10
    #     },
    # "Sky Attack" : {
    #     "name" : "Sky Attack", "nr" : 119, "move_type" : "FLYING", "category" : "physical", "TM" : 43, "power" : 140,
    #     "accuracy" : 90, "PP" : 5
    #     },
    "Slam" : {
        "name" : "Slam", "nr" : 120, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 80,
        "accuracy" : 75, "PP" : 20
        },
    "Slash" : {
        "name" : "Slash", "nr" : 121, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 70,
        "accuracy" : 100, "PP" : 20
        },
    "Sleep Powder" : {
        "name" : "Sleep Powder", "nr" : 122, "move_type" : "GRASS", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 75, "PP" : 15
        },
    "Sludge" : {
        "name" : "Sludge", "nr" : 123, "move_type" : "POISON", "category" : "special", "TM" : 0, "power" : 65,
        "accuracy" : 100, "PP" : 20
        },
    "Smog" : {
        "name" : "Smog", "nr" : 124, "move_type" : "POISON", "category" : "special", "TM" : 0, "power" : 30,
        "accuracy" : 70, "PP" : 20
        },
    "Smokescreen" : {
        "name" : "Smokescreen", "nr" : 125, "move_type" : "NORMAL", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 100, "PP" : 20
        },
    # "Soft-Boiled" : {
    #     "name" : "Soft-Boiled", "nr" : 126, "move_type" : "NORMAL", "category" : "status", "TM" : 41, "power" : 0,
    #     "accuracy" : 0, "PP" : 5
    #     },
    # "Solar Beam" : {
    #     "name" : "Solar Beam", "nr" : 127, "move_type" : "GRASS", "category" : "special", "TM" : 22, "power" : 120,
    #     "accuracy" : 100, "PP" : 10
    #     },
    # "Sonic Boom" : {
    #     "name" : "Sonic Boom", "nr" : 128, "move_type" : "NORMAL", "category" : "special", "TM" : 0, "power" : 0,
    #     "accuracy" : 90, "PP" : 20
    #     },
    "Spike Cannon" : {
        "name" : "Spike Cannon", "nr" : 129, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 20,
        "accuracy" : 100, "PP" : 15
        },
    # "Splash" : {
    #     "name" : "Splash", "nr" : 130, "move_type" : "NORMAL", "category" : "status", "TM" : 0, "power" : 0,
    #     "accuracy" : 0, "PP" : 40
    #     },
    "Spore" : {
        "name" : "Spore", "nr" : 131, "move_type" : "GRASS", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 100, "PP" : 15
        },
    "Stomp" : {
        "name" : "Stomp", "nr" : 132, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 65,
        "accuracy" : 100, "PP" : 20
        },
    "Strength" : {
        "name" : "Strength", "nr" : 133, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 80,
        "accuracy" : 100, "PP" : 15
        },
    # "String Shot" : {
    #     "name" : "String Shot", "nr" : 134, "move_type" : "BUG", "category" : "status", "TM" : 0, "power" : 0,
    #     "accuracy" : 95, "PP" : 40
    #     },
    "Struggle" : {
        "name" : "Struggle", "nr" : 135, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 50,
        "accuracy" : 100, "PP" : 100
        },
    "Stun Spore" : {
        "name" : "Stun Spore", "nr" : 136, "move_type" : "GRASS", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 75, "PP" : 30
        },
    # "Submission" : {
    #     "name" : "Submission", "nr" : 137, "move_type" : "FIGHTING", "category" : "physical", "TM" : 17, "power" : 80,
    #     "accuracy" : 80, "PP" : 20
    #     },
    # "Substitute" : {
    #     "name" : "Substitute", "nr" : 138, "move_type" : "NORMAL", "category" : "status", "TM" : 50, "power" : 0,
    #     "accuracy" : 0, "PP" : 10
    #     },
    # "Super Fang" : {
    #     "name" : "Super Fang", "nr" : 139, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 0,
    #     "accuracy" : 90, "PP" : 10
    #     },
    "Supersonic" : {
        "name" : "Supersonic", "nr" : 140, "move_type" : "NORMAL", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 55, "PP" : 20
        },
    # "Surf" : {
    #     "name" : "Surf", "nr" : 141, "move_type" : "WATER", "category" : "special", "TM" : 0, "power" : 90,
    #     "accuracy" : 100, "PP" : 15
    #     },
    # "Swift" : {
    #     "name" : "Swift", "nr" : 142, "move_type" : "NORMAL", "category" : "special", "TM" : 39, "power" : 60,
    #     "accuracy" : 100, "PP" : 20
    #     },
    "Swords Dance" : {
        "name" : "Swords Dance", "nr" : 143, "move_type" : "NORMAL", "category" : "status", "TM" : 3, "power" : 0,
        "accuracy" : 0, "PP" : 20
        },
    "Tackle" : {
        "name" : "Tackle", "nr" : 144, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 40,
        "accuracy" : 100, "PP" : 35
        },
    "Tail Whip" : {
        "name" : "Tail Whip", "nr" : 145, "move_type" : "NORMAL", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 100, "PP" : 30
        },
    # "Take Down" : {
    #     "name" : "Take Down", "nr" : 146, "move_type" : "NORMAL", "category" : "physical", "TM" : 9, "power" : 90,
    #     "accuracy" : 85, "PP" : 20
    #     },
    # "Teleport" : {
    #     "name" : "Teleport", "nr" : 147, "move_type" : "PSYCHIC", "category" : "status", "TM" : 30, "power" : 0,
    #     "accuracy" : 0, "PP" : 20
    #     },
    # "Thrash" : {
    #     "name" : "Thrash", "nr" : 148, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 120,
    #     "accuracy" : 100, "PP" : 10
    #     },
    "Thunder" : {
        "name" : "Thunder", "nr" : 149, "move_type" : "ELECTRIC", "category" : "special", "TM" : 25, "power" : 110,
        "accuracy" : 70, "PP" : 10
        },
    "Thunder Punch" : {
        "name" : "Thunder Punch", "nr" : 150, "move_type" : "ELECTRIC", "category" : "physical", "TM" : 0, "power" : 75,
        "accuracy" : 100, "PP" : 15
        },
    "Thunder Shock" : {
        "name" : "Thunder Shock", "nr" : 151, "move_type" : "ELECTRIC", "category" : "special", "TM" : 0, "power" : 40,
        "accuracy" : 100, "PP" : 30
        },
    "Thunder Wave" : {
        "name" : "Thunder Wave", "nr" : 152, "move_type" : "ELECTRIC", "category" : "status", "TM" : 45, "power" : 0,
        "accuracy" : 90, "PP" : 20
        },
    "Thunderbolt" : {
        "name" : "Thunderbolt", "nr" : 153, "move_type" : "ELECTRIC", "category" : "special", "TM" : 24, "power" : 90,
        "accuracy" : 100, "PP" : 15
        },
    "Toxic" : {
        "name" : "Toxic", "nr" : 154, "move_type" : "POISON", "category" : "status", "TM" : 6, "power" : 0,
        "accuracy" : 90, "PP" : 10
        },
    # "Transform" : {
    #     "name" : "Transform", "nr" : 155, "move_type" : "NORMAL", "category" : "status", "TM" : 0, "power" : 0,
    #     "accuracy" : 0, "PP" : 10
    #     },
    # "Tri Attack" : {
    #     "name" : "Tri Attack", "nr" : 156, "move_type" : "NORMAL", "category" : "special", "TM" : 49, "power" : 80,
    #     "accuracy" : 100, "PP" : 10
    #     },
    # "Twineedle" : {
    #     "name" : "Twineedle", "nr" : 157, "move_type" : "BUG", "category" : "physical", "TM" : 0, "power" : 25,
    #     "accuracy" : 100, "PP" : 20
    #     },
    "Vine Whip" : {
        "name" : "Vine Whip", "nr" : 158, "move_type" : "GRASS", "category" : "physical", "TM" : 0, "power" : 45,
        "accuracy" : 100, "PP" : 25
        },
    "Vise Grip" : {
        "name" : "Vise Grip", "nr" : 159, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 55,
        "accuracy" : 100, "PP" : 30
        },
    "Water Gun" : {
        "name" : "Water Gun", "nr" : 160, "move_type" : "WATER", "category" : "special", "TM" : 12, "power" : 40,
        "accuracy" : 100, "PP" : 25
        },
    "Waterfall" : {
        "name" : "Waterfall", "nr" : 161, "move_type" : "WATER", "category" : "physical", "TM" : 0, "power" : 80,
        "accuracy" : 100, "PP" : 15
        },
    # "Whirlwind" : {
    #     "name" : "Whirlwind", "nr" : 162, "move_type" : "NORMAL", "category" : "status", "TM" : 4, "power" : 0,
    #     "accuracy" : 0, "PP" : 20
    #     },
    "Wing Attack" : {
        "name" : "Wing Attack", "nr" : 163, "move_type" : "FLYING", "category" : "physical", "TM" : 0, "power" : 60,
        "accuracy" : 100, "PP" : 35
        },
    "Withdraw" : {
        "name" : "Withdraw", "nr" : 164, "move_type" : "WATER", "category" : "status", "TM" : 0, "power" : 0,
        "accuracy" : 0, "PP" : 40
        },
    # "Wrap" : {
    #     "name" : "Wrap", "nr" : 165, "move_type" : "NORMAL", "category" : "physical", "TM" : 0, "power" : 15,
    #     "accuracy" : 90, "PP" : 20
    #     },
}

list_of_moves = [key for key in moves_g1]


OPP_ACC_dec_1 = ["Flash", "Kinesis", "Sand Attack", "Smokescreen"]
OPP_ATT_dec_1 = ["Growl", "Aurora Beam"]
OPP_CONFUSION = ["Confuse Ray", "Supersonic", "Confusion", "Dizzy Punch", "Psybeam"]
OPP_DEF_dec_1 = ["Leer", "Tail Whip"]
OPP_DEF_dec_2 = ["Screech"]
OPP_PARLYZ = ["Glare", "Stun Spore", "Thunder Wave", "Body Slam", "Lick", "Thunder", "Thunder Punch", "Thunder Shock",
              "Thunderbolt"]
OPP_POISON = ["Poison Gas", "Poison Powder", "Toxic", "Poison Sting", "Sludge", "Smog"]
OPP_SLEEP = ["Hypnosis", "Lovely Kiss", "Sing", "Sleep Powder", "Spore"]
US_ATT1 = ["Meditate", "Sharpen"]
US_ATT2 = ["Swords Dance"]
US_DEF1 = ["Defense Curl", "Harden", "Withdraw"]
US_DEF2 = ["Acid Armor"]
US_EVAS1 = ["Double Team"]
US_EVAS2 = ["Minimize"]
US_SPCDEF2 = ["Amnesia"]
US_SPEED2 = ["Agility", "Barrier"]
OPP_BURN = ["Ember", "Fire Blast", "Fire Punch", "Flamethrower"]
OPP_FLINCH = ["Bite", "Bone Club", "Headbutt", "Hyper Fang", "Rock Slide", "Rolling Kick", "Stomp", "Waterfall"]
OPP_Freeze = ["Blizzard", "Ice Beam", "Ice Punch"]
OPP_Specdef_dec_1 = ["Acid", "Psychic"]
OPP_Speed_dec_1 = ["Bubble", "Bubble Beam", "Constrict"]
only_lower_HP = ["Cut", "Drill Peck", "Egg Bomb", "Horn Attack", "Hydro Pump", "Mega Kick", "Mega Punch", "Pay Day",
                 "Peck", "Pound", "Rock Throw", "Scratch", "Slam", "Strength", "Tackle", "Vine Whip", "Vise Grip",
                 "Water Gun", "Wing Attack", "Struggle"]
US_CRITICAL = ["Crabhammer", "Karate Chop", "Razor Leaf", "Slash"]
MULTI_HITTER = ["Barrage", "Comet Punch", "Double Slap", "Fury Attack", "Fury Swipes", "Pin Missile", "Spike Cannon"]


fire_moves = [key for key in moves_g1.items() if key[1]["move_type"] == "FIRE"]
poison_moves = [key for key in moves_g1.items() if key[1]["move_type"] == "POISON"]
psychic_moves = [key for key in moves_g1.items() if key[1]["move_type"] == "PSYCHIC"]
ice_moves = [key for key in moves_g1.items() if key[1]["move_type"] == "ICE"]
dark_moves = [key for key in moves_g1.items() if key[1]["move_type"] == "DARK"]
normal_moves = [key for key in moves_g1.items() if key[1]["move_type"] == "NORMAL"]
ground_moves = [key for key in moves_g1.items() if key[1]["move_type"] == "GROUND"]
water_moves = [key for key in moves_g1.items() if key[1]["move_type"] == "WATER"]
ghost_moves = [key for key in moves_g1.items() if key[1]["move_type"] == "GHOST"]
flying_moves = [key for key in moves_g1.items() if key[1]["move_type"] == "FLYING"]
rock_moves = [key for key in moves_g1.items() if key[1]["move_type"] == "ROCK"]
fighting_moves = [key for key in moves_g1.items() if key[1]["move_type"] == "FIGHTING"]
grass_moves = [key for key in moves_g1.items() if key[1]["move_type"] == "GRASS"]
electric_moves = [key for key in moves_g1.items() if key[1]["move_type"] == "ELECTRIC"]

no_effect = ['NORMAL_GHOST', 'ELECTRIC_GROUND', 'FIGHTING_GHOST', 'GROUND_FLYING', 'PSYCHIC_DARK', 'GHOST_NORMAL',
             'DRAGON_FAIRY']
not_very_effective =['NORMAL_ROCK', 'FIRE_FIRE', 'FIRE_WATER', 'FIRE_ROCK', 'FIRE_DRAGON', 'WATER_WATER', 'WATER_GRASS',
                     'WATER_DRAGON', 'ELECTRIC_ELECTRIC', 'ELECTRIC_GRASS', 'ELECTRIC_DRAGON', 'GRASS_FIRE',
                     'GRASS_GRASS', 'GRASS_POISON', 'GRASS_FLYING', 'GRASS_BUG', 'GRASS_DRAGON', 'ICE_FIRE',
                     'ICE_WATER', 'ICE_ICE', 'FIGHTING_POISON', 'FIGHTING_FLYING', 'FIGHTING_PSYCHIC', 'FIGHTING_BUG',
                     'FIGHTING_FAIRY', 'POISON_POISON', 'POISON_GROUND', 'POISON_ROCK', 'POISON_GHOST', 'GROUND_GRASS',
                     'GROUND_BUG', 'FLYING_ELECTRIC', 'FLYING_ROCK', 'PSYCHIC_PSYCHIC', 'BUG_FIRE', "BUG_FIGHTING",
                     "BUG_POISON", "BUG_FLYING", "BUG_GHOST", "BUG_FAIRY", "ROCK_FIGHTING", "ROCK_GROUND", "GHOST_DARK",
                     "DARK_DARK", "DARK_FAIRY", "FAIRY_FIRE", "FAIRY_POISON"]
super_effective = ["FIRE_GRASS", "FIRE_ICE", "FIRE_BUG", "WATER_FIRE", "WATER_GROUND", "WATER_ROCK", "ELECTRIC_WATER",
                   "ELECTRIC_FLYING", "GRASS_WATER", "GRASS_GROUND", "GRASS_ROCK", "ICE_GRASS", "ICE_GROUND",
                   "ICE_FLYING", "ICE_DRAGON", "FIGHTING_NORMAL", "FIGHTING_ICE", "FIGHTING_ROCK", "FIGHTING_DARK",
                   "POISON_GRASS", "POISON_FAIRY", "GROUND_FIRE", "GROUND_ELECTRIC", "GROUND_POISON", "GROUND_ROCK",
                   "FLYING_GRASS", "FLYING_FIGHTING", "FLYING_BUG", "PSYCHIC_FIGHTING", "PSYCHIC_POISON", "BUG_GRASS",
                   "BUG_PSYCHIC", "BUG_DARK", "ROCK_FIRE", "ROCK_ICE", "ROCK_FLYING", "ROCK_BUG", "GHOST_PSYCHIC",
                   "GHOST_GHOST", "DRAGON_DRAGON", "DARK_PSYCHIC", "DARK_GHOST", "FAIRY_FIGHTING", "FAIRY_GHOST",
                   "FAIRY_DARK"]

Potions = ["Fresh water", "Soda pop", "Super Potion", "Lemonade", "Hyper Potion", "Max Potion"]


ITEMS = {
    "Status changers" : {"Antidote" : 7, "Burn heal" : 6, "Ice heal" : 5, "Awaking" : 2, "Parlyz heal" : 3, "Revive" : 12},
    "Potions" : [{"Fresh water" : 30}, {"Soda pop" : 40}, {"Super Potion" : 50}, {"Lemonade" : 60},
                 {"Hyper Potion" : 85}, {"Max Potion" : 300}]
    }

Status_changers = [key for key in ITEMS["Status changers"].keys()]
