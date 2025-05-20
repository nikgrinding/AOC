from itertools import permutations

test_file = r"AOC\AOC15\day-09\test.txt"
input_file = r"AOC\AOC15\day-09\input.txt"

def part_2(ip):

    cities = sorted([i for i in set((" ".join(ip)).split()) if i.isalpha() and i != "to"])
    
    M = [[0]*len(cities) for i in range(len(cities))]
    for i in ip:
        city_1, _, city_2, _, dist = i.split()
        M[cities.index(city_1)][cities.index(city_2)] = int(dist)
    for i in range(len(M)):
        for j in range(len(M)): M[i][j] = max(M[i][j], M[j][i])

    longest_cost = 0    
    for route in permutations(cities):
        cost = 0
        for city in range(len(route)-1):
            cost += M[cities.index(route[city])][cities.index(route[city+1])]
        longest_cost = max(longest_cost, cost)
    return longest_cost

with open(test_file) as f:
    part2_ip = f.read().split("\n\n\n")[1]
    part2_ip, eop = part2_ip.split("\n\n")
    part2_ip = part2_ip.split("\n")
    print("Part - 2: Test")
    print("\nInput:\n")
    for i in part2_ip: print(i)
    print("\nExpected Output:", eop)
    print("Generated Output:", part_2(part2_ip))
    
with open(input_file) as f:
    part2_ip = f.read().split("\n")
    print ("\nPart - 2: Main", part_2(part2_ip)) 