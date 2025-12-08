from collections import Counter

test_file = r"AOC25\day-08\test.txt"
input_file = r"AOC25\day-08\input.txt"

def part_1(ip, connections):

    ip = [[int(j) for j in i.split(',')] for i in ip]

    closest_points = [(ip[i], ip[j]) for i in range(len(ip)) for j in range(i+1, len(ip))]
    closest_points.sort(key = lambda x: (x[1][0] - x[0][0])**2 + (x[1][1] - x[0][1])**2 + (x[1][2] - x[0][2])**2)

    circuits = {tuple(i):None for i in ip}
    circuit_id = 1
    curr_connections = 0
    
    for i, j in closest_points:
        i, j = tuple(i), tuple(j)

        if circuits[i] and circuits[j]:
            to_be_changed = circuits[j]
            for circuit in circuits:
                if circuits[circuit] == to_be_changed:
                    circuits[circuit] = circuits[i]

        elif circuits[i]: circuits[j] = circuits[i]
        elif circuits[j]: circuits[i] = circuits[j]

        else:
            circuits[i] = circuits[j] = circuit_id
            circuit_id += 1

        curr_connections += 1
        if curr_connections == connections: break

    counter = Counter(circuits.values())
    needed_values = sorted([counter[i] for i in counter if i])[-3:]
    return needed_values[0]*needed_values[1]*needed_values[2]

with open(test_file) as f:
    part_1_ip, part_1_op = f.read().split('\n\n\n')[0].split('\n\n')
    part_1_ip = part_1_ip.split("\n")
    print("Part - 1: Test")
    print("\nInput:")
    for i in part_1_ip:
        print(i)
    print("Expected Output:", part_1_op)
    print("Generated Output:", part_1(part_1_ip, 10))
    
with open(input_file) as f:
    print ("\nPart - 1: Main", part_1(f.read().split("\n"), 1000))