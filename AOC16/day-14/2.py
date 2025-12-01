import hashlib, re

test_file = r"AOC16\day-14\test.txt"
input_file = r"AOC16\day-14\input.txt"

def part_2(ip):

    hashes = []

    def helper(hash_):
        for _ in range(2017): hash_ = hashlib.md5(hash_.encode()).hexdigest()
        return hash_

    for i in range(1000): hashes.append(helper(ip+str(i)))
    
    count = 0
    i = 0
    while count < 64:
        hashes.append(helper(ip+str(i+1000)))
        match_3 = re.search(r"(.)\1\1", hashes[i])
        if match_3:
            for j in range(i+1, i+1+1000):
                if match_3.group(1)*5 in hashes[j]: count += 1
        i += 1
    return i - 1

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