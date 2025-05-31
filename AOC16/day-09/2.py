test_file = r"AOC\AOC16\day-09\test.txt"
input_file = r"AOC\AOC16\day-09\input.txt"

def part_2(ip):

    if "(" not in ip: return len(ip)

    i = ip.index("(")
    rem = ip[ip.index("("):]
    j = rem.index(")")
    rem = rem[j+1:]

    a, b = [int(i) for i in ip[i+1: i+j].split("x")]

    return i + b * part_2(rem[:a]) + part_2(rem[a:])

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
    print ("\nPart - 2: Main", part_2(f.read()))