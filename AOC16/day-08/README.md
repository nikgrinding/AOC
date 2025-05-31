## Part 1

You're trying to read a smashed screen that uses a custom display technology. The screen is 50 pixels wide and 6 pixels tall, and starts with all pixels off. It supports three operations:

- `rect AxB`: turn on all pixels in a rectangle of width A and height B at the top-left
- `rotate row y=A by B`: shift row A to the right by B pixels, wrapping around
- `rotate column x=A by B`: shift column A down by B pixels, wrapping around

You're given a list of instructions encoded on a magnetic card and need to count how many pixels are lit (on) after executing all instructions.

**Example:**
```
rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1
```

**Output:**
```
.#..#.#
#.#....
.#.....
```

### Idea

We simulate the display as a 2D grid of characters and update it based on each instruction. We use list slicing to handle the rotations. After all instructions, we count how many `#` symbols are present.

## Part 2

In this part, instead of just counting pixels, we need to read a message displayed on the screen. Each letter is 5 pixels wide and 6 pixels tall. After running all instructions, the screen will show capital letters, and we need to read them visually.

### Idea

We use the same simulation as in Part 1 but at the end, we print the grid visually. Grouping the pixels into chunks of 5 allows us to read each letter manually and deduce the message from the printed result.