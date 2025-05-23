from itertools import combinations

test_file = r"AOC\AOC15\day-17\test.txt"
input_file = r"AOC\AOC15\day-17\input.txt"

def part_2(ip, eggnog):

    d = {i:0 for i in range(1, len(ip)+1)}
    for n_containers in range(1, len(ip)+1):
        for comb in combinations(ip, n_containers):
            if sum(comb) == eggnog: d[n_containers] += 1
    for i in d:
        if d[i] != 0: return d[i]

with open(test_file) as f:
    part2_ip = f.read().split("\n\n\n\n")[1]
    part2_ip, eop = part2_ip.split("\n\n\n")
    part2_ip, eggnog = part2_ip.split("\n\n")
    part2_ip = [int(i) for i in part2_ip.split("\n")]
    print("Part - 2: Test")
    print("\nInput:", part2_ip)
    print("\nExpected Output:", eop)
    print("Generated Output:", part_2(part2_ip, int(eggnog)))
    
with open(input_file) as f:
    part2_ip, eggnog = f.read().split("\n\n")
    part2_ip = [int(i) for i in part2_ip.split("\n")]
    print ("\nPart - 2: Main", part_2(part2_ip, int(eggnog)))