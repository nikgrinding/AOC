test_file = r"AOC25\day-07\test.txt"
input_file = r"AOC25\day-07\input.txt"

def part_1(ip):
    ip = [list(i) for i in ip]
    source_x = 0
    source_y = ip[0].index('S')
    visited = set()
    def helper(x, y):
        if not (0 <= x < len(ip) and 0 <= y < len(ip[0])):
            return 0
        if (x, y) in visited:
            return 0
        visited.add((x, y))
        if ip[x][y] != '^':
            return helper(x+1, y)
        return 1 + helper(x, y-1) + helper(x, y+1)
    return helper(source_x, source_y)

with open(test_file) as f:
    part_1_ip, part_1_op = f.read().split('\n\n\n')[0].split('\n\n')
    part_1_ip = part_1_ip.split("\n")
    print("Part - 1: Test")
    print("\nInput:")
    for i in part_1_ip:
        print(i)
    print("Expected Output:", part_1_op)
    print("Generated Output:", part_1(part_1_ip))
    
with open(input_file) as f:
    print ("\nPart - 1: Main", part_1(f.read().split("\n")))