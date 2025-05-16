test_file = r"AOC\AOC15\day-03\test.txt"
input_file = r"AOC\AOC15\day-03\input.txt"

def part_2(ip):

    curr_1, curr_2 = [0, 0], [0, 0]

    houses = set()
    houses.add(tuple(curr_1))

    d = {"^": [0, 1], "v": [0, -1], "<": [1, -1], ">": [1, 1]}

    for index in range(len(ip)):
        if index % 2 == 0:
            curr_1[d[ip[index]][0]] += d[ip[index]][1]
            if index + 1 < len(ip): 
                curr_2[d[ip[index+1]][0]] += d[ip[index+1]][1]
            houses.add(tuple(curr_1))
            houses.add(tuple(curr_2))

    return len(houses)

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