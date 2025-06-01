test_file = r"AOC\AOC16\day-10\test.txt"
input_file = r"AOC\AOC16\day-10\input.txt"

def part_2(ip):

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
            bots[" ".join(split_inst[:2])] = []
            bots[" ".join(split_inst[5:7])] = bots.get(" ".join(split_inst[5:7]), []) + [min(temp)]
            bots[" ".join(split_inst[-2:])] = bots.get(" ".join(split_inst[-2:]), []) + [max(temp)]
        else: ip.append(inst)
    
    return bots["output 0"][0]*bots["output 1"][0]*bots["output 2"][0]
    
with open(input_file) as f:
    print ("\nPart - 2: Main", part_2(f.read().split("\n")))