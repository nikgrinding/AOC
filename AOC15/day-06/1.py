import re

test_file = r"AOC15\day-06\test.txt"
input_file = r"AOC15\day-06\input.txt"

def part_1(ip):
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for instruction in ip:
        a, x = re.findall(r"\d*,\d*", instruction)
        a, b = [int(i) for i in a.split(",")]
        x, y = [int(i) for i in x.split(",")]
        for i in range(a, x+1):
            for j in range(b, y+1):
                if "on" in instruction: lights[i][j] = 1
                elif "off" in instruction: lights[i][j] = 0
                else: lights[i][j] = 1 - lights[i][j]
    return sum(sum(i) for i in lights)

with open(test_file) as f:
    part1_ip = f.read().split("\n\n\n")[0]
    part1_ip, eop = part1_ip.split("\n\n")
    part1_ip = part1_ip.split("\n")
    print("Part - 1: Test")
    print("\nInput:", part1_ip)
    print("Expected Output:", eop)
    print("Generated Output:", part_1(part1_ip))
    
with open(input_file) as f:
    part1_ip = f.read().split("\n")
    print ("\nPart - 1: Main", part_1(part1_ip)) 