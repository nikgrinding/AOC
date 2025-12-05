test_file = r"AOC25\day-05\test.txt"
input_file = r"AOC25\day-05\input.txt"

def part_2(ip):
    ranges = [[int(j) for j in i.split('-')] for i in ip[:ip.index('')]]
    intervals = []
    count = 0

    ranges.sort()
    for range in ranges:
        if not intervals or intervals[-1][-1] < range[0]:
            intervals.append(range)
        else:
            intervals[-1][-1] = max(intervals[-1][-1], range[-1])

    for start, end in intervals:
        count += end-start+1
    return count

with open(test_file) as f:
    part_2_ip, part_2_op = f.read().split('\n\n\n\n')[1].split('\n\n\n')
    part_2_ip = part_2_ip.split("\n")
    print("Part - 2: Test")
    print("\nInput:", part_2_ip)
    print("Expected Output:", part_2_op)
    print("Generated Output:", part_2(part_2_ip))
    
with open(input_file) as f:
    print ("\nPart - 2: Main", part_2(f.read().split("\n")))