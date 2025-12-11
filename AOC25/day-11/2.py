test_file = r"test.txt"
input_file = r"input.txt"

def part_2(ip):
    graph = {i.split(': ')[0]: i.split(': ')[1].split() for i in ip}
    path_count = {}
    def dfs(node, has_dac = False, has_fft = False):
        has_dac |= node == "dac"
        has_fft |= node == "fft"
        node_info = (node, has_dac, has_fft)
        if node == "out":
            return 1 if has_dac and has_fft else 0
        if node_info in path_count:
            return path_count[node_info]
        paths = 0
        for neighbour in graph[node]:
            paths += dfs(neighbour, has_dac, has_fft)
        path_count[node_info] = paths
        return paths
    return dfs("svr")


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