from collections import deque

test_file = r"AOC\AOC16\day-13\test.txt"
input_file = r"AOC\AOC16\day-13\input.txt"

def part_2(target, offset):
    
    def is_open_space(x, y):
        if x < 0 or y < 0: return False
        return bin(x*x + 3*x + 2*x*y + y + y*y + offset).count("1") % 2 == 0
    
    visited = set()
    queue = deque([((1, 1), 0)])
    while queue:
        (x, y), steps = queue.popleft()
        if steps == 50: return len(visited)
        for i, j in [(-1,0), (1,0), (0,-1), (0,1)]:
            new_x, new_y = x + i, y + j
            if (new_x, new_y) not in visited and is_open_space(new_x, new_y):
                visited.add((new_x, new_y))
                queue.append(((new_x, new_y), steps + 1))
    
with open(input_file) as f:
    part2_ip = f.read().split("\n")
    print ("\nPart - 2: Main", part_2([int(i) for i in part2_ip[0].split(",")], int(part2_ip[1])))