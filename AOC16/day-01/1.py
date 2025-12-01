test_file = r"AOC16\day-01\test.txt"
input_file = r"AOC16\day-01\input.txt"

def part_1(ip):

    dir_map = {"N": {"R": "E", "L": "W"}, "E": {"R": "S", "L": "N"}, "S": {"R": "W", "L": "E"}, "W": {"R": "N", "L": "S"}}

    dir = "N"

    x = y = 0
    
    for i in ip:
        dir, dist = dir_map[dir][i[0]], int(i[1:])
        if dir == "N": y += dist
        elif dir == "S": y -= dist
        elif dir == "E": x += dist
        else: x -= dist
    
    return abs(x) + abs(y)

with open(test_file) as f:
    part1_ip = f.read().split("\n\n")[0]
    part1_ip = part1_ip.split("\n")
    print("Part - 1: Test")
    for i in part1_ip:
        ip = i.replace(",", "").split()[:-1]
        print("\nInput:", ip)
        print("Expected Output:", i.split()[-1])
        print("Generated Output:", part_1(ip))
    
with open(input_file) as f:
    print ("\nPart - 1: Main", part_1(f.read().split(", ")))