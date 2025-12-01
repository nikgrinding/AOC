test_file = r"AOC16\day-09\test.txt"
input_file = r"AOC16\day-09\input.txt"

def part_1(ip):

    decompressed_length = 0

    i = 0
    while i < len(ip):
        if ip[i].isalpha():
            decompressed_length += 1
            i += 1
        else:
            i += 1
            marker = ""
            while ip[i] != ")":
                marker += ip[i]
                i += 1
            i += 1
            decompressed_length += eval(marker.replace("x", "*"))
            i += int(marker.split("x")[0])

    return decompressed_length

with open(test_file) as f:
    part1_ip = f.read().split("\n\n")[0]
    part1_ip = part1_ip.split("\n")
    print("Part - 1: Test")
    for i in part1_ip:
        ip = i.split()[0]
        print("\nInput:", ip)
        print("Expected Output:", i.split()[1])
        print("Generated Output:", part_1(ip))
    
with open(input_file) as f:
    print ("\nPart - 1: Main", part_1(f.read()))