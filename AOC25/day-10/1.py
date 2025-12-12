test_file = r"AOC25\day-10\test.txt"
input_file = r"AOC25\day-10\input.txt"

from itertools import combinations

def part_1(ip):
    answer = 0
    for line in ip:
        temp_answer = float("inf")
        lights = [1 if i == "#" else 0 for i in line.split()[0][1:-1]]
        buttons = [[int(j) for j in i[1:-1].split(',')] for i in line.split()[1:-1]]
        for i in range(1, len(buttons)+1):
            for j in combinations(buttons, i):
                temp = [0]*len(lights)
                for button in j:
                    for light in button:
                        temp[light] = 1 - temp[light]
                if temp == lights:
                    temp_answer = min(temp_answer, len(j))
        answer += temp_answer
    return answer

with open(test_file) as f:
    part_1_ip, part_1_op = f.read().split('\n\n\n')[0].split('\n\n')
    part_1_ip = part_1_ip.split("\n")
    print("Part - 1: Test")
    print("\nInput:")
    for i in part_1_ip:
        print(i)
    print("Expected Output:", part_1_op)
    print("Generated Output:", part_1(part_1_ip))
    
with open(input_file) as f:
    print ("\nPart - 1: Main", part_1(f.read().split("\n")))