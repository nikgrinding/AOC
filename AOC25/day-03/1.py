test_file = r"AOC25\day-03\test.txt"
input_file = r"AOC25\day-03\input.txt"

def part_1(ip):
    answer = 0
    for bank in ip:
        max1 = '0'
        max2 = '0'
        for i in range(len(bank)-1):
            battery = bank[i]
            if battery > max1:
                max1 = battery
                max2 = bank[i+1]
            elif battery > max2:
                max2 = battery
        max2 = max(max2, bank[-1])
        answer += int(max1 + max2)
    return answer

with open(test_file) as f:
    part_1_ip, part_1_op = f.read().split('\n\n\n')[0].split('\n\n')
    part_1_ip = part_1_ip.split("\n")
    print("Part - 1: Test")
    print("\nInput:", part_1_ip)
    print("Expected Output:", part_1_op)
    print("Generated Output:", part_1(part_1_ip))
    
with open(input_file) as f:
    print ("\nPart - 1: Main", part_1(f.read().split("\n")))