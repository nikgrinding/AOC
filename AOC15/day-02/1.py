test_file = r"AOC\AOC15\day-02\test.txt"
input_file = r"AOC\AOC15\day-02\input.txt"

def part_1(ip):
    ip = ip.split("x")
    ip = [int(i) for i in ip]
    area_1 = ip[0]*ip[1]
    area_2 = ip[1]*ip[2]
    area_3 = ip[2]*ip[0]
    return 2*(area_1+area_2+area_3) + min(area_1, area_2, area_3)

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
    part1_ip = f.read().split("\n")
    op = [part_1(ip) for ip in part1_ip]
    print ("\nPart - 1: Main", sum(op))