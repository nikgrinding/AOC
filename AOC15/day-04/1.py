import hashlib

test_file = r"AOC\AOC15\day-04\test.txt"
input_file = r"AOC\AOC15\day-04\input.txt"

def part_1(ip):
    i = 0
    while True:
        if hashlib.md5((ip+str(i)).encode()).hexdigest().startswith("00000"):
            return i
        i += 1

with open(test_file) as f:
    part1_ip = f.read().split("\n")
    print("Part - 1: Test")
    for i in part1_ip:
        ip = i.split()[0]
        print("\nInput:", ip)
        print("Expected Output:", i.split()[1])
        print("Generated Output:", part_1(ip))
    
with open(input_file) as f:
    part1_ip = f.read()
    print ("\nPart - 1: Main", part_1(part1_ip))