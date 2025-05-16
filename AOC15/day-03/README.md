## Part 1

Santa is delivering presents to an **infinite two-dimensional grid of houses**. He starts at position `(0, 0)` and moves according to a sequence of directions:

- `^` = move north  
- `v` = move south  
- `>` = move east  
- `<` = move west 

Each move takes Santa exactly one house in the corresponding direction, and he **delivers a present at each house he visits**. Our job is to find how many houses receive at least one present.

**Examples:**

- Input: `>` → Output: `2`
- Input: `^>v<` → Output: `4`
- Input: `^v^v^v^v^v` → Output: `2`

### Idea 

We can store santa's current location in a variable. After moving santa according to each direction, add the location to a set (stores only unique elements). The number of unique elements in the set represents the number of houses that received at least one present.

## Part 2

Santa’s job was tough, so this year he has help — a **robot version of himself**: **Robo-Santa**!

Santa and Robo-Santa both start at the same position `(0, 0)` and take turns following the instructions from the elf:

- Even-indexed steps (`0, 2, 4, ...`) are taken by **Santa**
- Odd-indexed steps (`1, 3, 5, ...`) are taken by **Robo-Santa**
- Both deliver presents to each house they visit

Again, our job is to find how many houses receive at least one present.

**Examples:**

- Input: `^>` → Output: `3`
- Input: `^>v<` → Output: `3`
- Input: `^v^v^v^v^v` → Output: `11`

### Idea

We can store Santa's and Robo-Santa's current locations in two separate variables. After moving the appropriate one according to each direction, we add the corresponding location to a set (which stores only unique elements). The number of unique elements in the set represents the number of houses that received at least one present.