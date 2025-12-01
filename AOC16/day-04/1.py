test_file = r"AOC16\day-04\test.txt"
input_file = r"AOC16\day-04\input.txt"

def part_1(ip):

    answer = 0

    for i in ip:

        chars, code = "".join(i.split("-")[:-1]), i.split("-")[-1]
        secID, code = code[:-1].split("[")

        d = {}
        for i in chars: d[i] = d.get(i, 0) + 1

        temp = ""
        for value in sorted(d.values(), reverse = True)[:5]:
            for key in sorted(d.keys()):
                if d[key] == value: temp += key if key not in temp else ""

        if code == temp[:5]: answer += int(secID)

    return answer

with open(test_file) as f:
    part1_ip = f.read().split("\n\n\n")[0]
    part1_ip, eop = part1_ip.split("\n\n")
    part1_ip = part1_ip.split("\n")
    print("Part - 1: Test")
    print("\nInput:")
    for i in part1_ip: print(i)
    print("\nExpected Output:", eop)
    print("Generated Output:", part_1(part1_ip))
    
with open(input_file) as f:
    print ("\nPart - 1: Main", part_1(f.read().split("\n")))