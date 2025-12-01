## Part 1

You're dropped in a city and given a sequence of directions. You start at the origin facing North. Each instruction tells you to turn left or right, then walk a number of blocks. Your task is to find the Manhattan distance from your starting point to your final position.

**Examples:**

- `R2, L3` → `5`
- `R2, R2, R2` → `2`
- `R5, L5, R5, R3` → `12`

### Idea

Keep track of your current direction and position, and update them as you process each instruction. At the end, return the sum of the absolute values of your x and y coordinates.

## Part 2

Now you're asked to find the **first** location you visit twice. As you follow each instruction, you must move step by step and record every position you pass through. The moment you revisit a position, report its distance from the origin.

**Examples:**

- `R8, R4, R4, R8` → `4`

### Idea

Simulate walking one block at a time in the current direction, recording all visited positions. Use a set to track locations. If a location is seen again, return its Manhattan distance immediately.