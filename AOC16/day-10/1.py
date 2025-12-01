test_file = r"AOC16\day-10\test.txt"
input_file = r"AOC16\day-10\input.txt"

def part_1(ip):

    shld_cmp = [int(i) for i in ip.pop().split()]

    bots = {}

    for inst in ip:
        if "value" in inst:
            split_inst = inst.split()
            bots[" ".join(split_inst[-2:])] = bots.get(" ".join(split_inst[-2:]), []) + [int(split_inst[1])]
            ip.remove(inst)
    
    while ip:
        inst = ip.pop(0)
        split_inst = inst.split()
        if len(bots.get(" ".join(split_inst[:2]), [])) == 2:
            temp = bots[" ".join(split_inst[:2])]
            if temp == shld_cmp or temp == shld_cmp[::-1]: return split_inst[1]
            bots[" ".join(split_inst[:2])] = []
            bots[" ".join(split_inst[5:7])] = bots.get(" ".join(split_inst[5:7]), []) + [min(temp)]
            bots[" ".join(split_inst[-2:])] = bots.get(" ".join(split_inst[-2:]), []) + [max(temp)]
        else: ip.append(inst)

with open(test_file) as f:
    part1_ip, eop = f.read().split("\n\n")
    part1_ip = part1_ip.split("\n")
    print("Part - 1: Test")
    print("\nInput:")
    for i in part1_ip: print(i)
    print("\nExpected Output:", eop)
    print("Generated Output:", part_1(part1_ip))
    
with open(input_file) as f:
    print ("\nPart - 1: Main", part_1(f.read().split("\n")))