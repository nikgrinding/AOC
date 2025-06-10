test_file = r"AOC\AOC16\day-12\test.txt"
input_file = r"AOC\AOC16\day-12\input.txt"

def part_1(ip):

    reg = {}

    i = 0

    while i < len(ip):
        inst = ip[i]
        if "cpy" in inst:
            _, reg_a, reg_b = inst.split()
            if reg_a.isnumeric(): reg[reg_b] = int(reg_a)
            else: reg[reg_b] = reg[reg_a]
        elif "inc" in inst: reg[inst.split()[-1]] += 1
        elif "dec" in inst: reg[inst.split()[-1]] -= 1
        else:
            if (inst.split()[1].isnumeric() and int(inst.split()[1]) != 0) or reg.get(inst.split()[1], 0) != 0: i += int(inst.split()[-1]) - 1
        i += 1
    
    return reg["a"]

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