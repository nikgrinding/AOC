test_file = r"AOC25\day-06\test.txt"
input_file = r"AOC25\day-06\input.txt"

def part_2(ip):

    ops, ip = ip[-1], ip[:-1]

    answer = 0

    d = {}
    reordered = []
    
    for i in range(len(ip[0])):
        if ops[i] in ['+', '*']:
            if d: reordered.append([int(i) for i in list(d.values()) if i.strip()])
            d = {}
        for j in range(len(ip)):
            d[i] = d.get(i, '') + ip[j][i]
    reordered.append([int(i) for i in list(d.values()) if i.strip()])

    ops = ops.split()

    for i in range(len(reordered)):
        if ops[i] == '+': answer += sum(reordered[i])
        else:
            temp = 1
            for val in reordered[i]: temp *= val
            answer += temp

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