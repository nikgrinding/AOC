## Part 1

We are given a grid representing a set of lights where each cell is either on (`#`) or off (`.`). The lights evolve over time following specific rules based on their neighbors:
- A light that's on stays on if it has 2 or 3 neighbors that are on; otherwise, it turns off
- A light that's off turns on if exactly 3 neighbors are on; otherwise, it stays off

We apply these rules for 100 steps and count how many lights are on at the end.

**Example:**
Input:
```
.#.#.#
...##.
#....#
..#...
#.#..#
####..
```
Output after 4 steps:
```
4
```

### Idea
For each step, update all lights simultaneously based on the previous state. Count on-neighbors for each cell, then apply rules to determine next state. Repeat this for 100 steps and count how many lights are on at the end.


## Part 2

Same as part 1, but the four corner lights are broken and permanently stuck in the "on" state. These corners stay on through all 100 steps, regardless of the rules.

**Example:**
Input:
```
##.#.#
...##.
#....#
..#...
#.#..#
####.#
```
Output after 5 steps:
```
17
```

### Idea
Follow the same simulation as in part 1, but after every step, force the four corners to be "on" before starting the next step. At the end, count the number of lights that are on.