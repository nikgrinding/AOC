from itertools import permutations

test_file = r"AOC15\day-09\test.txt"
input_file = r"AOC15\day-09\input.txt"

def part_1(ip):

    cities = sorted([i for i in set((" ".join(ip)).split()) if i.isalpha() and i != "to"])
    
    M = [[0]*len(cities) for i in range(len(cities))]
    for i in ip:
        city_1, _, city_2, _, dist = i.split()
        M[cities.index(city_1)][cities.index(city_2)] = int(dist)
    for i in range(len(M)):
        for j in range(len(M)): M[i][j] = max(M[i][j], M[j][i])

    shortest_cost = float("inf")    
    for route in permutations(cities):
        cost = 0
        for city in range(len(route)-1):
            cost += M[cities.index(route[city])][cities.index(route[city+1])]
        shortest_cost = min(shortest_cost, cost)
    return shortest_cost

with open(test_file) as f:
    part1_ip = f.read().split("\n\n\n")[0]
    part1_ip, eop = part1_ip.split("\n\n")
    part1_ip = part1_ip.split("\n")
    print("Part - 1: Test")
    print("\nInput:\n")
    for i in part1_ip: print(i)
    print("\nExpected Output:", eop)
    print("Generated Output:", part_1(part1_ip))
    
with open(input_file) as f:
    part1_ip = f.read().split("\n")
    print ("\nPart - 1: Main", part_1(part1_ip))