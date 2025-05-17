import re

test_file = r"AOC\AOC15\day-05\test.txt"
input_file = r"AOC\AOC15\day-05\input.txt"

def part_2(ip):
    pattern = r"(..).*\1"
    rule_1 = len(re.findall(pattern, ip))
    pattern = r"(.).\1"
    rule_2 = len(re.findall(pattern, ip))
    return bool(rule_1 and rule_2)

with open(test_file) as f:
    part2_ip = f.read().split("\n\n")[1]
    part2_ip = part2_ip.split("\n")
    print("Part - 2: Test")
    for i in part2_ip:
        ip = i.split()[0]
        print("\nInput:", ip)
        print("Expected Output:", i.split()[1])
        print("Generated Output:", part_2(ip))
    
with open(input_file) as f:
    part2_ip = f.read().split("\n")
    result = 0
    for ip in part2_ip:
        if part_2(ip): result += 1
    print ("\nPart - 2: Main", result) 