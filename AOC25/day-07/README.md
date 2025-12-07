# Day 7: Laboratories

## Part 1

A **tachyon beam** enters a manifold at position `S` and travels downward through a grid. The beam passes through empty space (`.`) but when it encounters a **splitter** (`^`), the beam stops and splits into two new beams that continue from the immediate left and right of the splitter. The goal is to count the total number of times the beam splits.

**Input format:**

-   Grid with `S` marking the starting position (always in the first row)
-   `.` represents empty space
-   `^` represents a splitter

**Key rules:**

-   Tachyon beams always move downward
-   When a beam hits a splitter, it stops and creates two new beams (left and right)
-   Multiple beams can merge into the same path (counted as one beam)
-   Count each split event, not the number of beams

_Example:_

```
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
```

**Explanation:**

1. Beam starts at `S` and moves down to the first `^` at row 2
2. Splits once -> 2 beams going left and right
3. Both beams hit splitters at row 4 -> but they merge in the middle, creating only 3 beams total
4. Process continues with each splitter creating new beams
5. Final count: **21 splits**

### Idea

1. Use **recursive DFS** starting from `S`, moving downward through the grid
2. Track **visited positions** to avoid counting the same path multiple times (beams can merge)
3. When encountering a splitter (`^`), increment the split counter and recursively explore both left and right paths
4. When encountering empty space (`.`), continue moving downward

## Part 2

Instead of multiple classical tachyon beams, a **single quantum tachyon particle** travels through the manifold. Using the **many-worlds interpretation**, each time the particle reaches a splitter, reality itself splits into multiple timelines - one where the particle went left and one where it went right. The goal is to count the total number of distinct timelines after the particle completes all possible journeys.

**Additional rules:**

-   Single particle takes **both paths** at every splitter
-   Each split creates a new timeline (universe branches)
-   Count the total number of distinct end states (timelines)

_Example:_

Using the same grid from Part 1:

-   Timeline 1: Particle always goes left at each splitter
-   Timeline 2: Particle alternates left/right at each splitter
-   Timeline 3+: Many other combinations of left/right choices
-   Total: **40 different timelines**

**Important edge cases:**

-   Different paths can lead to the same final position but are counted as separate timelines
-   A particle exiting the grid bottom counts as one timeline
-   Somehow have to avoid recalculation of identical subpaths

### Idea

1. Use **recursive counting** and a kind of **memoization** starting from `S`
2. Base case: when particle exits the grid boundary, return `1` (one timeline completes)
3. For empty space (`.`), continue downward and return the count from that path
4. For splitter (`^`), return the **sum** of timelines from both left and right paths (timelines multiply)
5. Cache results using `(x, y)` coordinates to avoid recalculating the same position multiple times
