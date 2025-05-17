import re

test_file = r"AOC\AOC15\day-06\test.txt"
input_file = r"AOC\AOC15\day-06\input.txt"

def part_2(ip):
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for instruction in ip:
        a, x = re.findall(r"\d*,\d*", instruction)
        a, b = [int(i) for i in a.split(",")]
        x, y = [int(i) for i in x.split(",")]
        for i in range(a, x+1):
            for j in range(b, y+1):
                if "on" in instruction: lights[i][j] += 1
                elif "off" in instruction: lights[i][j] = max(lights[i][j]-1, 0)
                else: lights[i][j] += 2
    return sum(sum(i) for i in lights)

with open(test_file) as f:
    part2_ip = f.read().split("\n\n\n")[1]
    part2_ip, eop = part2_ip.split("\n\n")
    part2_ip = part2_ip.split("\n")
    print("Part - 2: Test")
    print("\nInput:", part2_ip)
    print("Expected Output:", eop)
    print("Generated Output:", part_2(part2_ip))
    
with open(input_file) as f:
    part2_ip = f.read().split("\n")
    print ("\nPart - 2: Main", part_2(part2_ip)) 