test_file = r"AOC25\day-02\test.txt"
input_file = r"AOC25\day-02\input.txt"

def part_1(ip):
    answer = 0
    for interval in ip:
        start, end = interval.split('-')
        start, end = int(start), int(end)
        for num in range(start, end+1):
            string = str(num)
            n = len(string)
            if n % 2 != 0:
                continue
            if string[:n//2] == string[n//2:]:
                answer += num
    return answer

with open(test_file) as f:
    part_1_ip, part_1_op = f.read().split('\n\n\n')[0].split('\n\n')
    part_1_ip = part_1_ip.split(",")
    print("Part - 1: Test")
    print("\nInput:", part_1_ip)
    print("Expected Output:", part_1_op)
    print("Generated Output:", part_1(part_1_ip))
    
with open(input_file) as f:
    print ("\nPart - 1: Main", part_1(f.read().split(",")))