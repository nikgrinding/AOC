test_file = r"AOC16\day-04\test.txt"
input_file = r"AOC16\day-04\input.txt"

def part_2(ip):

    answer = []

    for i in ip:

        chars, secID = "-".join(i.split("-")[:-1]), i.split("-")[-1]
        secID = "".join(i for i in secID if i.isnumeric())
        chars = "".join([chr((ord(i)-ord('a')+int(secID))%26+ord('a')) if i != "-" else " " for i in chars])
        answer.append([chars, secID])

    if len(answer) == 1: return answer[0][0]

    for i in answer:
        if "north" in i[0]:
            return i[1]

with open(test_file) as f:
    part2_ip = f.read().split("\n\n\n")[1]
    part2_ip, eop = part2_ip.split("\n\n")
    part2_ip = part2_ip.split("\n")
    print("Part - 2: Test")
    print("\nInput:")
    for i in part2_ip: print(i)
    print("\nExpected Output:", eop)
    print("Generated Output:", part_2(part2_ip))
    
with open(input_file) as f:
    print ("\nPart - 2: Main", part_2(f.read().split("\n")))