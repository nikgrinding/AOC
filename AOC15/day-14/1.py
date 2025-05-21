test_file = r"AOC\AOC15\day-14\test.txt"
input_file = r"AOC\AOC15\day-14\input.txt"

def part_1(ip, time):
    reindeer = [[int(i.split()[3]), int(i.split()[6]), int(i.split()[-2])]  for i in ip]
    l = [i[0] * (i[1] * (time // (i[1]+i[2])) + min(time % (i[1]+i[2]), i[1])) for i in reindeer]
    return max(l)

with open(test_file) as f:
    part1_ip = f.read().split("\n\n\n")[0]
    part1_ip, eop = part1_ip.split("\n\n")
    part1_ip = part1_ip.split("\n")
    part1_ip, time = part1_ip[:-1], part1_ip[-1]
    print("Part - 1: Test")
    print("\nInput:\n")
    for i in part1_ip: print(i)
    print("\nExpected Output:", eop)
    print("Generated Output:", part_1(part1_ip, int(time)))
    
with open(input_file) as f:
    part1_ip = f.read().split("\n")
    part1_ip, time = part1_ip[:-1], part1_ip[-1]
    print ("\nPart - 1: Main", part_1(part1_ip, int(time)))