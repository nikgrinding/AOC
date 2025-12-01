test_file = r"AOC15\day-08\test.txt"
input_file = r"AOC15\day-08\input.txt"

def part_2(ip):
    extra_char = 0
    for i in ip.split("\n"):
        extra_char += 2
        for j in i:
            if j in ["\"", "\\"]: extra_char += 1
    return extra_char 

with open(test_file) as f:
    part2_ip = f.read().split("\n\n\n")[1]
    part2_ip, eop = part2_ip.split("\n\n")
    print("Part - 2: Test")
    print("\nInput:")
    print(part2_ip)
    print("\nExpected Output:", eop)
    print("\nGenerated Output:", part_2(part2_ip))
    
with open(input_file) as f:
    part2_ip = f.read()
    print ("\nPart - 2: Main", part_2(part2_ip))