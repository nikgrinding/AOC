from collections import deque
from itertools import combinations

test_file = r"AOC\AOC16\day-11\test.txt"
input_file = r"AOC\AOC16\day-11\input.txt"

def part_2(ip):

    d = {"elerium": (0, 0), "dilithium": (0, 0)}
    for i in range(len(ip)):
        inst = ip[i][:-1].split()
        for j in range(len(inst)-1):
            if "compatible" in inst[j]:
                if inst[j].split("-")[0] in d: d[inst[j].split("-")[0]][1] = i
                else: d[inst[j].split("-")[0]] = [-1, i]
            if "generator" in inst[j+1]:
                if inst[j] in d: d[inst[j]][0] = i
                else: d[inst[j]] = [i, -1]
    floors = tuple((i, j) for i,j in d.values())
    
    def is_valid(state):
        _, items = state
        for floor in range(4):
            generators = {i for i in range(len(items)) if items[i][0] == floor}
            microchips = {i for i in range(len(items)) if items[i][1] == floor}
            if generators and any(m not in generators for m in microchips):
                return False
        return True
    
    def bfs(start):

        seen = set()
        queue = deque([(start, 0)])

        while queue:

            (elevator, items), steps = queue.popleft()
            items = tuple(items)

            if all(g == 3 and m == 3 for g, m in items): return steps

            state_key = (elevator, tuple(sorted(items)))
            if state_key in seen: continue
            seen.add(state_key)

            indices = []
            for i in range(len(items)):
                if items[i][0] == elevator: indices.append(('G', i))
                if items[i][1] == elevator: indices.append(('M', i))

            for move in list(combinations(indices, 1)) + list(combinations(indices, 2)):

                new_items = [list(pair) for pair in items]
                for item_type, i in move:
                    if item_type == 'G': new_items[i][0] += 1
                    else: new_items[i][1] += 1

                for direction in [-1, 1]:

                    new_elevator = elevator + direction
                    if not (0 <= new_elevator <= 3): continue

                    moved_items = [list(pair) for pair in items]
                    for item_type, i in move:
                        if item_type == 'G': moved_items[i][0] = items[i][0] + direction
                        else: moved_items[i][1] = items[i][1] + direction

                    new_state = (new_elevator, tuple((i, j) for i,j in moved_items))
                    if is_valid(new_state): queue.append((new_state, steps + 1))
    
    return bfs((0, floors))
    
with open(input_file) as f:
    print ("\nPart - 2: Main", part_2(f.read().split("\n")))