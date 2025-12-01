import re 

test_file = r"AOC16\day-07\test.txt"
input_file = r"AOC16\day-07\input.txt"

def part_1(ip):

    supports_tls = 0

    for ip_addr in ip:

        outer = ""
        inner = ""

        flag = 1
        for char in ip_addr:
            if char in "[]":
                flag = 1 - flag
            if flag: outer += char
            else: inner += char

        if (re.search(r"(.)(?!\1)(.)\2\1", outer) and not re.search(r"(.)(?!\1)(.)\2\1", inner)): supports_tls += 1

    return supports_tls

with open(test_file) as f:
    part1_ip = f.read().split("\n\n\n")[0]
    part1_ip, eop = part1_ip.split("\n\n")
    part1_ip = part1_ip.split("\n")
    print("Part - 1: Test")
    print("\nInput:")
    for i in part1_ip: print(i)
    print("\nExpected Output:", eop)
    print("Generated Output:", part_1(part1_ip))
    
with open(input_file) as f:
    print ("\nPart - 1: Main", part_1(f.read().split("\n")))