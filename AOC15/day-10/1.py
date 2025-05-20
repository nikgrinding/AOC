test_file = r"AOC\AOC15\day-10\test.txt"
input_file = r"AOC\AOC15\day-10\input.txt"

def part_1(ip, iter):

    for _ in range(int(iter)):

        temp = ""
        i = 0
        c = 1

        while i < len(ip):

            if i == 0:
                i += 1
                continue

            if ip[i] == ip[i-1]: c += 1
            else:
                temp += str(c) + ip[i-1]
                c = 1

            i += 1

        temp += str(c) + ip[i-1]
        ip = temp

    return ip

with open(test_file) as f:
    part1_ip = f.read().split("\n")
    print("Part - 1: Test")
    for i in part1_ip:
        ip, iter, eop = i.split()
        print("\nInput:", ip)
        print("Expected Output:", eop)
        print("Generated Output:", part_1(ip, iter))
    
with open(input_file) as f:
    part1_ip, iter_1, _ = f.read().split()
    print ("\nPart - 1: Main", len(part_1(part1_ip, iter_1)))