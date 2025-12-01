## Part 1

You arrive at a secret entrance with a safe that has a dial numbered 0-99. The dial starts at 50. You're given a sequence of rotations in the format:

-   `L<n>` - rotate left (toward lower numbers) by n clicks
-   `R<n>` - rotate right (toward higher numbers) by n clicks

The dial wraps around (0-1 becomes 99, 99+1 becomes 0). The actual password is **the number of times the dial points at 0 after completing any rotation**.

**Example:**

```
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
```

Starting at 50:

-   L68 -> 82
-   L30 -> 52
-   R48 -> 0 (count: 1)
-   L5 -> 95
-   R60 -> 55
-   L55 -> 0 (count: 2)
-   L1 -> 99
-   L99 -> 0 (count: 3)
-   R14 -> 14
-   L82 -> 32

Password = `3`

### Idea

Track the current position starting at 50. For each rotation:

1. Apply the rotation (handle modulo 100 for wraparound)
2. Check if the final position is 0 and increment counter

## Part 2

Using "password method 0x434C49434B", you now count **every time the dial passes through 0 during any click**, not just at the end of rotations.

**Example:**
Using the same rotations:

-   L68: dial goes 50->49->...->0->99->...->82 (passes 0 once during rotation)
-   R48: dial ends at 0 (1 count)
-   R60: dial goes 55->56->...->99->0->1->...->55 (passes 0 once during rotation)
-   L55: dial ends at 0 (1 count)
-   L99: dial ends at 0 (1 count)
-   L82: dial goes 32->31->...->0->99->...->32 (passes 0 once during rotation)

Total = `6` (3 from ending at 0, 3 from passing through 0)

**Important:** A rotation like R1000 from position 50 would pass through 0 ten times (1000 -> 100 = 10 complete loops).

### Idea

For each rotation:

1. Count how many complete loops around the dial (rotations -> 100)
2. Check if the remaining rotation causes the dial to cross 0
3. Count if the final position is 0
