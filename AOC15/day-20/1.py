test_file = r"AOC\AOC15\day-20\test.txt"
input_file = r"AOC\AOC15\day-20\input.txt"

# def part_1(ip):

#     i = 1
#     while True:
#         gifts = 0
#         for j in range(1, int(i**0.5)+1):
#             if i % j == 0:
#                 gifts += 10*(j+i//j) if j != i//j else 10*j
#         if gifts >= ip: return i
#         i += 1

def part_1(ip):

    limit = 1000000

    presents = [0] * (limit + 1)
    for elf in range(1, limit + 1):
        for house in range(elf, limit + 1, elf): presents[house] += elf * 10
    
    for house in range(1, limit + 1):
        if presents[house] >= ip: return house

with open(test_file) as f:
    part1_ip = f.read().split("\n")
    print("Part - 1: Test")
    for i in part1_ip:
        ip = i.split()[0]
        print("\nInput:", ip)
        print("Expected Output:", i.split()[1])
        print("Generated Output:", part_1(int(ip)))
    
with open(input_file) as f:
    part1_ip = f.read()
    print ("\nPart - 1: Main", part_1(int(part1_ip))) 