test_file = r"AOC16\day-06\test.txt"
input_file = r"AOC16\day-06\input.txt"

def part_2(ip):

    l = [{} for _ in range(len(ip[0]))]

    for string in ip:
        for i in range(len(string)):
            l[i][string[i]] = l[i].get(string[i], 0) + 1
    
    msg = ""
    for position in l:
        for char in position:
            if position[char] == min(position.values()):
                msg += char
                break

    return msg

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