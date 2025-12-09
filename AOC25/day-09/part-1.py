test_file = r"test.txt"
input_file = r"input.txt"

def part_1(ip):
    ip = [[int(j) for j in i.split(',')[::-1]] for i in ip]
    answer = 0
    for i in range(len(ip)):
        for j in range(i+1, len(ip)):
            answer = max(answer, (abs(ip[i][0]-ip[j][0])+1)*(abs(ip[i][1]-ip[j][1])+1))
    return answer

with open(test_file) as f:
    part_1_ip, part_1_op = f.read().split('\n\n\n')[0].split('\n\n')
    part_1_ip = part_1_ip.split("\n")
    print("Part - 2: Test")
    print("\nInput:")
    for i in part_1_ip:
        print(i)
    print("Expected Output:", part_1_op)
    print("Generated Output:", part_1(part_1_ip))
    
with open(input_file) as f:
    print ("\nPart - 2: Main", part_1(f.read().split("\n")))