test_file = r"AOC\AOC15\day-23\test.txt"
input_file = r"AOC\AOC15\day-23\input.txt"

def part_2(ip):

    d = {"a": 1, "b": 0}

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
    
with open(input_file) as f:
    part2_ip = f.read().split("\n")
    print ("\nPart - 2: Main", part_2(part2_ip))