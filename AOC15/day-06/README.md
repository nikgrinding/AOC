## Part 1

Your neighbors keep defeating you in the holiday house decorating contest year after year, but this time you're going all in — by deploying **one million lights** in a 1000×1000 grid!

Each light in the grid starts in the **off** state. Santa has sent you a list of **instructions** to turn on, turn off, or toggle the state of rectangular sections of the grid. Your task is to determine how many lights are **on** after executing all of Santa's instructions.

**Grid and Coordinates**

- The lights are arranged in a 1000×1000 grid.
- Each light is identified by a coordinate pair `(x, y)` where `0 <= x <= 999` and `0 <= y <= 999`.
- Each instruction specifies an inclusive rectangular region from a top-left coordinate to a bottom-right coordinate.

**Instructions Format**

Instructions are of the form:

- `turn on x1,y1 through x2,y2` — Turns **on** all lights in the specified range.
- `turn off x1,y1 through x2,y2` — Turns **off** all lights in the specified range.
- `toggle x1,y1 through x2,y2` — **Flips** the state of each light: on to off, or off to on.

**Examples**

- `turn on 0,0 through 999,999`  
  Turns **on** every light in the entire grid (1,000,000 lights).

- `toggle 0,0 through 999,0`  
  Toggles the first row of lights (1,000 lights).

- `turn off 499,499 through 500,500`  
  Turns **off** 4 lights in the middle of the grid.

### Idea

We represent the grid using a 2D list of size `1000 × 1000`, initialized with all zeros.

For each instruction:
- We extract the two coordinate pairs
- Depending on whether the instruction contains `"on"`, `"off"`, or `"toggle"`, we update the grid values:
  - `"on"` → set the value to 1
  - `"off"` → set the value to 0
  - `"toggle"` → set the value to `1 - current`

Finally, we count the total number of lights that are **on**.

## Part 2

Just after you finish implementing your perfect light grid, you realize you've mistranslated Santa's instructions from Ancient Nordic Elvish.

It turns out that the lights you're using don't just turn on and off — they have **individual brightness controls**. Each light can have a **brightness of zero or more**, and the initial brightness of all lights is **zero**.

Santa's instructions actually mean the following:

- `"turn on"` increases the brightness of each light in the range by **1**.
- `"turn off"` decreases the brightness of each light in the range by **1**, to a **minimum of 0**.
- `"toggle"` increases the brightness of each light in the range by **2**.


**Examples**

- `turn on 0,0 through 0,0`  
  Affects a single light — increases its brightness by 1 → total brightness = **1**.

- `toggle 0,0 through 999,999`  
  Affects the entire 1000×1000 grid — increases each light's brightness by 2 → total brightness = **2,000,000**.

Your task is to determine the **total brightness** of all lights after processing all of Santa's instructions.

### Idea

We treat the grid as a 1000×1000 matrix where each cell stores an integer representing its current brightness.

- When the instruction is `"turn on"`, increment the brightness of each affected light by 1.
- When the instruction is `"turn off"`, decrement the brightness by 1, **but not below 0**.
- When the instruction is `"toggle"`, increment the brightness by 2.

At the end, **sum all the brightness values** in the grid to get the final result.