## Part 1

You're in a maze of twisty little cubicles, and each coordinate is either a wall or an open space. A formula involving the coordinates and a given number determines which it is. Starting at position (1,1), your goal is to find the minimum number of steps required to reach position (31,39), moving only up, down, left, or right (no diagonals), and only through open spaces.

**Example:**
With the input `10`, to reach (7,4), the shortest path takes 11 steps:
```
  0123456789
0 .#.####.##
1 .O#..#...#
2 #OOO.##...
3 ###O#.###.
4 .##OO#OO#.
5 ..##OOO.#.
6 #...##.###
```

### Idea

We model this as a shortest-path problem in an implicit graph. Using BFS, we start from (1,1) and expand to neighboring positions only if they are open and not yet visited. We continue until we reach the target (31,39), counting the number of steps taken.

## Part 2

Now, we want to find how many unique locations can be reached within **at most 50 steps** starting from (1,1), using the same movement and wall-checking rules.

### Idea

We reuse the BFS approach but instead of stopping at a target, we explore until we reach a depth of 50 steps. We count how many distinct positions we visited during this search and return that as the result.