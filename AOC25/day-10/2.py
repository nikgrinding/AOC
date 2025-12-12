test_file = r"AOC25\day-10\test.txt"
input_file = r"AOC25\day-10\input.txt"

import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def part_2(ip):
    def lpp_helper(A, b):
        result = milp(
            c = np.ones(len(A[0])),
            constraints = LinearConstraint(A, lb=b, ub=b),
            bounds = Bounds(0, np.inf),
            integrality = np.ones(len(A[0]), dtype=int))
        return result.fun

    answer = 0
    for line in ip:
        buttons = sorted([[int(j) for j in i[1:-1].split(',')] for i in line.split()[1:-1]], key = len, reverse = True)
        joltages = [int(j) for j in line.split()[-1][1:-1].split(',')]
        A = [[0]*len(buttons) for _ in range(len(joltages))]
        for i, button in enumerate(buttons):
            for j in button:
                A[j][i] = 1
        answer += lpp_helper(np.array(A, dtype=float),  joltages)
    return int(answer)

with open(test_file) as f:
    part_2_ip, part_2_op = f.read().split('\n\n\n')[1].split('\n\n')
    part_2_ip = part_2_ip.split("\n")
    print("Part - 2: Test")
    print("\nInput:")
    for i in part_2_ip:
        print(i)
    print("Expected Output:", part_2_op)
    print("Generated Output:", part_2(part_2_ip))
    
with open(input_file) as f:
    print ("\nPart - 2: Main", part_2(f.read().split("\n")))