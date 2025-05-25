import re

test_file = r"AOC\AOC15\day-22\test.txt"
input_file = r"AOC\AOC15\day-22\input.txt"

def part_2(ip, boss):

    player = {"hp": 50, "mana": 500}
    boss = {"hp": int(boss[0].split(":")[1]) , "damage": int(boss[1].split(":")[1])}

    spells = {}
    for line in ip:
        name = re.match(r"^(.+?) costs (\d+) mana\.", line)
        if not name: continue
        name, cost = name.groups()
        damage, heal, effect = 0, 0, None
        if "instantly does" in line:
            damage = re.search(r"instantly does (\d+) damage", line)
            damage = int(damage.group(1)) if damage else 0
            heal = re.search(r"heals you for (\d+)", line)
            heal = int(heal.group(1)) if heal else 0
        else:
            effect = re.search(r"starts an effect that lasts for (\d+) turns", line)
            effect = (name, int(effect.group(1))) if effect else None
        spells[name] = {"cost": int(cost), "damage": damage, "heal": heal, "effect": effect}
    
    min_mana = [float("inf")]

    def helper (player, boss, effects = {}, mana_spent = 0, history = [], turn = 0):

        if mana_spent >= min_mana[0]: return

        if "Shield" in effects and effects["Shield"] > 0:
            player["armor"] = 7
            effects["Shield"] -= 1
            if effects["Shield"] == 0: player["armor"] = 0
        
        if "Poison" in effects and effects["Poison"] > 0:
            boss["hp"] -= 3
            effects["Poison"] -= 1

        if "Recharge" in effects and effects["Recharge"] > 0:
            player["mana"] += 101
            effects["Recharge"] -= 1
        
        if boss["hp"] <= 0:
            min_mana[0] = min(min_mana[0], mana_spent)
            return
        
        if turn == 0:

            player["hp"] -= 1

            for spell in spells:

                if spells[spell]["effect"] and spells[spell]["effect"][0] in effects and effects[spells[spell]["effect"][0]] > 0: continue
                if player["mana"] < spells[spell]["cost"]: continue

                new_player, new_boss, new_effects, new_history = player.copy(), boss.copy(), effects.copy(), history + [spell]

                new_player["mana"] -= spells[spell]["cost"]
                spent = spells[spell]["cost"] + mana_spent

                new_boss["hp"] -= spells[spell]["damage"]
                new_player["hp"] += spells[spell]["heal"]

                if spells[spell]["effect"]: new_effects[spells[spell]["effect"][0]] = spells[spell]["effect"][1]

                if new_boss["hp"] <= 0:
                    min_mana[0] = min(min_mana[0], spent)
                    continue

                helper(new_player, new_boss, new_effects, spent, new_history, 1-turn)

        else:

            player["hp"] -= max(1, boss["damage"] - (player["armor"] if "armor" in player else 0))
            if player["hp"] > 0: helper(player, boss, effects, mana_spent, history, 1-turn)
        
    helper(player, boss)
    return min_mana[0]

with open(input_file) as f:
    part2_ip, boss = f.read().split("\n\n")
    print ("\nPart - 2: Main", part_2(part2_ip.split("\n"), boss.split("\n")))