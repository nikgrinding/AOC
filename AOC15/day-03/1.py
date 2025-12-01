test_file = r"AOC15\day-03\test.txt"
input_file = r"AOC15\day-03\input.txt"

def part_1(ip):

    curr = [0, 0]

    houses = set()
    houses.add(tuple(curr))

    d = {"^": [0, 1], "v": [0, -1], "<": [1, -1], ">": [1, 1]}

    for dir in ip:
        curr[d[dir][0]] += d[dir][1]
        houses.add(tuple(curr))
        
    return len(houses)

with open(test_file) as f:
    part1_ip = f.read().split("\n\n")[0]
    part1_ip = part1_ip.split("\n")
    print("Part - 1: Test")
    for i in part1_ip:
        ip = i.split()[0]
        print("\nInput:", ip)
        print("Expected Output:", i.split()[1])
        print("Generated Output:", part_1(ip))
    
with open(input_file) as f:
    part1_ip = f.read()
    print ("\nPart - 1: Main", part_1(part1_ip)) 