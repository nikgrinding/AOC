import hashlib, re

test_file = r"AOC\AOC16\day-14\test.txt"
input_file = r"AOC\AOC16\day-14\input.txt"

def part_1(ip):

    hashes = []

    for i in range(1000): hashes.append(hashlib.md5((ip+str(i)).encode()).hexdigest())
    
    count = 0
    i = 0
    while count < 64:
        hashes.append(hashlib.md5((ip+str(i+1000)).encode()).hexdigest())
        match_3 = re.search(r"(.)\1\1", hashes[i])
        if match_3:
            for j in range(i+1, i+1+1000):
                if match_3.group(1)*5 in hashes[j]: count += 1
        i += 1
    return i - 1

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