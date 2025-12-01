test_file = r"AOC15\day-16\test.txt"
input_file = r"AOC15\day-16\input.txt"

def part_2(ip, signature):

    signature = {i.split()[0]: i.split()[1] for i in signature}

    for aunt in ip:
        curr_aunt = aunt.split(", ")
        aunt_no = curr_aunt[0].split(":")[0].split()[1]
        curr_aunt[0] = ": ".join(curr_aunt[0].split(": ")[1:])
        curr_aunt = {i.split()[0]: i.split()[1] for i in curr_aunt}
        flag = True
        for i in curr_aunt:
            if i in ["cats:", "trees:"]: 
                if curr_aunt[i] <= signature[i]: flag = False
            elif i in ["pomeranians:", "goldfish:"]:
                if curr_aunt[i] >= signature[i]: flag = False
            else: 
                if curr_aunt[i] != signature[i]: flag = False
        if flag: return aunt_no
    
with open(input_file) as f:
    part2_ip, signature = f.read().split("\n\n")
    part2_ip = part2_ip.split("\n")
    signature = signature.split("\n")
    print ("\nPart - 2: Main", part_2(part2_ip, signature))