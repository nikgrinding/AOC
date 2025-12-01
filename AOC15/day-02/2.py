test_file = r"AOC15\day-02\test.txt"
input_file = r"AOC15\day-02\input.txt"

def part_2(ip):
    ip = ip.split("x")
    ip = [int(i) for i in ip]
    area_1 = 2*(ip[0]+ip[1])
    area_2 = 2*(ip[1]+ip[2])
    area_3 = 2*(ip[2]+ip[0])
    return ip[0]*ip[1]*ip[2] + min(area_1, area_2, area_3)

with open(test_file) as f:
    part2_ip = f.read().split("\n\n")[1]
    part2_ip = part2_ip.split("\n")
    print("Part - 2: Test")
    for i in part2_ip:
        ip = i.split()[0]
        print("\nInput:", ip)
        print("Expected Output:", i.split()[1])
        print("Generated Output:", part_2(ip))
    
with open(input_file) as f:
    part2_ip = f.read().split("\n")
    op = [part_2(ip) for ip in part2_ip]
    print ("\nPart - 2: Main", sum(op))