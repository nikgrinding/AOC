test_file = r"AOC15\day-12\test.txt"
input_file = r"AOC15\day-12\input.txt"

def part_1(ip):
    answer = 0
    temp = ""
    for i in ip:
        if i == "-" or i.isnumeric(): temp += i
        else: 
            if temp: 
                answer += int(temp)
                temp = ""
    return answer

with open(test_file) as f:
    part1_ip = f.read().split("\n\n")[0]
    part1_ip = part1_ip.split("\n")
    print("Part - 1: Test")
    for i in part1_ip:
        ip = i.split()[0]
        print("\nInput:", ip)
        print("Expected Output:", i.split()[1])
        print("Generated Output:", part_1(ip))
    
with open(input_file) as f:
    print ("\nPart - 1: Main", part_1(f.read()))