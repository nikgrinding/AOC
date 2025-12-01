from itertools import combinations

test_file = r"AOC15\day-24\test.txt"
input_file = r"AOC15\day-24\input.txt"

def part_2(ip):

    valid_grp1 = []

    for i in range(len(ip)):
        for comb in combinations(ip, i):
            if sum(comb) == sum(ip)//4: valid_grp1.append(comb)
        if valid_grp1: break

    def helper(grp):
        prod = 1
        for i in grp: prod *= i
        return prod
    
    return helper(sorted(valid_grp1, key = helper)[0])

with open(test_file) as f:
    part2_ip = f.read().split("\n\n\n")[1]
    part2_ip, eop = part2_ip.split("\n\n")
    part2_ip = [int(i) for i in part2_ip.split("\n")]
    print("Part - 2: Test")
    print("\nInput:", part2_ip)
    print("\nExpected Output:", eop)
    print("Generated Output:", part_2(part2_ip))
    
with open(input_file) as f:
    part2_ip = f.read()
    part2_ip = [int(i) for i in part2_ip.split("\n")]
    print ("\nPart - 2: Main", part_2(part2_ip))