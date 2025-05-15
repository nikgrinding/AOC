test_file = r"AOC\AOC15\day-01\test.txt"
input_file = r"AOC\AOC15\day-01\input.txt"

def part_2(ip):
    counter = 0
    for index, bracket in enumerate(ip):
        if bracket == "(": counter += 1
        else: counter -= 1
        if counter < 0: return index + 1

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