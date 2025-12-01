test_file = r"AOC25\day-01\test.txt"
input_file = r"AOC25\day-01\input.txt"

def part_2(ip):

    answer = 0
    position = 50

    for inst in ip:

        dir = inst[0]
        rotations = int(inst[1:])

        answer += rotations // 100
        rotations %= 100
        old = position

        if dir == "L":
            position -= rotations
            if position < 0:
                if old > 0:
                    answer += 1
                position = 100 + position
        else:
            position += rotations
            if position > 100:
                answer += 1
            position %= 100

        if position == 0:
            answer += 1
            
    return answer

with open(test_file) as f:
    part_2_ip, part_2_op = f.read().split("\n\n\n")[1].split('\n\n')
    part_2_ip = part_2_ip.split("\n")
    print("Part - 2: Test")
    print("\nInput:", part_2_ip)
    print("Expected Output:", part_2_op)
    print("Generated Output:", part_2(part_2_ip))
    
with open(input_file) as f:
    print ("\nPart - 2: Main", part_2(f.read().split("\n")))