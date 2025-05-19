test_file = r"AOC\AOC15\day-07\test.txt"
input_file = r"AOC\AOC15\day-07\input.txt"

def op (a, operation, b):
    if operation == "AND": return a & b
    elif operation == "OR": return a | b
    elif operation == "LSHIFT": return a << b
    else: return a >> b

def part_2(ip, b = 0):

    vars = dict()
    if b: 
        vars["b"] = b
        ip = [i for i in ip if not i.endswith("-> b")]

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
    
with open(input_file) as f:
    part2_ip = f.read().split("\n")
    b = part_2(part2_ip.copy())["a"]
    print ("\nPart - 2: Main", part_2(part2_ip, b)["a"]) 