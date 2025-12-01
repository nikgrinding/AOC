test_file = r"AOC15\day-25\test.txt"
input_file = r"AOC15\day-25\input.txt"

def part_1(ip):
    cell_no = (sum(ip)-1)*(sum(ip)-2)//2 + ip[1]
    code = 20151125
    for i in range(1, cell_no):
        code  = code * 252533 % 33554393
    return code

with open(test_file) as f:
    part1_ip, eop = f.read().split("\n\n")
    part1_ip = [i for i in part1_ip.split("\n")]
    part1_ip = [[int(j) for j in i.split() if j.isnumeric()] for i in [i.replace(".", "").replace(",", "") for i in part1_ip]]
    print("Part - 1: Test")
    for i in part1_ip: 
        print("Input:", i)
        print("Generated Output:", part_1(i))
    print("\nExpected Output:")
    for i in eop.split('\n'): print(i)
    
with open(input_file) as f:
    part1_ip = [int(i) for i in f.read().replace(".", "").replace(",", "").split() if i.isnumeric()]
    print(part1_ip)
    print ("\nPart - 1: Main", part_1(part1_ip))