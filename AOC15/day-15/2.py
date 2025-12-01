test_file = r"AOC15\day-15\test.txt"
input_file = r"AOC15\day-15\input.txt"

def part_2(ip, spoons, calories):

    l = [[int(j.split()[-1]) for j in i] for i in [i.split(", ") for i in ip]]

    def combs(n, current = []):
        if n == 0: return [current] if sum(current) == spoons else []
        results = []
        for i in range(1, spoons):
            if sum(current) + i > spoons: break
            results += combs(n - 1, current + [i])
        return results

    score = 0

    for comb in combs(len(l)):
        temp_score = [[i*comb[index] for i in l[index]] for index in range(len(l))]
        temp_score = [sum(j[i] for j in temp_score) for i in range(len(temp_score[0]))]
        curr_score = 1
        if temp_score[-1] == calories:
            for i in temp_score[:-1]: curr_score *= i if i > 0 else 0
            score = max(score, curr_score)

    return score

with open(test_file) as f:
    part2_ip = f.read().split("\n\n\n")[1]
    part2_ip, eop = part2_ip.split("\n\n")
    part2_ip = part2_ip.split("\n")
    part2_ip, spoons = part2_ip[:-1], part2_ip[-1]
    spoons, calories = spoons.split()
    print("Part - 2: Test")
    print("\nInput:\n")
    for i in part2_ip: print(i)
    print("\nExpected Output:", eop)
    print("Generated Output:", part_2(part2_ip, int(spoons), int(calories)))
    
with open(input_file) as f:
    part2_ip = f.read().split("\n")
    part2_ip, spoons = part2_ip[:-1], part2_ip[-1]
    spoons, calories = spoons.split()
    print ("\nPart - 2: Main", part_2(part2_ip, int(spoons), int(calories)))