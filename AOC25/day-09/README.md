# Day 9: Movie Theater

## Part 1
- The problem asks us to find the **largest possible rectangle** formed by selecting two red tiles from a given grid as opposite corners.
- We are given a list of coordinates representing the locations of these red tiles.
- The area is calculated including the tiles themselves, so a rectangle from `x1,y1` to `x2,y2` has dimensions `(|x1-x2| + 1)` by `(|y1-y2| + 1)`.

### Input Format
The input is a list of coordinate pairs, one per line:
```text
7,1
11,1
11,7
9,7
...
```
### What is to be done
- Any two points from the input list can be chosen as corners.
- There are no obstructions or boundaries; the entire grid is effectively empty except for the chosen corners.
- We simply need to maximize `width * height`.

### Expected Output
For the full example input provided in the problem description, the maximum area is `50`.

### Idea
1. Parse the input into a list of `(x, y)` integer tuples.
2. Iterate through every unique pair of points `(p1, p2)` in the list.
3. Calculate the area formed by these two points using the formula `(abs(x1-x2)+1) * (abs(y1-y2)+1)`.
4. Track and return the maximum area found.

---

## Part 2
*(Note: This solution is currently a Work in Progress. It works perfectly for the test input, but fails on the main input because reality is often disappointing ;-;)*

- The problem introduces a constraint: rectangles can only be formed using **Red** (input) or **Green** tiles.
- The Red tiles now form a connected loop (a boundary), and everything inside that loop is considered **Green**.
- We must find the largest rectangle where **every tile inside the rectangle** is either Red or Green.

### Additional Rules
- The rectangle must still use two original Red tiles as corners.
- The rectangle cannot cross into "empty" space (outside the Red/Green loop).
- The shape formed by the input is a rectilinear polygon (all edges are vertical or horizontal).

### Edge Cases
- **Concave Shapes:** Shapes like "U" or "C" where a straight line between two valid points might cross empty space.
- **Coordinate Compression:** The actual coordinates are too large to build a full grid.

### Idea
1. Parse inputs and build a dictionary-based grid. Remove empty columns by transposing the matrix and filtering out rows (former columns) that contain no `#`.
2. Iterate through every row. Identify the first and last `#` in that row and fill everything between them with `#`.
3. Transpose the matrix (swap rows and columns) and repeat the gap-filling process to ensure the shape is solid vertically as well. Transpose back to original orientation.
4. Sort the original inputs and map them to their new positions in the compressed/filled grid.
5. Iterate through pairs of mapped points. Check if the sub-rectangle between them contains any empty spots (`.`). If valid, calculate the area using the *original* coordinates.