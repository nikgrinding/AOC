test_file = r"AOC15\day-07\test.txt"
input_file = r"AOC15\day-07\input.txt"

def op (a, operation, b):
    if operation == "AND": return a & b
    elif operation == "OR": return a | b
    elif operation == "LSHIFT": return a << b
    else: return a >> b

def part_1(ip):

    vars = dict()

    while ip:
        inst = ip.pop(0)
        lhs, rhs = inst.split(" -> ")
        lhs = lhs.split()
        if len(lhs) == 1:
            if lhs[0].isnumeric(): vars[rhs] = int(lhs[0])
            elif lhs[0] in vars: vars[rhs] = vars[lhs[0]]
        elif len(lhs) == 2:
            if lhs[1].isnumeric(): vars[rhs] = ~int(lhs[1]) & 0xFFFF
            elif lhs[1] in vars: vars[rhs] = ~vars[lhs[1]] & 0xFFFF
        else:
            if lhs[0].isnumeric() and lhs[2].isnumeric(): vars[rhs] = op(int(lhs[0]), lhs[1], int(lhs[2]))
            elif lhs[0].isnumeric() and lhs[2] in vars: vars[rhs] = op(int(lhs[0]), lhs[1], vars[lhs[2]])
            elif lhs[0] in vars and lhs[2].isnumeric(): vars[rhs] = op(vars[lhs[0]], lhs[1], int(lhs[2]))
            elif lhs[0] in vars and lhs[2] in vars: vars[rhs] = op(vars[lhs[0]], lhs[1], vars[lhs[2]])
        if rhs not in vars: ip.append(inst)
    
    return vars

with open(test_file) as f:
    part1_ip, eop = f.read().split("\n\n")
    part1_ip = part1_ip.split("\n")
    eop = eop.split("\n")
    print("Part - 1: Test")
    print("\nInput:")
    for i in part1_ip: print(i)
    print("\nExpected Output:")
    for i in eop: print(i)
    gop = part_1(part1_ip)
    print("\nGenerated Output:")
    for i in sorted(gop):
        print(i, gop[i])
    
with open(input_file) as f:
    part1_ip = f.read().split("\n")
    print ("\nPart - 1: Main", part_1(part1_ip)["a"]) 