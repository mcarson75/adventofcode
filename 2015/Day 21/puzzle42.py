from itertools import combinations

# Opponent's beginning
# Hit Points: 103
# Damage: 9
# Armor: 2
#
# Player's beginning
# Hit Points: 100
# Damage: 0
# Armor: 0
#
# Weapons:    Cost  Damage  Armor
# Dagger        8     4       0
# Shortsword   10     5       0
# Warhammer    25     6       0
# Longsword    40     7       0
# Greataxe     74     8       0

# Armor:      Cost  Damage  Armor
# Leather      13     0       1
# Chainmail    31     0       2
# Splintmail   53     0       3
# Bandedmail   75     0       4
# Platemail   102     0       5

# Rings:      Cost  Damage  Armor
# Damage +1    25     1       0
# Damage +2    50     2       0
# Damage +3   100     3       0
# Defense +1   20     0       1
# Defense +2   40     0       2
# Defense +3   80     0       3

weapons = [{"cost" : 8,   "damage" : 4, "armor" : 0, "name" : "Dagger"},
           {"cost" : 10,  "damage" : 5, "armor" : 0, "name" : "Shortsword"},
           {"cost" : 25,  "damage" : 6, "armor" : 0, "name" : "Warhammer"},
           {"cost" : 40,  "damage" : 7, "armor" : 0, "name" : "Longsword"},
           {"cost" : 74,  "damage" : 8, "armor" : 0, "name" : "Greataxe"}]
armor =   [{"cost" : 0,   "damage" : 0, "armor" : 0, "name" : "None"},
           {"cost" : 13,  "damage" : 0, "armor" : 1, "name" : "Leather"},
           {"cost" : 31,  "damage" : 0, "armor" : 2, "name" : "Chainmail"},
           {"cost" : 53,  "damage" : 0, "armor" : 3, "name" : "Splintmail"},
           {"cost" : 75,  "damage" : 0, "armor" : 4, "name" : "Bandedmail"},
           {"cost" : 102, "damage" : 0, "armor" : 5, "name" : "Platemail"}]
rings =   [{"cost" : 0,   "damage" : 0, "armor" : 0, "name" : "None"},
           {"cost" : 0,   "damage" : 0, "armor" : 0, "name" : "None"},
           {"cost" : 25,  "damage" : 1, "armor" : 0, "name" : "Damage +1"},
           {"cost" : 50,  "damage" : 2, "armor" : 0, "name" : "Damage +2"},
           {"cost" : 100, "damage" : 3, "armor" : 0, "name" : "Damage +3"},
           {"cost" : 20,  "damage" : 0, "armor" : 1, "name" : "Defense +1"},
           {"cost" : 40,  "damage" : 0, "armor" : 2, "name" : "Defense +2"},
           {"cost" : 80,  "damage" : 0, "armor" : 3, "name" : "Defense +3"}]

boss = {"hit": 103, "damage": 9, "armor": 2}

def player_wins(damage, armor):
    b = 103
    p = 100
    while True:
        b -= max(1, damage - 2)
        if b <= 0: return True
        p -= max(1, 9 - armor)
        if p <= 0: return False

max_cost = 0

#winning_combo = {"weapon" : None, "armor" : None, "ring" : None}
for w in weapons:
    for a in armor:
        for r1, r2 in combinations(rings, 2):
            cost = w["cost"] + a["cost"] + r1["cost"] + r2["cost"]
            dam = w["damage"] + a["damage"] + r1["damage"] + r2["damage"]
            arm = w["armor"] + a["armor"] + r1["armor"] + r2["armor"]
            if not player_wins(dam, arm) and cost > max_cost:
                max_cost = cost
                winning_combo = {"weapon" : w["name"], "armor" : a["name"], "ring1" : r1["name"], "ring2" : r2["name"]}
    

print(winning_combo)
print(max_cost)