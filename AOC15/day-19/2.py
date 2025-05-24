import random

test_file = r"AOC\AOC15\day-19\test.txt"
input_file = r"AOC\AOC15\day-19\input.txt"

def part_2(ip, molecule):

    d = {i.split(" => ")[1]: i.split(" => ")[0] for i in ip}
    
    steps = 0

    temp = molecule
    while temp != "e":
        for i in d:
            if i in temp:
                temp = temp.replace(i, d[i], 1)
                steps += 1
                break
        else:
            temp = molecule
            steps = 0
            items = list(d.items())
            random.shuffle(items)
            d = dict(items)

    return steps

with open(test_file) as f:
    part2_ip = f.read().split("\n\n\n\n\n")[1]
    part2_ip = part2_ip.split("\n\n\n\n")
    print("Part - 2: Test")
    for i in part2_ip:
        ip, eop = i.split("\n\n\n")
        ip, molecule = ip.split("\n\n")
        ip = ip.split("\n")
        print("\nInput:")
        for i in ip: print(i)
        print("Expected Output:", eop)
        print("Generated Output:", part_2(ip, molecule))
    
with open(input_file) as f:
    part2_ip, molecule = f.read().split("\n\n")
    part2_ip = part2_ip.split("\n")
    print ("\nPart - 2: Main", part_2(part2_ip, molecule))