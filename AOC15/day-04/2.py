import hashlib

test_file = r"AOC\AOC15\day-04\test.txt"
input_file = r"AOC\AOC15\day-04\input.txt"

def part_2(ip):
    i = 0
    while True:
        if hashlib.md5((ip+str(i)).encode()).hexdigest().startswith("000000"):
            return i
        i += 1
    
with open(input_file) as f:
    part2_ip = f.read()
    print ("\nPart - 2: Main", part_2(part2_ip))