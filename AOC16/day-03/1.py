test_file = r"AOC\AOC16\day-03\test.txt"
input_file = r"AOC\AOC16\day-03\input.txt"

def part_1(ip):

    valid = 0

    for i in ip:
        if i[0]+i[1]>i[2] and i[1]+i[2]>i[0] and i[2]+i[0]>i[1]:  valid += 1
    
    return valid

with open(test_file) as f:
    part1_ip = f.read().split("\n\n\n")[0]
    part1_ip, eop = part1_ip.split("\n\n")
    part1_ip = [[int(j) for j in i.split()] for i in part1_ip.split("\n")]
    print("Part - 1: Test")
    print("\nInput:", part1_ip)
    print("Expected Output:", eop)
    print("Generated Output:", part_1(part1_ip))
    
with open(input_file) as f:
    part1_ip = [[int(j) for j in i.split()] for i in f.read().split("\n")]
    print ("\nPart - 1: Main", part_1(part1_ip))