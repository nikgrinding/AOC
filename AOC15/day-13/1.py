from itertools import permutations

test_file = r"AOC\AOC15\day-13\test.txt"
input_file = r"AOC\AOC15\day-13\input.txt"

def part_1(ip):
    ppl = sorted(set(i.split()[0] for i in ip))
    M = [[0]*len(ppl) for _ in range(len(ppl))]
    sign = {"gain": 1, "lose": -1}
    for i in ip: M[ppl.index(i.split()[0])][ppl.index(i.split()[-1][:-1])] = int(i.split()[3]) * sign[i.split()[2]]
    happiness = 0
    for perm in permutations(ppl):
        l = list(perm) + [perm[0]]
        happiness = max(sum(M[ppl.index(l[i])][ppl.index(l[i+1])] for i in range(len(ppl))) + sum(M[ppl.index(l[i+1])][ppl.index(l[i])] for i in range(len(ppl))), happiness)
    return happiness

with open(test_file) as f:
    part1_ip, eop = f.read().split("\n\n")
    part1_ip = part1_ip.split("\n")
    print("Part - 1: Test")
    print("\nInput:\n")
    for i in part1_ip: print(i)
    print("\nExpected Output:", eop)
    print("Generated Output:", part_1(part1_ip))
    
with open(input_file) as f:
    part1_ip = f.read().split("\n")
    print ("\nPart - 1: Main", part_1(part1_ip))