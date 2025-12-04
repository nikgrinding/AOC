# Day 4: Printing Department

## Part 1

The Elves need to optimize forklift work by identifying which paper rolls can be accessed. A paper roll (`@`) can be accessed by a forklift if it has **fewer than 4 adjacent paper rolls** in the 8 surrounding positions (horizontal, vertical, and diagonal). The goal is to count how many accessible rolls exist in the initial configuration.

**Input format:** A grid where `@` represents a paper roll and `.` represents empty space.

**Key rules:**
- A roll is accessible if it has **less than 4** neighboring `@` symbols
- Check all 8 adjacent positions (including diagonals)
- Empty positions (`.`) don't count as neighbors

**Example:**

```
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
```

Accessible rolls (marked with `x`):
```
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
```

**Expected output:** `13` accessible rolls

### Idea

1. For each position containing a `@`, count how many of the 8 adjacent cells also contain `@`
2. If the count is less than 4, the roll is accessible
3. Sum up all accessible rolls in the grid

## Part 2

Now the Elves want to know how many rolls can be **removed in total** through an iterative process. After removing accessible rolls, new rolls may become accessible (as their neighbor count decreases). The process continues until no more rolls can be removed.

**Additional rules:**
- Remove all accessible rolls simultaneously in each round
- After removal, recalculate which rolls are now accessible
- Repeat until no rolls can be accessed

**Example:**

Starting with the same grid, the process unfolds:
- **Round 1:** Remove 13 rolls (those with <4 neighbors)
- **Round 2:** Remove 12 rolls (newly accessible after round 1)
- **Round 3:** Remove 7 rolls
- **Round 4:** Remove 5 rolls
- **Round 5:** Remove 2 rolls
- **Round 6-9:** Remove 1 roll each
- **Total:** `43` rolls removed

**Important edge cases:**
- The process must continue until no change occurs between rounds
- All accessible rolls in a round are removed together before rechecking

### Idea

1. Identify all accessible rolls (same logic as Part 1)
2. Remove all accessible rolls simultaneously by marking them as `.`
3. Repeat steps 1-2 until no more accessible rolls are found
4. Return the total count of all removed rolls across all rounds
