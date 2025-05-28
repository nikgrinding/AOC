test_file = r"AOC\AOC16\day-02\test.txt"
input_file = r"AOC\AOC16\day-02\input.txt"

def part_2(ip):

    i, j = 2, 0

    num_pad = [[0, 0, 1, 0, 0], [0, 2, 3, 4, 0], [5, 6, 7, 8, 9], [0, "A", "B", "C", 0], [0, 0, "D", 0, 0]]

    pwd = ""

    for command in ip:
        for dir in command:
            if dir == "U": i -= 1 if i > 0 and num_pad[i-1][j] != 0 else 0
            elif dir == "D": i += 1 if i < 4 and num_pad[i+1][j] != 0 else 0
            elif dir == "L": j -= 1 if j > 0 and num_pad[i][j-1] != 0 else 0
            else: j += 1 if j < 4 and num_pad[i][j+1] != 0 else 0
        pwd += str(num_pad[i][j])

    return pwd

with open(test_file) as f:
    part2_ip = f.read().split("\n\n\n")[1]
    part2_ip, eop = part2_ip.split("\n\n")
    part2_ip = part2_ip.split("\n")
    print("Part - 2: Test")
    print("\nInput:", part2_ip)
    print("Expected Output:", eop)
    print("Generated Output:", part_2(part2_ip))
    
with open(input_file) as f:
    print ("\nPart - 2: Main", part_2(f.read().split("\n")))