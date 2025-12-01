test_file = r"AOC15\day-16\test.txt"
input_file = r"AOC15\day-16\input.txt"

def part_1(ip, signature):

    signature = {i.split()[0]: i.split()[1] for i in signature}

    for aunt in ip:
        curr_aunt = aunt.split(", ")
        aunt_no = curr_aunt[0].split(":")[0].split()[1]
        curr_aunt[0] = ": ".join(curr_aunt[0].split(": ")[1:])
        curr_aunt = {i.split()[0]: i.split()[1] for i in curr_aunt}
        flag = True
        for i in curr_aunt:
            if curr_aunt[i] != signature[i]: flag = False
        if flag: return aunt_no
    
with open(input_file) as f:
    part1_ip, signature = f.read().split("\n\n")
    part1_ip = part1_ip.split("\n")
    signature = signature.split("\n")
    print ("\nPart - 1: Main", part_1(part1_ip, signature))