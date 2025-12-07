test_file = r"AOC25\day-07\test.txt"
input_file = r"AOC25\day-07\input.txt"

def part_2(ip):
    ip = [list(i) for i in ip]
    source_x = 0
    source_y = ip[0].index('S')
    visited = dict()
    def helper(x, y):
        if not (0 <= x < len(ip) and 0 <= y < len(ip[0])):
            return 1
        if (x, y) in visited:
            return visited[(x, y)]
        count = 0
        if ip[x][y] != '^':
            count += helper(x+1, y)
        else:
            count += helper(x, y-1) + helper(x, y+1)
        visited[(x, y)] = count
        return count
    return helper(source_x, source_y)

with open(test_file) as f:
    part_2_ip, part_2_op = f.read().split('\n\n\n')[1].split('\n\n')
    part_2_ip = part_2_ip.split("\n")
    print("Part - 2: Test")
    print("\nInput:")
    for i in part_2_ip:
        print(i)
    print("Expected Output:", part_2_op)
    print("Generated Output:", part_2(part_2_ip))
    
with open(input_file) as f:
    print ("\nPart - 2: Main", part_2(f.read().split("\n")))