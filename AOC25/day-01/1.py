test_file = r"AOC25\day-01\test.txt"
input_file = r"AOC25\day-01\input.txt"

def part_1(ip):

    answer = 0
    position = 50

    for inst in ip:

        dir = inst[0]
        rotations = int(inst[1:]) % 100

        if dir == "L":
            position -= rotations
            if position < 0:
                position = 100 + position
                
        else:
            position += rotations
            position %= 100

        if position == 0:
            answer += 1
            
    return answer

with open(test_file) as f:
    part_1_ip, part_1_op = f.read().split("\n\n\n")[0].split('\n\n')
    part_1_ip = part_1_ip.split("\n")
    print("Part - 1: Test")
    print("\nInput:", part_1_ip)
    print("Expected Output:", part_1_op)
    print("Generated Output:", part_1(part_1_ip))
    
with open(input_file) as f:
    print ("\nPart - 1: Main", part_1(f.read().split("\n")))