# Day 9: Movie Theater

## Part 1

The movie theater has a grid floor with red tiles at specific coordinates. The task is to find the **largest rectangle** that can be formed using any two red tiles as opposite corners. The rectangle doesn't need to contain only red tiles - it can include any tiles, as long as two opposite corners are red.

### Input Format

-   Each line contains coordinates in the format `x,y` representing the position of a red tile
-   Coordinates are comma-separated integers

### Key Rules

-   Choose any two red tiles as opposite corners of a rectangle
-   Calculate the area of the rectangle formed
-   Find the maximum possible area among all possible pairs

### Example

Input:

```
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
```

Grid visualization (# represents red tiles):

```
..............
.......#...#..
..............
..#....#......
..............
..#......#....
..............
.........#.#..
..............
```

**Step-by-step walkthrough:**

1. Consider tiles at `(2,5)` and `(9,7)`:

    - Width = |9-2| + 1 = 8
    - Height = |7-5| + 1 = 3
    - Area = 8 \* 3 = 24

2. Consider tiles at `(7,1)` and `(11,7)`:

    - Width = |11-7| + 1 = 5
    - Height = |7-1| + 1 = 7
    - Area = 5 \* 7 = 35

3. Consider tiles at `(2,5)` and `(11,1)`:
    - Width = |11-2| + 1 = 10
    - Height = |5-1| + 1 = 5
    - Area = 10 \* 5 = **50** (maximum)

**Expected output:** 50

### Idea

1. Parse all red tile coordinates into a list of `(row, col)` pairs
2. Iterate through all possible pairs of red tiles using nested loops
3. For each pair, calculate the rectangle area as `(|x1-x2| + 1) * (|y1-y2| + 1)`
4. Track and return the maximum area found

## Part 2

Part 2 adds a constraint: the rectangle can **only include red or green tiles**. Green tiles form a closed loop connecting all red tiles in the order they appear in the input (wrapping from last to first). Additionally, all tiles **inside this loop** are also green. The rectangle must still have red corners, but cannot include any tiles that are neither red nor green.

### Additional Rules

-   Red tiles in the input list are connected sequentially by straight lines of green tiles
-   The first and last red tiles are also connected (forming a loop)
-   All tiles inside the closed loop are green
-   The rectangle can only contain red or green tiles (no other tiles)

### Example

Using the same input, the green tiles (X) form a loop:

```
..............
.......#XXX#..
.......XXXXX..
..#XXXX#XXXX..
..XXXXXXXXXX..
..#XXXXXX#XX..
.........XXX..
.........#X#..
..............
```

**Valid rectangle examples:**

1. Between `(7,3)` and `(11,1)` -> Area = 15
2. Between `(9,7)` and `(9,5)` -> Area = 3
3. Between `(9,5)` and `(2,3)` -> Area = **24** (maximum)

**Expected output:** 24

### Important Edge Cases

-   Rectangles that would have been valid in Part 1 may be invalid if they include non-green tiles
-   Thin vertical or horizontal rectangles along the loop boundary may be optimal
-   The loop filling algorithm must correctly identify all interior tiles as green

### Idea

1. Build a grid and mark all red tiles
2. Construct the green tile loop by connecting consecutive red tiles with straight lines (horizontal or vertical)
3. Fill the interior of the loop by scanning each row between its leftmost and rightmost `#` markers
4. For each pair of red tiles, validate that all tiles in the rectangle are red or green
5. Return the maximum valid area found
