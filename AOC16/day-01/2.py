test_file = r"AOC16\day-01\test.txt"
input_file = r"AOC16\day-01\input.txt"

def part_2(ip):

    dir_map = {"N": {"R": "E", "L": "W"}, "E": {"R": "S", "L": "N"}, "S": {"R": "W", "L": "E"}, "W": {"R": "N", "L": "S"}}

    dir = "N"

    x = y = 0

    visited = set()
    visited.add((0, 0))
    
    for i in ip:
        dir, dist = dir_map[dir][i[0]], int(i[1:])
        if dir == "N": 
            for j in range(y+1, y+dist+1): 
                if (x, j) in visited: return abs(x) + abs(j)
                visited.add((x,j))
            y += dist
        elif dir == "S":
            for j in range(y-1, y-dist-1, -1):
                if (x, j) in visited: return abs(x) + abs(j)
                visited.add((x,j))
            y -= dist
        elif dir == "E":
            for j in range(x+1, x+dist+1):
                if (j, y) in visited: return abs(j) + abs(y)
                visited.add((j,y))
            x += dist
        else:
            for j in range(x-1, x-dist-1, -1):
                if (j, y) in visited: return abs(j) + abs(y)
                visited.add((j,y))
            x -= dist

with open(test_file) as f:
    part2_ip = f.read().split("\n\n")[1]
    part2_ip = part2_ip.split("\n")
    print("Part - 2: Test")
    for i in part2_ip:
        ip = i.replace(",", "").split()[:-1]
        print("\nInput:", ip)
        print("Expected Output:", i.split()[-1])
        print("Generated Output:", part_2(ip))
    
with open(input_file) as f:
    print ("\nPart - 2: Main", part_2(f.read().split(", ")))