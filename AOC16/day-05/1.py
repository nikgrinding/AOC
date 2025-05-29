import hashlib

test_file = r"AOC\AOC16\day-05\test.txt"
input_file = r"AOC\AOC16\day-05\input.txt"

def part_1(ip):
    i = 0
    pwd = ""
    while len(pwd) < 8:
        hash_ = hashlib.md5((ip+str(i)).encode()).hexdigest()
        if hash_.startswith("00000"):
            pwd += hash_[5]
        i += 1
    return pwd

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