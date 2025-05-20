test_file = r"AOC\AOC15\day-08\test.txt"
input_file = r"AOC\AOC15\day-08\input.txt"

def part_1(ip):
    extra_char = 0
    i = 0
    while i < len(ip):
        if ip[i] == "\"": extra_char += 1
        elif ip[i] == "\\" and ip[i+1] in ["\"", "\\"]: 
            extra_char += 1
            i += 1
        elif ip[i] == "\\" and ip[i+1] == "x":
            extra_char += 3
            i += 3
        i += 1
    return extra_char

with open(test_file) as f:
    part1_ip = f.read().split("\n\n\n")[0]
    part1_ip, eop = part1_ip.split("\n\n")
    print("Part - 1: Test")
    print("\nInput:")
    print(part1_ip)
    print("\nExpected Output:", eop)
    print("\nGenerated Output:", part_1(part1_ip))
    
with open(input_file) as f:
    part1_ip = f.read()
    print ("\nPart - 1: Main", part_1(part1_ip))