# import re

test_file = r"AOC25\day-02\test.txt"
input_file = r"AOC25\day-02\input.txt"

def part_2(ip):
    def is_valid(string):
        n = len(string)
        for length in range(1, n//2+1):
            if n % length == 0:
                if string[:length] * (n//length) == string:
                    return True
        return False
    
    answer = 0
    for interval in ip:
        start, end = interval.split('-')
        start, end = int(start), int(end)
        for num in range(start, end+1):
            if is_valid(str(num)):
                answer += num
            """
            also works :)

            pattern = r'(.+?)\1+'
            string = str(num)
            if re.fullmatch(pattern, string):
                answer += num
            """
    return answer

with open(test_file) as f:
    part_2_ip, part_2_op = f.read().split('\n\n\n')[1].split('\n\n')
    part_2_ip = part_2_ip.split(",")
    print("part - 2: Test")
    print("\nInput:", part_2_ip)
    print("Expected Output:", part_2_op)
    print("Generated Output:", part_2(part_2_ip))
    
with open(input_file) as f:
    print ("\npart - 2: Main", part_2(f.read().split(",")))