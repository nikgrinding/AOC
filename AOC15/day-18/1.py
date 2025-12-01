test_file = r"AOC15\day-18\test.txt"
input_file = r"AOC15\day-18\input.txt"

def part_1(ip, steps):
    lights = [[j for j in i] for i in ip]

    def helper(r, c):
        neighbors = [lights[i][j] if 0 <= i < len(lights) and 0 <= j < len(lights[0]) else "." for i in range(r-1, r+2) for j in range(c-1, c+2)]
        return neighbors.count("#") if lights[r][c] == "." else neighbors.count("#") - 1
    
    temp = [[j for j in i] for i in lights]
    for _ in range(steps):
        for i in range(len(temp)):
            for j in range(len(temp[0])):
                on_neighbors = helper(i, j)
                if temp[i][j] == "#" and not(2 <= on_neighbors <= 3): temp[i][j] = "."
                elif on_neighbors == 3: temp[i][j] = "#"
        lights = [[j for j in i] for i in temp]

    on = 0
    for i in lights:
        for j in i:
            if j == "#": on += 1
    return on

with open(test_file) as f:
    part1_ip = f.read().split("\n\n\n\n")[0]
    part1_ip, eop = part1_ip.split("\n\n\n")
    part1_ip, steps = part1_ip.split("\n\n")
    part1_ip = part1_ip.split("\n")
    print("Part - 1: Test")
    print("\nInput:\n")
    for i in part1_ip: print(i)
    print("\nExpected Output:", eop)
    print("Generated Output:", part_1(part1_ip, int(steps)))
    
with open(input_file) as f:
    part1_ip, steps = f.read().split("\n\n")
    part1_ip = part1_ip.split("\n")
    print ("\nPart - 1: Main", part_1(part1_ip, int(steps)))