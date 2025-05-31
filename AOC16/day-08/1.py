test_file = r"AOC\AOC16\day-08\test.txt"
input_file = r"AOC\AOC16\day-08\input.txt"

def part_1(ip, width, height):

    pixels = [["." for _ in range(width)] for _ in range(height)]

    for inst in ip:
        if "rect" in inst:
            a, b = [int(i) for i in inst.split()[-1].split("x")]
            for i in range(b):
                for j in range(a):
                    pixels[i][j] = "#"
        elif "column" in inst:
            x, rotate = [int(i) for i in inst.split("=")[-1].split(" by ")]
            col = [row[x] for row in pixels]
            col = col[-rotate:]+col[:-rotate]
            for i in range(len(pixels)):
                pixels[i][x] = col[i]
        else:
            y, rotate = [int(i) for i in inst.split("=")[-1].split(" by ")]
            pixels[y] = pixels[y][-rotate:]+pixels[y][:-rotate]
    
    on = 0
    for i in pixels:
        for j in i:
            if j == "#": on += 1
    return on

with open(test_file) as f:
    part1_ip, eop = f.read().split("\n\n")
    part1_ip = part1_ip.split("\n")
    print("Part - 1: Test")
    print("\nInput:")
    for i in part1_ip: print(i)
    print("\nExpected Output:", eop)
    print("Generated Output:", part_1(part1_ip, 7, 3))
    
with open(input_file) as f:
    print ("\nPart - 1: Main", part_1(f.read().split("\n"), 50, 6))