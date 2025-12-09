test_file = r"test.txt"
input_file = r"input.txt"

def part_2(ip):
    ip = [[int(j) for j in i.split(',')][::-1] for i in ip]
    cols = max(i[1] for i in ip)+1
    d = {}
    for i, j in ip:
        if i not in d:
            d[i] = ['.']*cols
        d[i][j] = '#'
    print('#1')
    grid = []
    for i in sorted(d):
        grid.append(d[i])
    print('#2')
    transposed_matrix = list(zip(*grid))
    print('#3')
    new_grid = []
    for i in transposed_matrix:
        if '#' in i:
            new_grid.append(i)
    grid = list(zip(*new_grid))
    print('#4')
    ip.sort()
    new_ip = sorted([(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '#'])
    for i in range(len(grid)):
        row = "".join(grid[i])
        l_ptr, r_ptr = row.find('#'), row.rfind('#')
        grid[i] = list(grid[i])
        grid[i][l_ptr:r_ptr+1] = ['#']*(r_ptr-l_ptr+1)
    grid = list(zip(*grid))
    for i in range(len(grid)):
        row = "".join(grid[i])
        l_ptr, r_ptr = row.find('#'), row.rfind('#')
        grid[i] = list(grid[i])
        grid[i][l_ptr:r_ptr+1] = ['#']*(r_ptr-l_ptr+1)
    grid = list(zip(*grid))
    print('#5')
    def is_valid(p1, p2):
        for i in range(min(p1[0], p2[0]), max(p1[0], p2[0])+1):
            for j in range(min(p1[1], p2[1]), max(p1[1], p2[1])+1):
                if grid[i][j] == '.':
                    return False
        return True
    answer = 0
    for i in range(len(ip)):
        for j in range(i+1, len(ip)):
            if is_valid(new_ip[i], new_ip[j]):
                answer = max(answer, (abs(ip[i][0]-ip[j][0])+1)*(abs(ip[i][1]-ip[j][1])+1))
    return answer

with open(test_file) as f:
    part_2_ip, part_2_op = f.read().split('\n\n\n')[1].split('\n\n')
    part_2_ip = part_2_ip.split("\n")
    print("Part - 2: Test")
    print("\nInput:")
    for i in part_2_ip:
        print(i)
    print("Expected Output:", part_2_op)
    print("Generated Output:", part_2(part_2_ip))
    
with open(input_file) as f:
    print ("\nPart - 2: Main", part_2(f.read().split("\n")))