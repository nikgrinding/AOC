import re 

test_file = r"AOC16\day-07\test.txt"
input_file = r"AOC16\day-07\input.txt"

def part_2(ip):

    supports_ssl = 0

    for ip_addr in ip:

        outer = ""
        inner = ""

        flag = 1
        for char in ip_addr:
            if char in "[]":
                flag = 1 - flag
            if flag: outer += char
            else: inner += char

        for sequence in set(i.group(1) for i in re.finditer(r'(?=((.).\2))', outer)):
            if re.search(sequence[1]+sequence[0]+sequence[1], inner):
                supports_ssl += 1
                break

    return supports_ssl

with open(test_file) as f:
    part2_ip = f.read().split("\n\n\n")[1]
    part2_ip, eop = part2_ip.split("\n\n")
    part2_ip = part2_ip.split("\n")
    print("Part - 2: Test")
    print("\nInput:")
    for i in part2_ip: print(i)
    print("\nExpected Output:", eop)
    print("Generated Output:", part_2(part2_ip))
    
with open(input_file) as f:
    print ("\nPart - 2: Main", part_2(f.read().split("\n")))