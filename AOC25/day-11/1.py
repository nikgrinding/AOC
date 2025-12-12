test_file = r"AOC25\day-11\test.txt"
input_file = r"AOC25\day-11\input.txt"

def part_1(ip):
    graph = {i.split(': ')[0]: i.split(': ')[1].split() for i in ip}
    path_count = {}
    def dfs(node):
        if node == "out":
            return 1
        if node in path_count:
            return path_count[node]
        paths = 0
        for neighbour in graph[node]:
            paths += dfs(neighbour)
        path_count[node] = paths
        return paths
    return dfs("you")


with open(test_file) as f:
    part_1_ip, part_1_op = f.read().split('\n\n\n')[0].split('\n\n')
    part_1_ip = part_1_ip.split("\n")
    print("Part - 1: Test")
    print("\nInput:")
    for i in part_1_ip:
        print(i)
    print("Expected Output:", part_1_op)
    print("Generated Output:", part_1(part_1_ip))
    
with open(input_file) as f:
    print ("\nPart - 1: Main", part_1(f.read().split("\n")))