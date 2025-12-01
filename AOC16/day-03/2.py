test_file = r"AOC16\day-03\test.txt"
input_file = r"AOC16\day-03\input.txt"

def part_2(ip):

    valid = 0

    for i in range(0, len(ip), 3):
        l = [ip[i], ip[i+1], ip[i+2]]
        l = [[l[b][a] for b in range(3)] for a in range(3)]
        for j in l:
            if j[0]+j[1]>j[2] and j[1]+j[2]>j[0] and j[2]+j[0]>j[1]:  valid += 1
    
    return valid

with open(test_file) as f:
    part2_ip = f.read().split("\n\n\n")[1]
    part2_ip, eop = part2_ip.split("\n\n")
    part2_ip = [[int(j) for j in i.split()] for i in part2_ip.split("\n")]
    print("Part - 2: Test")
    print("\nInput:", part2_ip)
    print("Expected Output:", eop)
    print("Generated Output:", part_2(part2_ip))
    
with open(input_file) as f:
    part2_ip = [[int(j) for j in i.split()] for i in f.read().split("\n")]
    print ("\nPart - 2: Main", part_2(part2_ip))