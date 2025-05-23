test_file = r"AOC\AOC15\day-18\test.txt"
input_file = r"AOC\AOC15\day-18\input.txt"

def part_2(ip, steps):
    lights = [[j for j in i] for i in ip]
    lights[0][0], lights[0][-1], lights[-1][0], lights[-1][-1] = ["#"]*4

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
        lights[0][0], lights[0][-1], lights[-1][0], lights[-1][-1] = ["#"]*4

    on = 0
    for i in lights:
        for j in i:
            if j == "#": on += 1
    return on

with open(test_file) as f:
    part2_ip = f.read().split("\n\n\n\n")[1]
    part2_ip, eop = part2_ip.split("\n\n\n")
    part2_ip, steps = part2_ip.split("\n\n")
    part2_ip = part2_ip.split("\n")
    print("Part - 2: Test")
    print("\nInput:\n")
    for i in part2_ip: print(i)
    print("\nExpected Output:", eop)
    print("Generated Output:", part_2(part2_ip, int(steps)))
    
with open(input_file) as f:
    part2_ip, steps = f.read().split("\n\n")
    part2_ip = part2_ip.split("\n")
    print ("\nPart - 2: Main", part_2(part2_ip, int(steps)))