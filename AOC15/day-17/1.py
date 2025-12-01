test_file = r"AOC15\day-17\test.txt"
input_file = r"AOC15\day-17\input.txt"

def part_1(ip, eggnog):

    dp = [0]*(eggnog+1)
    dp[0] = 1

    for i in ip:
        for j in range(eggnog, i-1, -1):
            dp[j] += dp[j-i]
    
    return dp[-1]

with open(test_file) as f:
    part1_ip = f.read().split("\n\n\n\n")[0]
    part1_ip, eop = part1_ip.split("\n\n\n")
    part1_ip, eggnog = part1_ip.split("\n\n")
    part1_ip = [int(i) for i in part1_ip.split("\n")]
    print("Part - 1: Test")
    print("\nInput:", part1_ip)
    print("\nExpected Output:", eop)
    print("Generated Output:", part_1(part1_ip, int(eggnog)))
    
with open(input_file) as f:
    part1_ip, eggnog = f.read().split("\n\n")
    part1_ip = [int(i) for i in part1_ip.split("\n")]
    print ("\nPart - 1: Main", part_1(part1_ip, int(eggnog)))