test_file = r"AOC25\day-06\test.txt"
input_file = r"AOC25\day-06\input.txt"

def part_1(ip):

    ops, ip = ip[-1].split(), [[int(j) for j in i.split()] for i in ip[:-1]]

    answer = 0

    for i in range(len(ip[0])):

        if ops[i] == '+': temp = 0
        else: temp = 1

        for line in ip:
            if ops[i] == '+': temp += line[i]
            else: temp *= line[i]

        answer += temp 
        
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