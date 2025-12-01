test_file = r"AOC16\day-08\test.txt"
input_file = r"AOC16\day-08\input.txt"

def part_2(ip, width, height):

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

    for i in range(len(pixels)):
        for j in range(len(pixels[0])):
            if pixels[i][j] != ".": print(pixels[i][j], end = "")
            else: print(" ", end = "")
            if (j+1)%5 == 0: print("\t", end = "")
        print()
    
with open(input_file) as f:
    print ("\nPart - 2: Main")
    part_2(f.read().split("\n"), 50, 6)