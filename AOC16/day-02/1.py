test_file = r"AOC16\day-02\test.txt"
input_file = r"AOC16\day-02\input.txt"

def part_1(ip):

    i, j = 1, 1

    num_pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    pwd = ""

    for command in ip:
        for dir in command:
            if dir == "U": i -= 1 if i > 0 else 0
            elif dir == "D": i += 1 if i < 2 else 0
            elif dir == "L": j -= 1 if j > 0 else 0
            else: j += 1 if j < 2 else 0
        pwd += str(num_pad[i][j])

    return pwd

with open(test_file) as f:
    part1_ip = f.read().split("\n\n\n")[0]
    part1_ip, eop = part1_ip.split("\n\n")
    part1_ip = part1_ip.split("\n")
    print("Part - 1: Test")
    print("\nInput:", part1_ip)
    print("Expected Output:", eop)
    print("Generated Output:", part_1(part1_ip))
    
with open(input_file) as f:
    print ("\nPart - 1: Main", part_1(f.read().split("\n")))