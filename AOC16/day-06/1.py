test_file = r"AOC16\day-06\test.txt"
input_file = r"AOC16\day-06\input.txt"

def part_1(ip):

    l = [{} for _ in range(len(ip[0]))]

    for string in ip:
        for i in range(len(string)):
            l[i][string[i]] = l[i].get(string[i], 0) + 1
    
    msg = ""
    for position in l:
        for char in position:
            if position[char] == max(position.values()):
                msg += char
                break

    return msg

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