import json

test_file = r"AOC\AOC15\day-12\test.txt"
input_file = r"AOC\AOC15\day-12\input.txt"

def part_2(ip):

    ip = json.loads(ip)

    def helper(item):
        if type(item) == int: return item
        elif type(item) == list: return sum([helper(subitem) for subitem in item])
        elif type(item) == dict:
            if "red" in item.values(): return 0
            return sum([helper(subitem) for subitem in item.values()])
        else: return 0

    return helper(ip)

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
    print ("\nPart - 2: Main", part_2(f.read()))