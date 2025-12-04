test_file = r"AOC25\day-04\test.txt"
input_file = r"AOC25\day-04\input.txt"

def part_1(ip):

    ip = [list(i) for i in ip]
    m, n = len(ip), len(ip[0])

    def helper(i, j):
        count = 0
        for r in range(-1, 2):
            for c in range(-1, 2):
                if ip[i][j] != '@': return False
                if (r != 0 or c != 0) and 0 <= i + r < m and 0 <= j + c < n and ip[i+r][j+c] == '@':
                    count += 1
        return count < 4
    
    answer = 0
    
    for i in range(m):
        for j in range(n):
            answer += 1 if helper(i, j) else 0

    return answer

with open(test_file) as f:
    part_1_ip, part_1_op = f.read().split('\n\n\n')[0].split('\n\n')
    part_1_ip = part_1_ip.split("\n")
    print("Part - 1: Test")
    print("\nInput:")
    for i in part_1_ip:
        print(i)
    print()
    print("Expected Output:", part_1_op)
    print("Generated Output:", part_1(part_1_ip))
    
with open(input_file) as f:
    print ("\nPart - 1: Main", part_1(f.read().split("\n")))