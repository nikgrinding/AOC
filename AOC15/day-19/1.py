import re

test_file = r"AOC15\day-19\test.txt"
input_file = r"AOC15\day-19\input.txt"

def part_1(ip, molecule):
    
    possible_molecules = set()

    d = {}
    for i in ip:
        lhs, rhs = i.split(" => ")
        if lhs in d: d[lhs].append(rhs)
        else: d[lhs] = [rhs]

    for i in d:
        for j in d[i]:
            for k in re.finditer(i, molecule): possible_molecules.add(molecule[:k.span()[0]] + j + molecule[k.span()[1]:])
    
    return len(possible_molecules)

with open(test_file) as f:
    part1_ip = f.read().split("\n\n\n\n\n")[0]
    part1_ip = part1_ip.split("\n\n\n\n")
    print("Part - 1: Test")
    for i in part1_ip:
        ip, eop = i.split("\n\n\n")
        ip, molecule = ip.split("\n\n")
        ip = ip.split("\n")
        print("\nInput:")
        for i in ip: print(i)
        print("Expected Output:", eop)
        print("Generated Output:", part_1(ip, molecule))
    
with open(input_file) as f:
    part1_ip, molecule = f.read().split("\n\n")
    part1_ip = part1_ip.split("\n")
    print ("\nPart - 1: Main", part_1(part1_ip, molecule)) 