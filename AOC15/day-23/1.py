test_file = r"AOC15\day-23\test.txt"
input_file = r"AOC15\day-23\input.txt"

def part_1(ip):

    d = {"a": 0, "b": 0}

    i = 0
    while i < len(ip):
        inst = ip[i]
        if "hlf" in inst: d[inst.split()[-1]] //= 2
        elif "tpl" in inst: d[inst.split()[-1]] *= 3
        elif "inc" in inst: d[inst.split()[-1]] += 1
        elif "jmp" in inst: i += int(inst.split()[-1])-1
        elif "jie" in inst: i += int(inst.split()[-1])-1 if d[inst[4]] % 2 == 0 else 0
        else: i += int(inst.split()[-1])-1 if d[inst[4]] == 1 else 0
        i += 1
    
    return d["a"], d["b"]

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