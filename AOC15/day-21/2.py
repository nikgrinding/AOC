from itertools import combinations

test_file = r"AOC15\day-21\test.txt"
input_file = r"AOC15\day-21\input.txt"

def part_2(ip, weapons, armors, rings):

    def helper (player, boss):
        chance = 0
        while player[0] > 0 and boss[0] > 0:
            if chance == 0: boss[0] -= max(1, player[1] - boss[2])
            else: player[0] -= max(1, boss[1] - player[2])
            chance = 1 - chance
        return boss[0] <= 0

    boss = [int(i.split()[-1]) for i in ip]

    weapons = [[int(j) for j in i.split()[1:]] for i in weapons.split("\n")[1:]]
    armors = [[int(j) for j in i.split()[1:]] for i in armors.split("\n")[1:]]
    rings = [[int(j) for j in i.split()[2:]] for i in rings.split("\n")[1:]]

    possible_weapons = weapons
    possible_armors = [[0, 0, 0]] + armors
    possible_rings = [[0, 0, 0]] + rings + [[comb[0][0]+comb[1][0], comb[0][1]+comb[1][1], comb[0][2]+comb[1][2]] for comb in combinations(rings, 2)]

    max_cost = float("-inf")

    for weapon in possible_weapons:
        for armor in possible_armors:
            for ring in possible_rings:
                cost = weapon[0] + armor[0] + ring[0]
                player_damage = weapon[1] + armor[1] + ring[1]
                player_armor = weapon[2] + armor[2] + ring[2]
                if not helper([100, player_damage, player_armor], [i for i in boss]): max_cost = max(max_cost, cost)
    
    return max_cost
    
with open(input_file) as f:
    part2_ip, boss = f.read().split("\n\n\n")
    weapons, armors, rings = part2_ip.split("\n\n")
    boss = boss.split("\n")
    print ("\nPart - 2: Main", part_2(boss, weapons, armors, rings))