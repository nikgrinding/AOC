test_file = r"AOC15\day-20\test.txt"
input_file = r"AOC15\day-20\input.txt"

def part_2(ip):

    limit = 1000000

    presents = [0] * (limit + 1)
    for elf in range(1, limit + 1):
        for house in range(elf, min(limit + 1, elf*50 + 1), elf): 
            presents[house] += elf * 11
    
    for house in range(1, limit + 1):
        if presents[house] >= ip: return house

with open(input_file) as f:
    part2_ip = f.read()
    print ("\nPart - 2: Main", part_2(int(part2_ip))) 