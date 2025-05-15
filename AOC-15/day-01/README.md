## Part 1

Santa is navigating a building using a string of instructions:

- `(` means go **up** one floor.
- `)` means go **down** one floor.

He starts at **floor 0**, and your task is to determine the **final floor** after processing the entire string.

**Examples:**

- Input: `(()(()(` → Output: `3`
- Input: `())` → Output: `-1`

### Idea

We can use a counter that increases for each `(` and decreases for each `)` in the input. Final value of the counter gives the output.

## Part 2

Now, given the same instructions, we need to find the position of the first character that causes him to enter the basement (floor -1).

**Examples:**

- Input: `)` → Output: `1`
- Input: `()())` → Output: `5`

### Idea

Along with the counter we used earlier, we can also store the index of the character we are processing. When the counter hits a negative value, we return the index.