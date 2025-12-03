test_file = r"AOC25\day-03\test.txt"
input_file = r"AOC25\day-03\input.txt"

def part_2(ip):
    answer = 0
    for bank in ip:
        stack = []
        c = 0
        for battery in bank:
            while stack and stack[-1] < battery and c < len(bank)-12:
                c += 1
                stack.pop()
            stack.append(battery)
        answer += int("".join(stack[:12]))
    return answer

with open(test_file) as f:
    part_2_ip, part_2_op = f.read().split('\n\n\n')[1].split('\n\n')
    part_2_ip = part_2_ip.split("\n")
    print("Part - 2: Test")
    print("\nInput:", part_2_ip)
    print("Expected Output:", part_2_op)
    print("Generated Output:", part_2(part_2_ip))
    
with open(input_file) as f:
    print ("\nPart - 2: Main", part_2(f.read().split("\n")))