test_file = r"AOC\AOC15\day-15\test.txt"
input_file = r"AOC\AOC15\day-15\input.txt"

def part_1(ip, spoons):

    l = [[int(j.split()[-1]) for j in i][:-1] for i in [i.split(", ") for i in ip]]

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
        for i in temp_score: curr_score *= i if i > 0 else 0
        score = max(score, curr_score)

    return score

with open(test_file) as f:
    part1_ip = f.read().split("\n\n\n")[0]
    part1_ip, eop = part1_ip.split("\n\n")
    part1_ip = part1_ip.split("\n")
    part1_ip, spoons = part1_ip[:-1], part1_ip[-1]
    print("Part - 1: Test")
    print("\nInput:\n")
    for i in part1_ip: print(i)
    print("\nExpected Output:", eop)
    print("Generated Output:", part_1(part1_ip, int(spoons)))
    
with open(input_file) as f:
    part1_ip = f.read().split("\n")
    part1_ip, spoons = part1_ip[:-1], part1_ip[-1]
    spoons = spoons.split()[0]
    print ("\nPart - 1: Main", part_1(part1_ip, int(spoons)))