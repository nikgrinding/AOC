## Part 1

You’re given a grid where codes are filled diagonally starting at position `(1,1)` and moving in diagonals like:
```
(1,1) → (2,1) → (1,2) → (3,1) → (2,2) → (1,3) → ...
```

Each position contains a code calculated from the previous one using this formula:
```
next_code = (current_code * 252533) % 33554393
```

The first code at `(1,1)` is `20151125`  
You need to compute the code at a specific position like `(row, column)`

**Examples:**  
Input: `(row=4, col=2)`  
You first compute the cell number in diagonal order (14th in this case), and then apply the formula 13 times to get the result

### Idea

To find the value at a particular cell `(row, col)`:
- Compute the cell number in diagonal order using the formula:  
  `cell = (row + col - 1)(row + col - 2)/2 + col`
- Generate the code by applying the recurrence relation that many times
- Return the final code

## Part 2

There is no Part 2 for Day 25
<p style = "font-size: 30px; font-weight: bold;"> And that's it — the sleigh is fully loaded, the code is cracked, and Advent of Code 2015 is complete! 🎄</p>
