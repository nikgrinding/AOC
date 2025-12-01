import hashlib

test_file = r"AOC16\day-05\test.txt"
input_file = r"AOC16\day-05\input.txt"

def part_2(ip):
    i = 0
    pwd = ["_"]*8
    while "_" in pwd:
        hash_ = hashlib.md5((ip+str(i)).encode()).hexdigest()
        if hash_.startswith("00000"):
            if '0' <= hash_[5] <= '7' and pwd[int(hash_[5])] == "_":
                pwd[int(hash_[5])] = hash_[6]
        i += 1
    return "".join(pwd)

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
    part2_ip = f.read()
    print ("\nPart - 2: Main", part_2(part2_ip))