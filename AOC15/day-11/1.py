import re

test_file = r"AOC15\day-11\test.txt"
input_file = r"AOC15\day-11\input.txt"

def part_1(ip):
    while True:
        rule_2 = r"[iol]"
        if re.findall(rule_2, ip):
            l = list(ip)
            for i in range(len(l)):
                if l[i] in "iol":
                    l[i] = chr(ord(l[i])+1)
                    l[i+1:] = ["a"]*(len(l)-i-1)
                    break
            ip = "".join(l)
        else:
            rule_1 = "|".join([chr(i)+chr(i+1)+chr(i+2) for i in range(97,121)])
            rule_3 = "|".join([chr(i)*2 for i in range(97,123)])
            if len(re.findall(rule_1, ip)) > 0 and len(re.findall(rule_3, ip)) > 1: return ip 
            l = list(ip)
            for i in range(len(l)-1, -1, -1):
                if l[i] != "z":
                    l[i] = chr(ord(l[i])+1)
                    l[i+1:] = ["a"]*(len(l)-i-1)
                    break
            ip = "".join(l)

with open(test_file) as f:
    part1_ip = f.read().split("\n")
    print("Part - 1: Test")
    for i in part1_ip:
        ip, eop = i.split()
        print("\nInput:", ip)
        print("Expected Output:", eop)
        print("Generated Output:", part_1(ip))
    
with open(input_file) as f:
    part1_ip = f.read()
    print ("\nPart - 1: Main", part_1(part1_ip))