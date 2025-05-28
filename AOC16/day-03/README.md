## Part 1

You’re given a list of triangles represented by three side lengths. A triangle is valid only if the sum of any two sides is greater than the third. Count how many triangles in the list are valid.

**Example:**
```
5 10 25
```
→ Invalid (5 + 10 is not greater than 25)

### Idea

For each line, check if the sum of any two sides is greater than the third side. If it passes all three checks, it’s a valid triangle.

## Part 2

Instead of reading the triangle side lengths row by row, now you must read them vertically in groups of three rows. Each column in these groups forms one triangle.

**Example:**
```
101 301 501
102 302 502
103 303 503
```
→ Triangles: [101, 102, 103], [301, 302, 303], [501, 502, 503]

### Idea

Process input in chunks of 3 rows, and then extract the columns to form triangles. For each vertical group, check if the triangle is valid using the same rule as in part 1.