test_file = r"AOC15\day-14\test.txt"
input_file = r"AOC15\day-14\input.txt"

def part_2(ip, time):

    reindeer = [[int(i.split()[3]), int(i.split()[6]), int(i.split()[-2])]  for i in ip]
    
    def helper(reindeer, time): return [i[0] * (i[1] * (time // (i[1]+i[2])) + min(time % (i[1]+i[2]), i[1])) for i in reindeer]
    
    dist = [helper(reindeer, i) for i in range(1, time+1)]

    d = {i: 0 for i in range(len(reindeer))}
    
    for i in dist:
        for index in range(len(i)):
            if i[index] == max(i): d[index] += 1
    
    return max(d.values())

with open(test_file) as f:
    part2_ip = f.read().split("\n\n\n")[1]
    part2_ip, eop = part2_ip.split("\n\n")
    part2_ip = part2_ip.split("\n")
    part2_ip, time = part2_ip[:-1], part2_ip[-1]
    print("Part - 2: Test")
    print("\nInput:\n")
    for i in part2_ip: print(i)
    print("\nExpected Output:", eop)
    print("Generated Output:", part_2(part2_ip, int(time)))
    
with open(input_file) as f:
    part2_ip = f.read().split("\n")
    part2_ip, time = part2_ip[:-1], part2_ip[-1]
    print ("\nPart - 2: Main", part_2(part2_ip, int(time)))