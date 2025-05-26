from itertools import combinations

test_file = r"AOC\AOC15\day-24\test.txt"
input_file = r"AOC\AOC15\day-24\input.txt"

def part_1(ip):

    valid_grp1 = []

    for i in range(len(ip)):
        for comb in combinations(ip, i):
            if sum(comb) == sum(ip)//3: valid_grp1.append(comb)
        if valid_grp1: break

    def helper(grp):
        prod = 1
        for i in grp: prod *= i
        return prod
    
    return helper(sorted(valid_grp1, key = helper)[0])

with open(test_file) as f:
    part1_ip = f.read().split("\n\n\n")[0]
    part1_ip, eop = part1_ip.split("\n\n")
    part1_ip = [int(i) for i in part1_ip.split("\n")]
    print("Part - 1: Test")
    print("\nInput:", part1_ip)
    print("\nExpected Output:", eop)
    print("Generated Output:", part_1(part1_ip))
    
with open(input_file) as f:
    part1_ip = f.read()
    part1_ip = [int(i) for i in part1_ip.split("\n")]
    print ("\nPart - 1: Main", part_1(part1_ip))