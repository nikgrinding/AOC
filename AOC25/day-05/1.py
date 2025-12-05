test_file = r"AOC25\day-05\test.txt"
input_file = r"AOC25\day-05\input.txt"

def part_1(ip):
    ranges = [[int(j) for j in i.split('-')] for i in ip[:ip.index('')]]
    ingredients = [int(i) for i in ip[ip.index('')+1:]]
    intervals = []
    count = 0

    ranges.sort()
    for range in ranges:
        if not intervals or intervals[-1][-1] < range[0]:
            intervals.append(range)
        else:
            intervals[-1][-1] = max(intervals[-1][-1], range[-1])
    
    for ingredient in ingredients:
        for start, end in intervals:
            if start <= ingredient <= end:
                count += 1
                break

    return count

with open(test_file) as f:
    part_1_ip, part_1_op = f.read().split('\n\n\n\n')[0].split('\n\n\n')
    part_1_ip = part_1_ip.split("\n")
    print("Part - 1: Test")
    print("\nInput:", part_1_ip)
    print("Expected Output:", part_1_op)
    print("Generated Output:", part_1(part_1_ip))
    
with open(input_file) as f:
    print ("\nPart - 1: Main", part_1(f.read().split("\n")))