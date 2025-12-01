import re

test_file = r"AOC15\day-05\test.txt"
input_file = r"AOC15\day-05\input.txt"

def part_1(ip):
    pattern = r"a|e|i|o|u"
    rule_1 = len(re.findall(pattern, ip))
    pattern = r"|".join([chr(i)*2 for i in range(97, 123)])
    rule_2 = len(re.findall(pattern, ip))
    pattern = r"ab|cd|pq|xy"
    rule_3 = len(re.findall(pattern, ip))
    return bool(rule_1 >= 3 and rule_2 and not rule_3)

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
    part1_ip = f.read().split("\n")
    result = 0
    for ip in part1_ip:
        if part_1(ip): result += 1
    print ("\nPart - 1: Main", result) 