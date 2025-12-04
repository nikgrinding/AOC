test_file = r"AOC25\day-04\test.txt"
input_file = r"AOC25\day-04\input.txt"

def part_2(ip):

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
    temp = -1

    while temp != answer:
        temp = answer
        l = []
        for i in range(m):
            for j in range(n):
                if helper(i, j):
                    l.append((i, j))
                    answer += 1
        for i, j in l:
            ip[i][j] = '.'
            
    return answer

with open(test_file) as f:
    part_2_ip, part_2_op = f.read().split('\n\n\n')[1].split('\n\n')
    part_2_ip = part_2_ip.split("\n")
    print("Part - 2: Test")
    print("\nInput:")
    for i in part_2_ip:
        print(i)
    print()
    print("Expected Output:", part_2_op)
    print("Generated Output:", part_2(part_2_ip))
    
with open(input_file) as f:
    print ("\nPart - 2: Main", part_2(f.read().split("\n")))